import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go
import time

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Placement AI | Analytics Dashboard",
    page_icon="🎓",
    layout="wide"
)

# --- SIDEBAR & THEME TOGGLE ---
with st.sidebar:
    st.title("🎨 Customization")
    # This acts as our "Slide Button" for Dark Mode
    theme_mode = st.toggle("Enable Dark Mode", value=False)
    st.divider()

# --- DYNAMIC THEME COLORS ---
if theme_mode:
    bg_color = "#0f172a"
    card_bg = "#1e293b"
    text_color = "#f8fafc"
    border_color = "#334155"
else:
    bg_color = "#f8fafc"
    card_bg = "#ffffff"
    text_color = "#0f172a"
    border_color = "#e2e8f0"

# --- REFINED CSS WITH ANIMATIONS ---
st.markdown(f"""
    <style>
    /* Smooth Background Transition */
    .stApp {{
        background-color: {bg_color};
        transition: background-color 0.5s ease;
    }}
    
    /* Fade-in Animation for Cards */
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Global Text Transitions */
    h1, h2, h3, p, label {{
        color: {text_color} !important;
        font-family: 'Inter', sans-serif;
        transition: color 0.5s ease;
    }}

    /* Animated Input Card */
    div[data-testid="stVerticalBlock"] > div:has(div.stNumberInput) {{
        background-color: {card_bg};
        padding: 2rem;
        border-radius: 16px;
        border: 1px solid {border_color};
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        animation: fadeIn 0.8s ease-out;
        transition: all 0.5s ease;
    }}

    /* Button Hover Pulse */
    .stButton>button {{
        background: linear-gradient(90deg, #4f46e5, #3730a3);
        color: white !important;
        border: none;
        border-radius: 10px;
        padding: 0.8rem 2rem;
        font-size: 18px;
        font-weight: 700;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(79, 70, 229, 0.3);
    }}
    
    .stButton>button:hover {{
        transform: scale(1.02);
        box-shadow: 0 0 20px rgba(79, 70, 229, 0.5);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    try:
        with open("stp.pkl", "rb") as f:
            return pickle.load(f)
    except Exception:
        return None

model = load_model()

# --- MAIN UI ---
st.markdown(f"<h1 style='text-align: center; color: {text_color};'>🎓 STUDENT PLACEMENT PREDICTION</h1>", unsafe_allow_html=True)
st.write("---")

# Input Layout
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("### 👤 Personal Details")
    age = st.number_input("Candidate Age", 18, 35, 22)
    gender = st.selectbox("Gender Identification", ["Male", "Female"])
    branch = st.selectbox("Specialization", ["CSE", "IT", "ECE","EEE", "ME", "Civil"])

with col2:
    st.markdown("### 📈 Academic Performance")
    cgpa = st.slider("CGPA", 0.0, 10.0, 7.5, step=0.1)
    internship_count = st.number_input("Internship Experience", 0, 5, 1)
    project_count = st.number_input("Technical Projects", 0, 10, 2)

with col3:
    st.markdown("### 🏆 Skill Assessment")
    coding_score = st.slider("Coding Score", 0, 100, 60)
    comm_score = st.slider("Communication", 0, 100, 65)
    soft_score = st.slider("Soft Skills", 0, 100, 70)
    cert_count = st.number_input("Certifications", 0, 10, 1)

st.write(" ")
if st.button("Generate Report"):
    with st.spinner('🚀 Analyzing Data Patterns...'):
        time.sleep(1.2) # Adding a beat for the animation feel
        
    st.divider()
    
    # Prep Input
    data = pd.DataFrame([{
        "age": age, "gender": gender, "branch": branch, "cgpa": cgpa,
        "internship_count": internship_count, "project_count": project_count,
        "certifications_count": cert_count, "coding_skills_score": coding_score,
        "communication_skills_score": comm_score, "soft_skills_score": soft_score
    }])

    # Results Layout
    res_col, chart_col = st.columns([1, 1])

    with res_col:
        st.subheader("Result")
        
        # Determine Prediction
        if model:
            prediction = model.predict(data)
            is_placed = prediction[0] == "Placed"
        else:
            is_placed = True # Mock for Demo

        if is_placed:
            st.success("### ✅ PLACED")
            st.markdown("#### **CONGRATULATIONS!**")
            st.balloons()
        else:
            st.error("### ❌ NOT PLACED")
            st.markdown("#### **DO HARD WORK**")
            st.snow()

    with chart_col:
        categories = ['Coding', 'Communication', 'Soft Skills', 'GPA']
        values = [coding_score, comm_score, soft_score, cgpa*10]

        # Match chart colors to Dark Mode
        chart_text_color = "white" if theme_mode else "black"
        chart_grid_color = "#475569" if theme_mode else "#e2e8f0"

        fig = go.Figure(data=go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            fillcolor='rgba(79, 70, 229, 0.4)',
            line=dict(color="#4f46e5", width=3),
            marker=dict(color="#3730a3", size=8)
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True, 
                    range=[0, 100], 
                    gridcolor=chart_grid_color,
                    tickfont=dict(color=chart_text_color, size=10)
                ),
                angularaxis=dict(
                    tickfont=dict(size=14, color=chart_text_color, weight="bold"),
                    rotation=90,
                    direction="clockwise",
                    gridcolor=chart_grid_color
                ),
                bgcolor=card_bg
            ),
            showlegend=False,
            margin=dict(t=40, b=40, l=80, r=80),
            height=350,
            paper_bgcolor="rgba(0,0,0,0)"
        )
        st.plotly_chart(fig, use_container_width=True)

st.write("---")
st.caption(f"© 2026 Career Intelligence Systems. All rights reserved. | Theme: {'Dark' if theme_mode else 'Light'}")