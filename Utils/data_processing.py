import pandas as pd
import numpy as np

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

# Sauvegarder dans un CSV pour le MVP
df = generate_athlete_data()
df.to_csv("data/athletes.csv", index=False)
