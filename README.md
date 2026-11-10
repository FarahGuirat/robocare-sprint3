# robocare-sprint3
# RoboCare — Prévision du rendement agricole

Ce projet académique s’inspire de RoboCare, une plateforme de suivi agricole. Pour le sprint 3, j’ai développé un prototype qui estime le rendement du blé dur et de l’orge dans la région de Zaghouan à partir de données de pluviométrie.

## Données et modèle

Le prototype utilise un extrait de données agricoles sur Zaghouan. J’ai préparé les données, puis entraîné et évalué un modèle de régression dans Google Colab. L’application Streamlit utilise ce modèle pour afficher une estimation selon la culture sélectionnée et la quantité de pluie saisie.

Le prototype couvre deux cultures dans une seule région. L’estimation dépend des données utilisées pour entraîner le modèle.

## Lancer l’application

Depuis le dossier du projet, avec l’environnement Python activé et les dépendances installées, exécuter la commande suivante.

```bash
python -m streamlit run app.py
```

Dans l’interface, sélectionner **Blé dur** ou **Orge**, renseigner la pluviométrie, puis lancer la prévision.

## Suivi dans Jira

- `RGAI-12` — Prévision du rendement agricole
- `RGAI-24` — Préparation du jeu de données