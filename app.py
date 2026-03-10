import streamlit as st
from pages import landing_page, resume_upload, personal_details, academic_details, skill_assessment, result_page

st.set_page_config(page_title="STUDENT PLACEMENT PREDICTION", page_icon="🚀", layout="wide")


if "step" not in st.session_state:
    st.session_state.step = 0

if "resume_data" not in st.session_state:
    st.session_state.resume_data = {
        "cgpa": None,
        "branch": None,
        "intern": None,
        "proj": None,
        "cert": None
    }

# Navigation
if st.session_state.step == 0:
    landing_page.show()

elif st.session_state.step == 1:
    resume_upload.show()

elif st.session_state.step == 2:
    personal_details.show()

elif st.session_state.step == 3:
    academic_details.show()

elif st.session_state.step == 4:
    skill_assessment.show()

elif st.session_state.step == 5:
    result_page.show()