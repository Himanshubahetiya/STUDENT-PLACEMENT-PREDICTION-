import streamlit as st
import pandas as pd
from utils.model_loader import load_model
import time

def show():
    # --- 1. Premium Result CSS ---
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;400;600&display=swap');

            .stApp {
                background: radial-gradient(circle at 50% 50%, #2b0303 0%, #050505 80%) !important;
                background-color: #050505 !important;
                color: white !important;
                font-family: 'Inter', sans-serif;
            }

            .result-title {
                font-family: 'Orbitron', sans-serif;
                font-size: 40px;
                font-weight: 900;
                text-align: center;
                letter-spacing: 6px;
                color: #ffffff;
                text-shadow: 0 0 30px rgba(255, 49, 49, 0.6);
                margin-top: 50px;
            }

            /* Main Dashboard Card */
            .result-card {
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 49, 49, 0.2);
                border-radius: 20px;
                padding: 40px;
                backdrop-filter: blur(20px);
                box-shadow: 0 20px 50px rgba(0,0,0,0.7);
                margin-bottom: 30px;
            }

            .status-placed {
                color: #00ffcc;
                font-family: 'Orbitron';
                font-size: 48px;
                font-weight: 900;
                text-shadow: 0 0 20px rgba(0, 255, 204, 0.6);
                margin-bottom: 10px;
            }

            .status-not-placed {
                color: #ff3131;
                font-family: 'Orbitron';
                font-size: 48px;
                font-weight: 900;
                text-shadow: 0 0 20px rgba(255, 49, 49, 0.6);
                margin-bottom: 10px;
            }

            /* Skill Stats Styling */
            .stat-box {
                border-left: 3px solid #ff3131;
                padding-left: 15px;
                margin: 10px 0;
                background: rgba(255, 49, 49, 0.05);
                padding-top: 5px;
                padding-bottom: 5px;
            }

            /* --- FIXED BUTTON SIZE (Same as Skills Page) --- */
            .stButton > button {
                background: #ff3131 !important;
                color: white !important;
                font-family: 'Orbitron' !important;
                font-weight: bold !important;
                letter-spacing: 2px !important;
                border-radius: 4px !important;
                width: 220px !important; 
                height: 50px !important;
                box-shadow: 0 0 15px rgba(255, 49, 49, 0.4);
                transition: 0.3s;
            }
            .stButton > button:hover {
                transform: scale(1.05);
                background: #d00 !important;
                box-shadow: 0 0 20px rgba(255, 49, 49, 0.6);
            }

            header, footer, #MainMenu {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # --- 2. Model Prediction ---
    model = load_model()
    data = pd.DataFrame([{
        "age": st.session_state.age,
        "gender": st.session_state.gender,
        "branch": st.session_state.branch,
        "cgpa": st.session_state.cgpa,
        "internship_count": st.session_state.internships,
        "project_count": st.session_state.projects,
        "certifications_count": st.session_state.certs,
        "coding_skills_score": st.session_state.coding,
        "communication_skills_score": st.session_state.comm,
        "soft_skills_score": st.session_state.soft
    }])

    # Prediction Logic
    if model:
        prediction = model.predict(data)
        placed = (prediction[0] == "Placed")
        # Pseudo-probability based on CGPA and Coding for UI bar
        prob = min(98, max(30, (st.session_state.cgpa * 6) + (st.session_state.coding * 0.4)))
    else:
        placed = data["cgpa"][0] > 7.5
        prob = 75 if placed else 40

    # --- 3. UI Content ---
    st.markdown('<h1 class="result-title">ANALYSIS COMPLETE</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#ff3131; font-family:\'Orbitron\'; font-size:12px; letter-spacing:3px; margin-bottom:40px;">PLACEMENT PREDICTION REPORT</p>', unsafe_allow_html=True)

    _, col_mid, _ = st.columns([1, 2.5, 1])
    
    with col_mid:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        
        if placed:
            st.balloons() 
            st.markdown('<h2 class="status-placed">PLACED ✅</h2>', unsafe_allow_html=True)
            st.markdown(f'<p style="color:#00ffcc; font-weight:bold;">Success Probability: {prob:.1f}%</p>', unsafe_allow_html=True)
        else:
            st.markdown('<h2 class="status-not-placed">NOT PLACED ❌</h2>', unsafe_allow_html=True)



        # --- 4. Corner Aligned Buttons ---
        st.markdown("<br><br>", unsafe_allow_html=True)
        btn_col1, gap, btn_col2 = st.columns([1, 4.5, 1])

        with btn_col1:
            if st.button("⬅ BACK"):
                st.session_state.step = 4
                st.rerun()
                
        with btn_col2:
            if st.button("Home Manu"):
                # Clear relevant keys
                for key in ['resume_data', 'cgpa', 'coding', 'step']:
                    if key in st.session_state:
                        del st.session_state[key]
                st.session_state.step = 0
                st.rerun()

if __name__ == "__main__":
    show()