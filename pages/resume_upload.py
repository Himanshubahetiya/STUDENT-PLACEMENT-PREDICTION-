import streamlit as st
from utils.resume_parser import parse_resume

def show():
    # --- 1. Custom CSS for Consistent Red/Black Theme ---
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;400;600&display=swap');

            /* Background & Global Font */
            .stApp {
                background: radial-gradient(circle at 50% 50%, #2b0303 0%, #050505 80%) !important;
                background-color: #050505 !important;
                color: white !important;
                font-family: 'Inter', sans-serif;
            }

            /* Title Styling */
            .upload-title {
                font-family: 'Orbitron', sans-serif;
                font-size: 40px;
                font-weight: 900;
                text-align: center;
                letter-spacing: 5px;
                color: #ffffff;
                text-shadow: 0 0 20px rgba(255, 49, 49, 0.5);
                margin-bottom: 30px;
                margin-top: 50px;
            }

            /* File Uploader Container */
            .stFileUploader {
                background: rgba(255, 255, 255, 0.05);
                border: 1px dashed rgba(255, 49, 49, 0.5);
                border-radius: 15px;
                padding: 20px;
                backdrop-filter: blur(10px);
            }

            /* Button Styling (Red & Glossy) */
            .stButton > button {
                background: #ff3131 !important;
                color: white !important;
                border: none !important;
                font-family: 'Orbitron' !important;
                font-weight: bold !important;
                letter-spacing: 1.5px !important;
                border-radius: 4px !important;
                box-shadow: 0 0 15px rgba(255, 49, 49, 0.4);
                width: 100%;
                transition: 0.3s;
            }
            .stButton > button:hover {
                transform: scale(1.02);
                background: #d00 !important;
            }

            /* Success Message Styling */
            .stSuccess {
                background-color: rgba(0, 255, 0, 0.1) !important;
                color: #00ff00 !important;
                border: 1px solid #00ff00 !important;
            }

            header, footer, #MainMenu {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

    # --- 2. Title ---
    st.markdown('<h1 class="upload-title">UPLOAD RESUME</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:#ff3131; font-family:\'Orbitron\'; font-size:12px; margin-top:-20px; margin-bottom:40px;">STEP 01: AI FEATURE EXTRACTION</p>', unsafe_allow_html=True)

    # --- 3. File Uploader Section ---
    _, mid_col, _ = st.columns([1, 2, 1])
    with mid_col:
        uploaded_file = st.file_uploader("", type=["pdf"])

        if uploaded_file:
            with st.spinner("AI is parsing your resume..."):
                data = parse_resume(uploaded_file)
                st.session_state.resume_data = data
                st.success("✅ Resume Parsed Successfully")


        # --- 4. Navigation Buttons ---
        st.markdown("<br>", unsafe_allow_html=True)
        btn_col1, gap, btn_col2 = st.columns([1, 5.5, 1])

        with btn_col1:
            if st.button("⬅ BACK"):
                st.session_state.step = 0
                st.rerun()

        with btn_col2:
            if st.button("NEXT →", key="next_btn"):
                if st.session_state.resume_data.get("cgpa") is not None:
                    st.session_state.step = 2
                    st.rerun()
                else:
                    st.error("Please upload resume first!")

if __name__ == "__main__":
    show()