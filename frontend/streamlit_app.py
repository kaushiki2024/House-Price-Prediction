
import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Application title
st.title("🏠 House Price Prediction")
st.write("Enter the house details to predict its estimated price.")

# Input fields
st.subheader("House Details")

med_inc = st.number_input("Median Income", min_value=0.0, value=5.0)
house_age = st.number_input("House Age", min_value=0.0, value=25.0)
ave_rooms = st.number_input("Average Rooms", min_value=0.0, value=6.0)
ave_bedrms = st.number_input("Average Bedrooms", min_value=0.0, value=1.2)
population = st.number_input("Population", min_value=0.0, value=1000.0)
ave_occup = st.number_input("Average Occupancy", min_value=0.0, value=3.0)
latitude = st.number_input("Latitude", value=34.05)
longitude = st.number_input("Longitude", value=-118.24)

# Prediction button
if st.button("Predict House Price"):

    data = {
        "MedInc": med_inc,
        "HouseAge": house_age,
        "AveRooms": ave_rooms,
        "AveBedrms": ave_bedrms,
        "Population": population,
        "AveOccup": ave_occup,
        "Latitude": latitude,
        "Longitude": longitude
    }

    response = requests.post(
        "https://house-price-prediction-api-7wp7.onrender.com/predict",
        json=data
    )

    if response.status_code == 200:
        result = response.json()
        price = result["predicted_price"]

        st.success("Prediction completed!")
        st.metric("Predicted House Price", f"${price:,.2f}")

    else:
        st.error("Unable to get prediction from the API.")
