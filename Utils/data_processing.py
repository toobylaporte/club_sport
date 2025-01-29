import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

def add_member(df, nom, prenom, date_naissance, categorie):
    new_member = pd.DataFrame({
        "ID": [len(df) + 1],
        "Nom": [nom],
        "Prénom": [prenom],
        "DateNaissance": [str(date_naissance)],
        "Catégorie": [categorie]
    })
    return pd.concat([df, new_member], ignore_index=True)

def add_performance(df, membre, date, distance, temps, ressenti):
    new_performance = pd.DataFrame({
        "Athlete": [membre],
        "Date": [date],
        "Distance": [distance],
        "Time": [temps],
        "Feeling": [ressenti]
    })
    return pd.concat([df, new_performance], ignore_index=True)
