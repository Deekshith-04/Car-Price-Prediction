import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('car_price_model.pkl', 'rb'))

# Page config
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🚗 Car Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter car details to predict its selling price</p>", unsafe_allow_html=True)

st.markdown("---")

# Inputs
col1, col2 = st.columns(2)

with col1:
    present_price = st.number_input("Present Price (in lakhs)", min_value=0.0)
    kms_driven = st.number_input("Kilometers Driven", min_value=0)
    owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])

with col2:
    year = st.number_input("Year of Purchase", min_value=2000, max_value=2025)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

selling_type = st.selectbox("Seller Type", ["Dealer", "Individual"])

# Feature Engineering
car_age = 2025 - year

# Encoding (VERY IMPORTANT - must match training)
fuel_type_diesel = 1 if fuel_type == "Diesel" else 0
fuel_type_petrol = 1 if fuel_type == "Petrol" else 0

seller_individual = 1 if selling_type == "Individual" else 0

transmission_manual = 1 if transmission == "Manual" else 0

# Final input array (ORDER MUST MATCH TRAINING)
input_data = np.array([[present_price, kms_driven, owner, car_age,
                        fuel_type_diesel, fuel_type_petrol,
                        seller_individual, transmission_manual]])

st.markdown("---")

# Predict Button
if st.button("💰 Predict Price"):
    prediction = model.predict(input_data)[0]
    
    st.markdown(f"""
        <div style='text-align:center; padding:20px; border-radius:10px; background-color:#D5F5E3;'>
            <h2 style='color:#1E8449;'>Estimated Selling Price</h2>
            <h1 style='color:#117A65;'>₹ {round(prediction, 2)} Lakhs</h1>
        </div>
    """, unsafe_allow_html=True)