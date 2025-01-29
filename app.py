import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline
from utils.data_processing import load_data, save_data, add_member, add_performance
from utils.visualization import plot_performance
from models.predictive_model import analyze_sentiment

st.title("Club de Sport - Gestion des Performances")

# Chargement des données
athletes_df = load_data("data/athletes.csv")
members_df = load_data("data/members.csv")

# Menu principal
menu = st.sidebar.selectbox(
    "Menu",
    ["Accueil", "Ajouter un membre", "Ajouter une performance", "Liste des membres", "Performances d'un membre"]
)

if menu == "Accueil":
    st.write("Bienvenue dans l'application de gestion des performances du club de sport.")

elif menu == "Ajouter un membre":
    st.subheader("Ajouter un nouveau membre")
    with st.form("new_member"):
        nom = st.text_input("Nom")
        prenom = st.text_input("Prénom")
        date_naissance = st.date_input("Date de naissance")
        categorie = st.selectbox("Catégorie", ["Junior", "Senior", "Elite"])
        if st.form_submit_button("Ajouter"):
            members_df = add_member(members_df, nom, prenom, date_naissance, categorie)
            save_data(members_df, "data/members.csv")
            st.success(f"Membre {prenom} {nom} ajouté avec succès!")

elif menu == "Ajouter une performance":
    st.subheader("Ajouter une performance")
    with st.form("new_performance"):
        membre = st.selectbox("Membre", members_df["Nom"] + " " + members_df["Prénom"])
        date = st.date_input("Date de la performance")
        distance = st.number_input("Distance (m)", min_value=0)
        temps = st.number_input("Temps (s)", min_value=0)
        ressenti = st.slider("Ressenti", 1, 10)
        if st.form_submit_button("Ajouter"):
            athletes_df = add_performance(athletes_df, membre, date, distance, temps, ressenti)
            save_data(athletes_df, "data/athletes.csv")
            st.success("Performance ajoutée avec succès!")

elif menu == "Liste des membres":
    st.subheader("Liste des membres")
    st.dataframe(members_df)

elif menu == "Performances d'un membre":
    st.subheader("Performances d'un membre")
    membre = st.selectbox("Sélectionner un membre", members_df["Nom"] + " " + members_df["Prénom"])
    membre_performances = athletes_df[athletes_df["Athlete"] == membre]
    
    if not membre_performances.empty:
        st.plotly_chart(plot_performance(membre_performances))
        st.dataframe(membre_performances)
        
        sentiment = analyze_sentiment(membre_performances["FeelingText"].tolist())
        st.write(f"Sentiment général : {sentiment}")
    else:
        st.write("Aucune performance enregistrée pour ce membre.")

# Analyse de sentiment (conservée de l'ancien code)
st.header("Analyse de Sentiment")
feeling_input = st.text_input("Ressenti après l'entraînement (en texte) :", "")
if feeling_input:
    sentiment_analyzer = pipeline("sentiment-analysis")
    prediction = sentiment_analyzer(feeling_input)
    st.write(f"Sentiment prédit : {prediction[0]['label']} avec un score de {prediction[0]['score']:.2f}")

