import pandas as pd
import numpy as np

# Génération de données pour les performances des athlètes
def generate_athlete_data():
    np.random.seed(42)
    dates = pd.date_range(start='2025-01-01', end='2025-01-29', freq='D')
    athletes = [f"Athlete_{i}" for i in range(1, 21)]  # 20 athlètes

    data = []
    for athlete in athletes:
        for date in dates:
            distance = np.random.randint(180, 220)  # en mètres
            time = np.random.randint(25, 35)       # en secondes
            heart_rate = np.random.randint(150, 190)
            feeling = np.random.randint(1, 11)
            temperature = np.random.randint(15, 30)

            data.append([athlete, date, distance, time, heart_rate, feeling, temperature])

    df = pd.DataFrame(data, columns=["Athlete", "Date", "Distance", "Time", "HeartRate", "Feeling", "Temperature"])
    df["Speed"] = df["Distance"] / df["Time"]
    return df

# Génération de données pour les membres
def generate_member_data():
    members = []
    for i in range(1, 21):
        members.append({
            "ID": i,
            "Nom": f"Nom_{i}",
            "Prénom": f"Prénom_{i}",
            "DateNaissance": f"199{i%10}-01-{i:02d}",
            "Catégorie": np.random.choice(["Junior", "Senior", "Elite"])
        })
    return pd.DataFrame(members)

# Sauvegarder dans des fichiers CSV
athletes_df = generate_athlete_data()
members_df = generate_member_data()

athletes_df.to_csv("athletes.csv", index=False)
members_df.to_csv("members.csv", index=False)

print("Données générées et sauvegardées dans athletes.csv et members.csv.")
