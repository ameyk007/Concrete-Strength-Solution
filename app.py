import streamlit as st
import numpy as np
import pickle

# Page config
st.set_page_config(page_title="Concrete AI Predictor", page_icon="🏗️", layout="wide")

# Load model
model = pickle.load(open("model.pkl", "rb"))

# 🌈 Advanced Glassmorphism CSS
st.markdown("""
<style>

/* Background Gradient */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Glass Card */
.glass {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    transition: 0.3s;
}

/* Hover effect */
.glass:hover {
    transform: scale(1.02);
    box-shadow: 0 10px 40px rgba(0,0,0,0.6);
}

/* Title */
.title {
    font-size: 48px;
    font-weight: bold;
    text-align: center;
    background: linear-gradient(90deg, #00dbde, #fc00ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #fc00ff, #00dbde);
    color: white;
    border-radius: 25px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 20px rgba(255,255,255,0.5);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(0,0,0,0.4);
    backdrop-filter: blur(10px);
}

</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 👨‍💻 Profile")
st.sidebar.write("**Name:** Amey Karekar")
st.sidebar.write("**Email:** your_email@example.com")
st.sidebar.markdown("---")
st.sidebar.success("🚀 AI Powered App")

# Title
st.markdown('<p class="title">🏗️ Concrete Strength AI Predictor</p>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Layout
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    cement = st.number_input("Cement", min_value=0.0)
    slag = st.number_input("Blast Furnace Slag", min_value=0.0)
    flyash = st.number_input("Fly Ash", min_value=0.0)
    water = st.number_input("Water", min_value=0.0)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    superplasticizer = st.number_input("Superplasticizer", min_value=0.0)
    coarseaggregate = st.number_input("Coarse Aggregate", min_value=0.0)
    fineaggregate = st.number_input("Fine Aggregate", min_value=0.0)
    age = st.number_input("Age (days)", min_value=1)
    st.markdown('</div>', unsafe_allow_html=True)

# Button
st.markdown("<br>", unsafe_allow_html=True)

if st.button("⚡ Predict Now"):
    
    input_data = np.array([[cement, slag, flyash, water, superplasticizer,
                            coarseaggregate, fineaggregate, age]])

    prediction = model.predict(input_data)

    st.markdown(f"""
    <div class="glass" style="text-align:center; font-size:28px;">
        💪 Predicted Strength: <b>{prediction[0]:.2f} MPa</b>
    </div>
    """, unsafe_allow_html=True)
