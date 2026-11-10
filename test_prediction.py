import joblib
import pandas as pd

modele = joblib.load("modele_rendement.joblib")

exemple = pd.DataFrame({
    "Culture": ["Blé dur"],
    "Pluie nov. à avr. (mm)": [280]
})

rendement = modele.predict(exemple)[0]
print(f"Rendement estimé : {rendement:.2f} t/ha")