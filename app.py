import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

# App Title
st.title("Concrete Strength Prediction App 🏗️")

st.write("Enter the values below to predict concrete compressive strength (MPa)")

# Input fields
cement = st.number_input("Cement", min_value=0.0)
slag = st.number_input("Blast Furnace Slag", min_value=0.0)
flyash = st.number_input("Fly Ash", min_value=0.0)
water = st.number_input("Water", min_value=0.0)
superplasticizer = st.number_input("Superplasticizer", min_value=0.0)
coarseaggregate = st.number_input("Coarse Aggregate", min_value=0.0)
fineaggregate = st.number_input("Fine Aggregate", min_value=0.0)
age = st.number_input("Age (days)", min_value=1)

# Prediction button
if st.button("Predict Strength"):
    
    # Create input array
    input_data = np.array([[cement, slag, flyash, water, superplasticizer,
                            coarseaggregate, fineaggregate, age]])
    
    # Prediction
    prediction = model.predict(input_data)

    # Output
    st.success(f"Predicted Concrete Strength: {prediction[0]:.2f} MPa")
