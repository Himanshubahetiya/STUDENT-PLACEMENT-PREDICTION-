import streamlit as st

def show():
    # --- 1. Refined CSS (Fixed Button Size & Neon Sliders) ---
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;400;600&display=swap');

            /* Global Styles */
            .stApp {
                background: radial-gradient(circle at 50% 50%, #2b0303 0%, #050505 80%) !important;
                background-color: #050505 !important;
                color: white !important;
                font-family: 'Inter', sans-serif;
            }

            .page-title {
                font-family: 'Orbitron', sans-serif;
                font-size: 35px;
                font-weight: 900;
                text-align: center;
                letter-spacing: 5px;
                color: #ffffff;
                text-shadow: 0 0 20px rgba(255, 49, 49, 0.5);
                margin-top: 50px;
                margin-bottom: 10px;
            }

            .skill-card {
                background: rgba(255, 255, 255, 0.02);
                border: 1px solid rgba(255, 49, 49, 0.1);
                border-radius: 15px;
                padding: 35px;
                backdrop-filter: blur(15px);
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            }

            label {
                color: #ffffff !important;
                font-family: 'Orbitron' !important;
                font-size: 13px !important;
                letter-spacing: 2px !important;
                text-transform: uppercase;
                text-shadow: 0 0 10px rgba(255, 255, 255, 0.4) !important;
                margin-bottom: 15px !important;
                display: block;
            }

            /* --- SLIDER MINIMALIST LOOK --- */
            div[data-baseweb="slider"] > div {
                background-color: transparent !important;
                height: 4px !important;
            }
            div[data-baseweb="slider"] > div > div > div {
                background: #ff3131 !important;
                height: 4px !important;
                box-shadow: 0 0 10px rgba(255, 49, 49, 0.8);
            }
            div[data-testid="stTickBar"] { display: none !important; }
            div[role="slider"] {
                background-color: #ffffff !important;
                border: 2px solid #ff3131 !important;
                box-shadow: 0 0 15px rgba(255, 49, 49, 1) !important;
                height: 18px !important;
                width: 18px !important;
                top: 7px !important;
            }

            /* --- FIXED BUTTON SIZE LOGIC --- */
            .stButton > button {
                background: #ff3131 !important;
                color: white !important;
                font-family: 'Orbitron' !important;
                font-weight: bold !important;
                letter-spacing: 2px !important;
                border-radius: 4px !important;
                
                /* Consistency ke liye same size as previous pages */
                width: 220px !important; /* Text lamba hai isliye thoda wide rakha hai */
                height: 50px !important;
                display: flex !important;
                justify-content: center !important;
                align-items: center !important;
                
                box-shadow: 0 0 15px rgba(255, 49, 49, 0.4);
                transition: 0.3s;
                margin: 0 !important;
            }
            .stButton > button:hover {
                transform: scale(1.05);
                background: #d00 !important;
                box-shadow: 0 0 20px rgba(255, 49, 49, 0.6);
            }

            header, footer, #MainMenu {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # --- 2. Content ---
    st.markdown('<h1 class="page-title">SKILL ASSESSMENT</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#ff3131; font-family:\'Orbitron\'; font-size:12px; margin-bottom:40px;">STEP 04: CORE COMPETENCIES</p>', unsafe_allow_html=True)

    _, col_mid, _ = st.columns([1, 2.5, 1])
    
    with col_mid:
        st.markdown('<div class="skill-card">', unsafe_allow_html=True)
        
        coding = st.slider("Coding Proficiency", 0, 100, 60)
        comm = st.slider("Communication Skills", 0, 100, 65)
        soft = st.slider("Soft Skills", 0, 100, 70)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        cert = st.number_input(
            "Total Certifications",
            0, 10,
            int(st.session_state.resume_data.get("cert", 0)) if st.session_state.resume_data.get("cert") else 0
        )
        st.markdown('</div>', unsafe_allow_html=True)

        # --- Navigation (Updated with wide spacing & fixed size) ---
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Wide gap for corner-to-corner placement
        btn_col1, gap, btn_col2 = st.columns([1, 4.5, 1])
        
        with btn_col1:
            if st.button("⬅ BACK"):
                st.session_state.step = 3
                st.rerun()
                
        with btn_col2:
            # unique key for the final assessment button
            if st.button("GENERATE RESULT 🚀", key="final_gen"):
                st.session_state.coding = coding
                st.session_state.comm = comm
                st.session_state.soft = soft
                st.session_state.certs = cert
                st.session_state.step = 5
                st.rerun()

if __name__ == "__main__":
    show()