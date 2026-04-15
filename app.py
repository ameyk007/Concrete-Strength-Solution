import streamlit as st
import numpy as np
import pickle
import matplotlib.pyplot as plt
import shap

# Page config
st.set_page_config(page_title="Concrete AI Predictor", layout="wide")

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Sidebar
st.sidebar.title("👨‍💻 Profile")
st.sidebar.write("**Name:** Amey Karekar")
st.sidebar.write("**Email:** your_email@example.com")
st.sidebar.markdown("---")
st.sidebar.success("🚀 FAANG-Level ML App")

# Title
st.title("🏗️ Concrete Strength AI Predictor")

# Layout
col1, col2 = st.columns(2)

with col1:
    cement = st.slider("Cement", 0.0, 600.0, 200.0)
    slag = st.slider("Blast Furnace Slag", 0.0, 300.0, 100.0)
    flyash = st.slider("Fly Ash", 0.0, 300.0, 100.0)
    water = st.slider("Water", 0.0, 300.0, 150.0)

with col2:
    superplasticizer = st.slider("Superplasticizer", 0.0, 50.0, 10.0)
    coarseaggregate = st.slider("Coarse Aggregate", 0.0, 1200.0, 800.0)
    fineaggregate = st.slider("Fine Aggregate", 0.0, 1200.0, 800.0)
    age = st.slider("Age (days)", 1, 365, 28)

# Predict
if st.button("🚀 Predict Strength"):
    
    input_data = np.array([[cement, slag, flyash, water, superplasticizer,
                            coarseaggregate, fineaggregate, age]])

    prediction = model.predict(input_data)[0]

    st.success(f"💪 Predicted Strength: {prediction:.2f} MPa")

    # 📊 Gauge Chart
    fig, ax = plt.subplots()
    ax.barh(["Strength"], [prediction])
    ax.set_xlim(0, 100)
    st.pyplot(fig)

    # 📈 Feature Importance
    st.subheader("📊 Feature Importance")
    importance = model.feature_importances_
    features = ['cement','slag','flyash','water','superplasticizer',
                'coarseaggregate','fineaggregate','age']

    fig2, ax2 = plt.subplots()
    ax2.barh(features, importance)
    st.pyplot(fig2)

    # 🧠 SHAP Explainability
    st.subheader("🧠 Model Explainability (SHAP)")
    
    explainer = shap.Explainer(model)
    shap_values = explainer(input_data)

    fig3 = plt.figure()
    shap.plots.waterfall(shap_values[0], show=False)
    st.pyplot(fig3)
