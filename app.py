import streamlit as st
import pickle
import numpy as np

with open("crop_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🌱 Crop Recommendation System")
st.write("Enter the soil and environmental conditions to get a suitable crop recommendation.")

N = st.number_input("Nitrogen (N)", 0.0)
P = st.number_input("Phosphorus (P)", 0.0)
K = st.number_input("Potassium (K)", 0.0)
temperature = st.number_input("Temperature (°C)", 0.0)
humidity = st.number_input("Humidity (%)", 0.0)
ph = st.number_input("Soil pH", 0.0)
rainfall = st.number_input("Rainfall (mm)", 0.0)

if st.button("Recommend Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)

    st.success("Recommended Crop: " + prediction[0].upper())
