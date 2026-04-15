import streamlit as st
import numpy as np
import pickle

# Page config
st.set_page_config(page_title="Concrete Strength Predictor", page_icon="🏗️", layout="wide")

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Custom CSS for premium UI
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    margin-bottom: 20px;
}
.title {
    font-size: 40px;
    font-weight: bold;
    color: #ffffff;
}
.subtitle {
    color: #cfcfcf;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 👨‍💻 About Me")
st.sidebar.write("**Name:** Amey Karekar")
st.sidebar.write("**Email:** your_email@example.com")

st.sidebar.markdown("---")
st.sidebar.info("Built using XGBoost & Streamlit 🚀")

# Title
st.markdown('<p class="title">🏗️ Concrete Strength Prediction</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Enter input values to predict compressive strength</p>', unsafe_allow_html=True)

# Layout: 2 columns
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    cement = st.number_input("Cement", min_value=0.0)
    slag = st.number_input("Blast Furnace Slag", min_value=0.0)
    flyash = st.number_input("Fly Ash", min_value=0.0)
    water = st.number_input("Water", min_value=0.0)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    superplasticizer = st.number_input("Superplasticizer", min_value=0.0)
    coarseaggregate = st.number_input("Coarse Aggregate", min_value=0.0)
    fineaggregate = st.number_input("Fine Aggregate", min_value=0.0)
    age = st.number_input("Age (days)", min_value=1)
    st.markdown('</div>', unsafe_allow_html=True)

# Predict button centered
st.markdown("<br>", unsafe_allow_html=True)
center_col = st.columns([1,2,1])[1]

with center_col:
    if st.button("🚀 Predict Strength"):
        input_data = np.array([[cement, slag, flyash, water, superplasticizer,
                                coarseaggregate, fineaggregate, age]])

        prediction = model.predict(input_data)

        st.success(f"💪 Predicted Strength: {prediction[0]:.2f} MPa")
