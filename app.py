from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


dossier = Path(__file__).parent

st.set_page_config(page_title="RoboCare — Prévision du rendement")
st.html(dossier / "style.css")

st.title("RoboCare — Prévision du rendement")
st.write("Estimer le rendement du blé dur ou de l’orge à Zaghouan.")

with st.form("prevision"):
    culture = st.selectbox("Culture", ["Blé dur", "Orge"])
    pluie_saisie = st.text_input(
        "Pluie cumulée de novembre à avril (mm)",
        value="280",
    )
    estimer = st.form_submit_button("Estimer", type="primary")

if estimer:
    try:
        pluie = float(pluie_saisie.strip().replace(",", "."))
    except ValueError:
        st.error("Vérifiez votre saisie. Entrez une quantité de pluie en mm.")
        st.stop()

    if not 120.40 <= pluie <= 497.88:
        st.error(
            "Vérifiez la quantité de pluie saisie. "
            "Elle doit être comprise entre 120,40 et 497,88 mm."
        )
        st.stop()

    modele = joblib.load(dossier / "modele_rendement.joblib")
    donnees = pd.DataFrame({
        "Culture": [culture],
        "Pluie nov. à avr. (mm)": [pluie],
    })

    rendement = modele.predict(donnees)[0]
    resultat = f"{rendement:.2f}".replace(".", ",")
    pluie_affichee = f"{pluie:g}".replace(".", ",")

    st.html(f"""
        <section class="rendement-carte" aria-live="polite">
            <div class="rendement-titre">Rendement estimé à Zaghouan</div>
            <div class="rendement-valeur">{resultat} <span>t/ha</span></div>
            <div class="rendement-detail">{culture} · {pluie_affichee} mm de pluie</div>
        </section>
    """)