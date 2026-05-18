import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

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
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}

.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #00BFFF;
}

.stTextInput input {
    border-radius: 12px;
    background-color: #1E1E1E;
    color: white;
}

div.stButton > button {
    background-color: #00BFFF;
    color: white;
    border-radius: 12px;
    height: 50px;
    width: 220px;
    font-size: 18px;
    border: none;
}

div.stButton > button:hover {
    background-color: #009acd;
}

</style>
""", unsafe_allow_html=True)

# ============================================
# TITLE
# ============================================

st.markdown("<div class='title'>🌦️ Weather Dashboard</div>", unsafe_allow_html=True)

st.sidebar.title("🌍 Weather Dashboard")

page = st.sidebar.radio(
    "Navigation", 
    ["Home", "Weather Analytics", "About Project"])

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

        with st.spinner("Fetching weather data..."):
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
            visibility = data["visibility"] / 1000

            description = data["weather"][0]["description"]
            icon = data["weather"][0]["icon"]

            icon_url = f"http://openweathermap.org/img/wn/{icon}@4x.png"

            # ============================================
            # DISPLAY WEATHER
            # ============================================

            st.success(f"Weather in {city_name}, {country}")
            if temperature > 30:
                st.warning("It's extremely hot outside!")
            elif temp > 15:
                st.info("Cold weather detected!")
            else:
                st.success("Weather is pleasant today!")

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
            st.write(f"### Visibility: {visibility} km")
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

            fig = px.bar(
                df,
                x="Category",
                y="Values",
                title="Weather Statistics",
                text="Values",
            )
            
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.error("❌ City not found")

# ============================================
# ABOUT PAGE
# ============================================

if page == "About Project":
    st.write("## About This Project")
    
    st.write("""
             This Weather Dashboard was developed using:
             
             -Python
             -Streamlit
             -OpenWeather REST API
             -Plotly for data visualization
             -pandas for data manipulation
             
             Features include:
             -Real-time weather data fetching
             -Interactive visualizations
             -Responsive UI
             -Live weather updates
             """)
    
st.markdown("===")
st.markdown(
    "Developed using python, streamlit, plotly, and openweather api"
)
             







