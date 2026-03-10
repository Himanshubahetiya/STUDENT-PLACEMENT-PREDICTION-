import streamlit as st

def show():
    # --- 1. Updated Custom CSS for Right-Aligned Buttons ---
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;400;600&display=swap');

            /* Background */
            .stApp {
                background: radial-gradient(circle at 50% 50%, #2b0303 0%, #050505 80%) !important;
                background-color: #050505 !important;
                color: white !important;
                font-family: 'Inter', sans-serif;
            }

            /* Title Styling */
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

            /* Form Container Styling */
            .detail-card {
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 49, 49, 0.2);
                border-radius: 15px;
                padding: 30px;
                backdrop-filter: blur(15px);
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                margin-bottom: 20px;
            }

            /* White Glowing Labels for consistency */
            label {
                color: #ffffff !important;
                font-family: 'Orbitron' !important;
                font-size: 12px !important;
                letter-spacing: 1.5px !important;
                text-shadow: 0 0 10px rgba(255, 255, 255, 0.3) !important;
                text-transform: uppercase;
            }

            /* --- BUTTON ALIGNMENT FIX --- */
            
            /* Isse NEXT button wala column right side align ho jayega */
            [data-testid="column"]:nth-child(2) div.stButton {
                text-align: right;
            }

            .stButton > button {
        background: #ff3131 !important;
        color: white !important;
        font-family: 'Orbitron' !important;
        font-weight: bold !important;
        letter-spacing: 2px !important;
        border-radius: 4px !important;
        
        /* Width aur Height ko fix kar diya */
        width: 160px !important; 
        height: 48px !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        
        box-shadow: 0 0 15px rgba(255, 49, 49, 0.4);
        transition: 0.3s;
        margin: 0 !important;
    }

    /* Hover effect */
    .stButton > button:hover {
        transform: scale(1.05);
        background: #d00 !important;
        box-shadow: 0 0 20px rgba(255, 49, 49, 0.6);
    }
            
            .stButton > button:hover {
                transform: scale(1.05);
                background: #d00 !important;
                box-shadow: 0 0 20px rgba(255, 49, 49, 0.6);
            }
                
            header, footer, #MainMenu {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # --- 2. Page Header ---
    st.markdown('<h1 class="page-title">PERSONAL DETAILS</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#ff3131; font-family:\'Orbitron\'; font-size:12px; margin-bottom:40px;">STEP 02: IDENTITY & DOMAIN</p>', unsafe_allow_html=True)

    # --- 3. Form Section ---
    _, col_mid, _ = st.columns([1, 2.5, 1])
    
    with col_mid:
        st.markdown('<div class="detail-card">', unsafe_allow_html=True)
        
        age = st.number_input("Age", 18, 35, 22)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])

        branch_list = ["CSE", "IT", "ECE", "EEE", "ME", "Civil"]
        default_branch = st.session_state.resume_data.get("branch", None)
        idx = branch_list.index(default_branch) if default_branch in branch_list else 0

        branch = st.selectbox("Branch", branch_list, index=idx)
        st.markdown('</div>', unsafe_allow_html=True)

       # --- 4. Navigation (Same logic as Resume Page) ---
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Ratio [1, 5.5, 1] use karne se NEXT extreme right mein chala jayega
        btn_col1, gap, btn_col2 = st.columns([1, 5, 1])
        
        with btn_col1:
            if st.button("⬅ BACK"):
                st.session_state.step = 1
                st.rerun()
                
        with btn_col2:
            # unique key "next_personal" add ki hai conflict se bachne ke liye
            if st.button("NEXT →", key="next_personal"):
                st.session_state.age = age
                st.session_state.gender = gender
                st.session_state.branch = branch
                st.session_state.step = 3
                st.rerun()

if __name__ == "__main__":
    show()