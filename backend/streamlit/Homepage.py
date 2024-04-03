import streamlit as st
import requests
import pandas as pd
import os
import matplotlib.pyplot as plt

# This code sets the MPLCONFIGDIR environment variable to /tmp/matplotlib/, which should be writable by all users.
os.environ['MPLCONFIGDIR'] = "/tmp/matplotlib/"

# Functie om tijdreeksgegevens op te halen van de FastAPI-server
def fetch_time_series_data():
    response = requests.get("http://api:8000/api/sensor-data/", timeout=5.0)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        # Kolom 'created_date' converteren naar datetime
        df['created_date'] = pd.to_datetime(df['created_date'])
        # Sorteren op 'created_date'
        df.sort_values(by='created_date', inplace=True)
        # 'created_date' als index instellen
        df.set_index('created_date', inplace=True)
        return df
    else:
        st.error("Kan geen gegevens ophalen")

def main():
    # Aangepast thema voor Streamlit
    primary_color = "#000000"  # Zwart
    secondary_color = "#FFFFFF"  # Wit
    font = "Arial"
    st.set_page_config(page_title="Visualisatie van Tijdreeks", layout="wide")

    # Aangepaste CSS-stijl voor Streamlit
    css = f"""
    <style>
        h1, h2, h3, h4, h5, h6 {{
            font-family: {font};
            color: {primary_color};
        }}
        .stProgress .st-aq {{
            border-radius: 0;
            background-color: {primary_color};
        }}
        .css-hi6a2p {{
            padding-top: 3rem;
        }}
        .dataframe {{
            font-family: {font};
            color: {primary_color};
        }}
        .main .block-container {{
            background-color: {secondary_color};
            padding: 2rem;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

    # House of Talents logo toevoegen
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "house_of_talents_logo.png")
    st.image(logo_path, width=200)

    st.title("Afstand tot object in parkeergarage House Of Talents")

    # Tijdreeksgegevens ophalen
    df = fetch_time_series_data()

    if df is not None:
        # Datumbereik selectie voor de tabel
        st.subheader("Datumbereik Selectie voor Tabel")
        start_datum_tabel = st.date_input("Start Datum", value=df.index.min(), max_value=df.index.max())
        eind_datum_tabel = st.date_input("Eind Datum", value=df.index.max(), min_value=start_datum_tabel)

        # Gegevens filteren op basis van geselecteerd datumbereik voor de tabel
        gefilterde_df_tabel = df.loc[start_datum_tabel:eind_datum_tabel]

        # Gefilterde tijdreeksgegevens weergeven
        st.subheader("Gefilterde Tijdreeksgegevens")
        st.write(gefilterde_df_tabel)

        # Visualisatie van gegevens
        st.subheader("Visualisatie van Gegevens")

        # Lijnplot met markers en datumbereik selectie
        st.subheader("Lijnplot met Markers en Datumbereik Selectie")
        st.write("Een lijnplot met markers om individuele datapunten en volatiliteit binnen een geselecteerd datumbereik weer te geven.")

        # Get the minimum and maximum dates from the DatetimeIndex
        min_date = df.index.min().to_pydatetime()
        max_date = df.index.max().to_pydatetime()

        # Use the converted datetime objects for the date_input with unique keys
        start_datum_plot = st.date_input("Start Datum", value=min_date, max_value=max_date, key="start_date")
        end_datum_plot = st.date_input("Eind Datum", value=max_date, min_value=start_datum_plot, key="end_date")

        # Convert the selected dates back to pandas Timestamps
        start_datum_plot = pd.Timestamp(start_datum_plot)
        end_datum_plot = pd.Timestamp(end_datum_plot)

        # Filter the DataFrame based on the selected date range
        gefilterde_df_plot = df.loc[start_datum_plot:end_datum_plot]

        # Create a line plot with different colors for each sensor_id
        fig, ax = plt.subplots(figsize=(12, 6))

        # Define colors for each sensor_id
        colors = {1: 'r', 2: 'b'}  # Red for sensor_id 1, blue for sensor_id 2

        for sensor_id, group in gefilterde_df_plot.groupby('sensor_id'):
            ax.plot(group.index, group['distance'], color=colors[sensor_id], label=f'Sensor {sensor_id}')

        ax.set_xlabel("Datum", fontsize=14, color=primary_color)
        ax.set_ylabel("Afstand", fontsize=14, color=primary_color)
        ax.tick_params(axis="x", rotation=45, colors=primary_color)
        ax.tick_params(axis="y", colors=primary_color)
        ax.spines['bottom'].set_color(primary_color)
        ax.spines['top'].set_color(primary_color)
        ax.spines['right'].set_color(primary_color)
        ax.spines['left'].set_color(primary_color)
        ax.legend()

        st.pyplot(fig)

        # Staafdiagram van de gemiddelde afstand per uur
        st.subheader("Staafdiagram van de Gemiddelde Afstand per Uur")
        st.write("Een staafdiagram dat de gemiddelde afstand per uur weergeeft, wat een indicatie kan geven van de bezettingsgraad van de parkeergarage.")

        gemiddelde_per_uur = gefilterde_df_plot.groupby(gefilterde_df_plot.index.hour)['distance'].mean()

        fig, ax = plt.subplots(figsize=(12, 6))
        gemiddelde_per_uur.plot(kind='bar', ax=ax, color=primary_color)
        ax.set_xlabel("Uur van de Dag", fontsize=14, color=primary_color)
        ax.set_ylabel("Gemiddelde Afstand", fontsize=14, color=primary_color)
        ax.tick_params(axis="x", rotation=0, colors=primary_color)
        ax.tick_params(axis="y", colors=primary_color)
        ax.spines['bottom'].set_color(primary_color)
        ax.spines['top'].set_color(primary_color)
        ax.spines['right'].set_color(primary_color)
        ax.spines['left'].set_color(primary_color)

        st.pyplot(fig)

        # Spreidingsdiagram van de afstand over tijd
        st.subheader("Spreidingsdiagram van de Afstand over Tijd")
        st.write("Een spreidingsdiagram dat de afstand over tijd weergeeft, wat inzicht kan geven in de fluctuaties in de bezettingsgraad van de parkeergarage.")

        fig, ax = plt.subplots(figsize=(12, 6))
        for sensor_id, group in gefilterde_df_plot.groupby('sensor_id'):
            ax.scatter(group.index, group['distance'], color=colors[sensor_id], label=f'Sensor {sensor_id}', alpha=0.5)

        ax.set_xlabel("Datum", fontsize=14, color=primary_color)
        ax.set_ylabel("Afstand", fontsize=14, color=primary_color)
        ax.tick_params(axis="x", rotation=45, colors=primary_color)
        ax.tick_params(axis="y", colors=primary_color)
        ax.spines['bottom'].set_color(primary_color)
        ax.spines['top'].set_color(primary_color)
        ax.spines['right'].set_color(primary_color)
        ax.spines['left'].set_color(primary_color)
        ax.legend()

        st.pyplot(fig)

if __name__ == "__main__":
    main()