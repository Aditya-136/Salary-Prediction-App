import streamlit as st
import numpy as np

# ----- CUSTOM CSS -----
st.markdown("""
    <style>
    .stButton>button {
        background-color: #27AE60;
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.6em 1.2em;
        border-radius: 10px;
        transition: 0.3s;
        font-size: 1rem;
    }
    .stButton>button:hover {
        background-color: #00C853;
        color: white;
        transform: scale(1.05);
    }
    h1, h3 {
        color: #27AE60;
    }
    .emoji-title {
        font-size: 2.2em;
        font-weight: 700;
        color: #27AE60;
        margin-bottom: 1rem;
    }
    .summary-box {
        background-color: black;
        padding: 1.2em;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    hr {
        border: none;
        height: 1px;
        background: #cccccc;
        margin: 2em 0;
    }
    .footer {
        text-align: center;
        color: grey;
        font-size: 0.9em;
        margin-top: 3em
    }
    </style>
""", unsafe_allow_html=True)

# ----- TITLE -----
st.markdown("<div class='emoji-title'>Salary Prediction App", unsafe_allow_html=True)
st.markdown("Use this simple tool to estimate the expected annual salary based on candidate profile.")

# ----- SIDEBAR INPUTS -----
st.sidebar.header("Enter Candidate Details")

experience = st.sidebar.slider("Years of Experience", 0, 40, 2)
education = st.sidebar.selectbox("Education Level", ("High School", "Bachelor's", "Master's", "PhD"))
role = st.sidebar.selectbox("Job Role", ("Software Engineer", "Data Scientist", "Manager", "Designer"))

# ----- DUMMY PREDICTION LOGIC -----
def predict_salary(experience, education, role):
    base_salary = 30000
    experience_factor = experience * 1500

    education_bonus = {
        "High School": 0,
        "Bachelor's": 10000,
        "Master's": 20000,
        "PhD": 30000
    }

    role_bonus = {
        "Software Engineer": 20000,
        "Data Scientist": 25000,
        "Manager": 30000,
        "Designer": 15000
    }

    total = base_salary + experience_factor + education_bonus[education] + role_bonus[role]
    return round(total, -2)

# ----- PREDICT BUTTON -----
if st.sidebar.button("Predict Salary"):
    salary = predict_salary(experience, education, role)

    # SHOW INPUT SUMMARY
    st.markdown("### Candidate Summary")
    st.markdown(f"""
    <div class="summary-box">
        <ul>
            <li><strong>Experience:</strong> {experience} years</li>
            <li><strong>Education:</strong> {education}</li>
            <li><strong>Role:</strong> {role}</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # SHOW PREDICTION
    st.success(f"Estimated Annual Salary: **Rs {salary:,}**")

# ----- FOOTER -----
st.markdown("<hr style='margin-top: 3em;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Build using Stramlit</p>", unsafe_allow_html=True)