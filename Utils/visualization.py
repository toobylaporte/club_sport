import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

def plot_speed_evolution(df, athlete_name):
    """
    Crée un graphique Matplotlib montrant l'évolution de la vitesse d'un athlète.
    
    Parameters:
        df (pd.DataFrame): DataFrame contenant les données des performances.
        athlete_name (str): Nom de l'athlète pour filtrer les données.

    Returns:
        fig: Figure Matplotlib à afficher avec Streamlit.
    """
    filtered_df = df[df['Athlete'] == athlete_name]
    
    if filtered_df.empty:
        raise ValueError(f"Aucune donnée trouvée pour l'athlète : {athlete_name}")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(filtered_df['Date'], filtered_df['Speed'], marker='o', label='Vitesse')
    ax.set_title(f"Évolution de la vitesse - {athlete_name}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Vitesse (m/s)")
    ax.legend()
    plt.xticks(rotation=45)
    
    return fig


def plotly_speed_evolution(df, athlete_name):
    """
    Crée un graphique interactif Plotly montrant l'évolution de la vitesse d'un athlète.
    
    Parameters:
        df (pd.DataFrame): DataFrame contenant les données des performances.
        athlete_name (str): Nom de l'athlète pour filtrer les données.

    Returns:
        fig: Figure Plotly à afficher avec Streamlit.
    """
    filtered_df = df[df['Athlete'] == athlete_name]
    
    if filtered_df.empty:
        raise ValueError(f"Aucune donnée trouvée pour l'athlète : {athlete_name}")
    
    fig = px.line(
        filtered_df,
        x="Date",
        y="Speed",
        title=f"Évolution de la vitesse - {athlete_name}",
        labels={"Speed": "Vitesse (m/s)", "Date": "Date"},
        markers=True
    )
    
    return fig


def plot_correlation_matrix(df):
    """
    Crée une matrice de corrélation sous forme de graphique Plotly Heatmap.
    
    Parameters:
        df (pd.DataFrame): DataFrame contenant les colonnes numériques à corréler.

    Returns:
        fig: Figure Plotly Heatmap à afficher avec Streamlit.
    """
    correlation_matrix = df.corr()
    
    fig = px.imshow(
        correlation_matrix,
        text_auto=True,
        color_continuous_scale="Viridis",
        title="Matrice de corrélation"
    )
    
    return fig
