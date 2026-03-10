import streamlit as st

def show():
    # --- 1. Custom CSS (Fixed Button Size & Neon Slider) ---
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;400;600&display=swap');

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

            label {
                color: #ffffff !important;
                font-family: 'Orbitron' !important;
                font-size: 12px !important;
                letter-spacing: 1.5px !important;
                text-shadow: 0 0 10px rgba(255, 255, 255, 0.3) !important;
                text-transform: uppercase;
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
            div[role="slider"] {
                background-color: #ffffff !important;
                border: 2px solid #ff3131 !important;
                box-shadow: 0 0 15px rgba(255, 49, 49, 1) !important;
                height: 18px !important;
                width: 18px !important;
                top: 7px !important;
            }
            div[data-testid="stTickBar"] { display: none !important; }

            /* --- FIXED BUTTON SIZE LOGIC --- */
            .stButton > button {
                background: #ff3131 !important;
                color: white !important;
                font-family: 'Orbitron' !important;
                font-weight: bold !important;
                letter-spacing: 2px !important;
                border-radius: 4px !important;
                
                /* Size fix kiya gaya hai */
                width: 160px !important; 
                height: 48px !important;
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

    st.markdown('<h1 class="page-title">ACADEMIC PERFORMANCE</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#ff3131; font-family:\'Orbitron\'; font-size:12px; margin-bottom:40px;">STEP 03: SCORE & EXPERIENCE</p>', unsafe_allow_html=True)

    _, col_mid, _ = st.columns([1, 2, 1])
    with col_mid:
        cgpa = st.slider(
            "CGPA Score",
            0.0, 10.0,
            float(st.session_state.resume_data.get("cgpa", 0.0)) if st.session_state.resume_data.get("cgpa") else 0.0,
            step=0.1
        )

        intern = st.number_input(
            "Total Internships",
            0, 5,
            int(st.session_state.resume_data.get("intern", 0)) if st.session_state.resume_data.get("intern") else 0
        )

        proj = st.number_input(
            "Total Projects",
            0, 10,
            int(st.session_state.resume_data.get("proj", 0)) if st.session_state.resume_data.get("proj") else 0
        )
        
        # --- Navigation (Updated with wide spacing & fixed size) ---
        st.markdown("<br>", unsafe_allow_html=True)
        btn_col1, gap, btn_col2 = st.columns([1, 5, 1])

        with btn_col1:
            if st.button("⬅ BACK"):
                st.session_state.step = 2
                st.rerun()

        with btn_col2:
            # key "next_academic" use ki hai
            if st.button("NEXT →", key="next_academic"):
                st.session_state.cgpa = cgpa
                st.session_state.internships = intern
                st.session_state.projects = proj
                st.session_state.step = 4
                st.rerun()

if __name__ == "__main__":
    show()