import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

# Charger les données
athletes_df = pd.read_csv("athletes.csv")
members_df = pd.read_csv("members.csv")

# Titre de l'application
st.title("Application Club de Sport")
st.write("Suivi des performances, gestion des membres et analyse prédictive.")

# Section 1 : Suivi des performances
st.header("Suivi des Performances des Athlètes")
st.subheader("Données d'entraînement")
st.write(athletes_df.head())

# Filtrer par athlète
selected_athlete = st.selectbox("Sélectionnez un athlète :", athletes_df["Athlete"].unique())
filtered_df = athletes_df[athletes_df["Athlete"] == selected_athlete]

# Graphique d'évolution de la vitesse
fig, ax = plt.subplots()
ax.plot(filtered_df["Date"], filtered_df["Speed"], marker='o')
ax.set_title(f"Évolution de la vitesse - {selected_athlete}")
ax.set_xlabel("Date")
ax.set_ylabel("Vitesse (m/s)")
plt.xticks(rotation=45)
st.pyplot(fig)

# Section 2 : Gestion des membres
st.header("Gestion des Membres")
st.write(members_df)

with st.form("Inscription"):
    st.subheader("Inscription d'un nouveau membre")
    nom = st.text_input("Nom")
    prenom = st.text_input("Prénom")
    date_naissance = st.date_input("Date de naissance")
    categorie = st.selectbox("Catégorie sportive", ["Junior", "Senior", "Elite"])
    submit_button = st.form_submit_button(label="Ajouter")

if submit_button:
    new_member = {"ID": len(members_df) + 1, "Nom": nom, "Prénom": prenom, 
                  "DateNaissance": str(date_naissance), "Catégorie": categorie}
    members_df = members_df.append(new_member, ignore_index=True)
    members_df.to_csv("members.csv", index=False)
    st.success(f"Membre {nom} {prenom} ajouté avec succès !")

# Section 3 : Analyse prédictive
st.header("Analyse Prédictive")
st.subheader("Prédictions basées sur le ressenti")

sentiment_analyzer = pipeline("sentiment-analysis")

feeling_input = st.text_input("Ressenti après l'entraînement (en texte) :", "")
if feeling_input:
    prediction = sentiment_analyzer(feeling_input)
    st.write(f"Sentiment prédit : {prediction[0]['label']} avec un score de {prediction[0]['score']:.2f}")
