import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# ============================================
# PAGE CONFIG
# ============================================

st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌦️",
    layout="wide"
)

# ============================================
# CUSTOM CSS
# ============================================

st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }

    .stTextInput>div>div>input {
        background-color: #262730;
        color: white;
    }

    .weather-card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0px 0px 10px rgba(255,255,255,0.1);
    }

    .title {
        text-align: center;
        font-size: 45px;
        font-weight: bold;
        color: #00BFFF;
    }

    </style>
""", unsafe_allow_html=True)

# ============================================
# TITLE
# ============================================

st.markdown("<div class='title'>🌦️ Weather Dashboard</div>", unsafe_allow_html=True)

st.write("## Real-Time Weather Forecast Application")

# ============================================
# API KEY
# ============================================

API_KEY = "e9094dc9f5b9769b729c0259099aee70"

# ============================================
# USER INPUT
# ============================================

city = st.text_input("Enter City Name")

# ============================================
# FETCH WEATHER
# ============================================

if st.button("Get Weather"):

    if city == "":
        st.warning("Please enter city name")
    else:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            # ============================================
            # WEATHER DATA
            # ============================================

            city_name = data["name"]
            country = data["sys"]["country"]

            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]

            wind_speed = data["wind"]["speed"]

            description = data["weather"][0]["description"]
            icon = data["weather"][0]["icon"]

            icon_url = f"http://openweathermap.org/img/wn/{icon}@4x.png"

            # ============================================
            # DISPLAY WEATHER
            # ============================================

            st.success(f"Weather in {city_name}, {country}")

            col1, col2 = st.columns(2)

            with col1:
                st.image(icon_url, width=180)

            with col2:
                st.markdown(f"## 🌡️ {temperature} °C")
                st.write(f"### 🌤️ {description.title()}")

            # ============================================
            # METRICS
            # ============================================

            col1, col2, col3 = st.columns(3)

            col1.metric("Humidity", f"{humidity}%")
            col2.metric("Pressure", f"{pressure} hPa")
            col3.metric("Wind Speed", f"{wind_speed} m/s")

            # ============================================
            # GRAPH SECTION
            # ============================================

            st.write("## 📊 Weather Analytics")

            weather_data = {
                "Category": ["Temperature", "Humidity", "Pressure", "Wind Speed"],
                "Values": [temperature, humidity, pressure, wind_speed]
            }

            df = pd.DataFrame(weather_data)

            fig, ax = plt.subplots(figsize=(8,5))

            ax.bar(df["Category"], df["Values"])

            ax.set_title("Weather Statistics")

            st.pyplot(fig)

        else:
            st.error("❌ City not found")








