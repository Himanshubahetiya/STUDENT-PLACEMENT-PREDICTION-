import streamlit as st

def show():
    # --- 1. Page Configuration ---
    st.set_page_config(
        page_title="Placement Prediction AI System",
        page_icon="🔮",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # --- 2. Custom CSS for Perfect Centering & Glossy Red Theme ---
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Inter:wght@300;400;600&display=swap');

            .stApp {
                background: radial-gradient(circle at 50% 50%, #2b0303 0%, #050505 80%) !important;
                background-color: #050505 !important;
                color: white;
                font-family: 'Inter', sans-serif;
            }

            /* Fixed Top Navbar */
            .navbar {
                display: flex; justify-content: space-between; align-items: center;
                padding: 1rem 8%; background: rgba(0, 0, 0, 0.8);
                backdrop-filter: blur(15px); position: fixed;
                top: 0; left: 0; width: 100%; z-index: 999;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            }

            /* Header Section */
            .header-box {
                text-align: center;
                padding-top: 100px;
                width: 100%;
                margin-bottom: 20px;
            }

            .main-title {
                font-family: 'Orbitron', sans-serif; font-size: clamp(35px, 6vw, 60px); 
                font-weight: 900; letter-spacing: 12px; text-transform: uppercase;
                margin: 0; color: #ffffff; text-shadow: 0 0 30px rgba(255, 49, 49, 0.6);
            }

            .sub-title {
                color: #ff3131; font-family: 'Orbitron'; letter-spacing: 6px; 
                font-size: 14px; margin-top: 10px; font-weight: bold;
                text-align: center;
            }

            /* Absolute Centering for Image */
            .center-wrapper {
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%;
                margin: 20px 0;
            }

            .image-container img {
                max-width: 320px !important;
                filter: drop-shadow(0 0 50px rgba(255, 49, 49, 0.4));
            }

            /* Static Documentation Box */
            .doc-box {
                background: rgba(255, 255, 255, 0.03);
                border: 1px solid rgba(255, 49, 49, 0.3);
                border-radius: 12px; padding: 25px;
                backdrop-filter: blur(15px);
                font-family: 'Inter', sans-serif;
                color: #f0f0f0; font-size: 14px; line-height: 1.8;
                box-shadow: 0 15px 40px rgba(0,0,0,0.6);
            }

            /* Action Buttons */
            .stButton > button {
                background: #ff3131 !important; color: white !important;
                border: none !important; font-family: 'Orbitron' !important;
                font-size: 12px !important; font-weight: bold !important;
                letter-spacing: 2px !important; border-radius: 4px !important;
                padding: 12px 30px !important; box-shadow: 0 0 20px rgba(255, 49, 49, 0.4);
                transition: all 0.3s ease;
            }
            .stButton > button:hover { transform: scale(1.05); background: #d00 !important; }

            header, footer, #MainMenu {visibility: hidden;}
            .stDeployButton {display:none;}
        </style>
    """, unsafe_allow_html=True)

    # --- 3. Toggle State ---
    if 'show_docs' not in st.session_state:
        st.session_state.show_docs = False

    def toggle_docs():
        st.session_state.show_docs = not st.session_state.show_docs

    # --- 4. Custom Navbar ---
    st.markdown("""
        <div class="navbar">
            <div style="font-family:'Orbitron'; font-weight:900; font-size:22px; letter-spacing:2px;">PREDICTION AI</div>
            <div style="display:flex; gap:35px; font-size:10px; opacity:0.7; letter-spacing:1px;">
                <span>DASHBOARD</span><span>MODELS</span><span>FORECAST</span><span>ABOUT</span>
            </div>
            <div></div> 
        </div>
    """, unsafe_allow_html=True)

    # --- 5. Main Hero Section ---
    st.markdown("""
        <div class="header-box">
            <h1 class="main-title">PREDICTION AI SYSTEM</h1>
            <div class="sub-title">FOR A SMARTER FUTURE</div>
        </div>
    """, unsafe_allow_html=True)

    # --- 6. Content Logic ---
    if st.session_state.show_docs:
        # Side-by-Side when Doc is open
        _, col_img, col_text, _ = st.columns([0.4, 1.2, 1.8, 0.4], gap="large")
        with col_img:
            st.markdown('<div class="center-wrapper"><div class="image-container">', unsafe_allow_html=True)
            st.image("https://png.pngtree.com/png-vector/20250215/ourmid/pngtree-ai-technology-tape-sticker-no-background-png-image_15481663.png")
            st.markdown('</div></div>', unsafe_allow_html=True)
        with col_text:
            st.markdown("""
                <div class="doc-box">
                    <h3 style="font-family:'Orbitron'; color:#ff3131; font-size:18px;">🚀 SYSTEM DOCUMENTATION</h3>
                    <p>This advanced AI system processes student profiles to forecast their placement probability.</p>
                    <b>Core Modules:</b>
                    <ul>
                        <li><b>Resume Analysis:</b> NLP-based extraction.</li>
                        <li><b>Predictive Analytics:</b> Neural network scoring.</li>
                    </ul>
                    <b>Data Points:</b> CGPA, Coding Skills, Internships, Projects, Certifications, Age, Gender, and Branch.
                </div>
            """, unsafe_allow_html=True)
    else:
        # Pure Centered Image (No columns used here to ensure absolute center)
        st.markdown("""
            <div class="center-wrapper">
                <div class="image-container">
                    <img src="https://png.pngtree.com/png-vector/20250215/ourmid/pngtree-ai-technology-tape-sticker-no-background-png-image_15481663.png">
                </div>
            </div>
        """, unsafe_allow_html=True)

    # --- 7. Buttons (Centered) ---
    st.markdown("<br><br>", unsafe_allow_html=True)
    b_col1, b_col2, b_col3, b_col4, b_col5 = st.columns([2, 1, 0.1, 1, 2])

    with b_col2:
        # Button click hone par step 1 set karega aur rerun karega
        if st.button("GET STARTED ↗", use_container_width=True):
            st.session_state.step = 1
            st.rerun()

    with b_col4:
        st.button("READ DOCUMENT ↗", on_click=toggle_docs, use_container_width=True)
    

if __name__ == "__main__":
    show()