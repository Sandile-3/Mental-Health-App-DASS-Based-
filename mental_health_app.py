import streamlit as st
import joblib
import numpy as np

# --- Load Your Models ---
stress_model = joblib.load("model.joblib")          # Stress score predictor
anxiety_model = joblib.load("amodel.joblib")        # Anxiety score predictor
prone_anxiety_model = joblib.load("amodel2.joblib") # Prone to anxiety classifier
depression_model = joblib.load("dmodel.joblib")     # Depression score predictor
prone_depression_model = joblib.load("dmodel1.joblib")  # Prone to depression classifier


# --- Helper Functions ---
def get_stress_severity(score):
    if score <= 14:
        return "Normal"
    elif score <= 18:
        return "Mild"
    elif score <= 25:
        return "Moderate"
    elif score <= 33:
        return "Severe"
    else:
        return "Extremely Severe"


def get_anxiety_severity(score):
    if score <= 7:
        return "Normal"
    elif score <= 9:
        return "Mild"
    elif score <= 14:
        return "Moderate"
    elif score <= 19:
        return "Severe"
    else:
        return "Extremely Severe"


def get_depression_severity(score):
    if score <= 9:
        return "Normal"
    elif score <= 13:
        return "Mild"
    elif score <= 20:
        return "Moderate"
    elif score <= 27:
        return "Severe"
    else:
        return "Extremely Severe"


def stress_recommendations(score):
    """Provide practical tips depending on stress level."""
    if score <= 14:
        return "✅ Keep maintaining balance — continue healthy habits and rest well."
    elif score <= 18:
        return "😌 Try deep breathing or light exercise. Make sure you rest properly and stay socially connected."
    elif score <= 25:
        return "⚠️ Take breaks often, talk about what’s stressing you, and consider journaling or meditating."
    else:
        return "🚨 High stress level — it’s important to seek emotional support or speak with a counsellor."


# --- Streamlit UI ---
st.set_page_config(page_title="DASS-21 Mental Health Predictor", page_icon="🧠", layout="wide")

st.title("🧠 Mental Well-being Assessment Tool (DASS-Based)")
st.markdown(
    "This tool predicts your **Stress**, **Anxiety**, and **Depression** scores using trained "
    "Machine Learning models based on the DASS-21 mental health survey. "
    "It also indicates whether you may be **prone** to any of these conditions, "
    "helping you understand your mental health risk and take early steps."
)
st.info(
    "⚠️ **Note:** This app provides AI-based predictions — not a professional diagnosis. "
    "If your results indicate distress, please reach out to a mental health professional or counsellor."
)

st.markdown("---")

# --- User Selection ---
assessment_type = st.selectbox(
    "Select the assessment you'd like to take:",
    ["Stress Assessment", "Anxiety Assessment", "Depression Assessment"]
)

# Stress Questions
stress_questions = [
    "I found it hard to wind down",
    "I tended to over-react to situations",
    "I felt that I was using a lot of nervous energy",
    "I found myself getting agitated",
    "I found it difficult to relax",
    "I was intolerant of anything that kept me from getting on with what I was doing",
    "I felt that I was rather touchy"
]

# Anxiety Questions
anxiety_questions = [
    "I was aware of dryness of my mouth",
    "I experienced breathing difficulty (e.g., rapid breathing without exertion)",
    "I experienced trembling (e.g., in the hands)",
    "I was worried about situations in which I might panic and make a fool of myself",
    "I felt I was close to panic",
    "I was aware of the action of my heart in the absence of physical exertion",
    "I felt scared without any good reason"
]

# Depression Questions
depression_questions = [
    "I couldn’t seem to experience any positive feeling at all",
    "I found it difficult to work up the initiative to do things",
    "I felt that I had nothing to look forward to",
    "I felt down-hearted and blue",
    "I was unable to become enthusiastic about anything",
    "I felt I wasn’t worth much as a person",
    "I felt that life was meaningless"
]


# --- Select questions based on assessment ---
if assessment_type == "Stress Assessment":
    selected_questions = stress_questions
elif assessment_type == "Anxiety Assessment":
    selected_questions = anxiety_questions
elif assessment_type == "Depression Assessment":
    selected_questions = depression_questions

# --- Questionnaire Inputs ---
st.subheader("🧾 Answer the following questions (scale 0–3):")
cols = st.columns(3)
inputs = []
for idx, q in enumerate(selected_questions):
    with cols[idx % 3]:
        val = st.number_input(q, min_value=0, max_value=3, value=0)
        inputs.append(val)

input_data = np.array(inputs).reshape(1, -1)

# --- Prediction Button ---
if st.button("Submit Assessment"):
    if assessment_type == "Stress Assessment":
        score = stress_model.predict(input_data)[0]
        st.success(f"🧩 Predicted Stress Score: {score:.2f}")
        st.info(f"Severity Level: {get_stress_severity(score)}")
        st.markdown(f"**Recommendation:** {stress_recommendations(score)}")

    elif assessment_type == "Anxiety Assessment":
        score = anxiety_model.predict(input_data)[0]
        prone_score = prone_anxiety_model.predict([[score]])[0]

        severity = get_anxiety_severity(score)
        st.success(f"🧩 Predicted Anxiety Score: {score:.2f}")
        st.info(f"Severity Level: {severity}")

        if prone_score == 1:
            st.warning(
                "⚠️ You are **prone to anxiety**. "
                "Even if your current anxiety level appears mild or moderate, a score close to the 'prone to anxiety' threshold indicates that you are at risk                  of developing higher anxiety. "
                "Consider using relaxation techniques, controlled breathing, mindfulness, and limiting stimulants like caffeine to manage your risk."
            )
        else:
            st.success("✅ You are not prone to anxiety — keep maintaining your emotional balance.")

    elif assessment_type == "Depression Assessment":
        score = depression_model.predict(input_data)[0]
        prone_score = prone_depression_model.predict([[score]])[0]

        severity = get_depression_severity(score)
        st.success(f"🧩 Predicted Depression Score: {score:.2f}")
        st.info(f"Severity Level: {severity}")

        if prone_score == 1:
            st.warning(
                "⚠️ You are **prone to depression**. "
                "Even though your current level may appear mild or moderate, your score is close to the severe range. "
                "This indicates vulnerability to low mood during stressful times. "
                "Focus on social connection, enjoyable activities, adequate rest, and seeking support if needed."
            )
        else:
            st.success("✅ You are not prone to depression — continue maintaining healthy mental habits.")

st.markdown("---")
st.caption(
    "Developed using DASS-21 data and Machine Learning regression & classification models. "
    "Dataset citation: Rony, Golam Rabbany; Hossain, Md. Biplob; Chowdhury, ABM Alauddin; Ahmed, Foysal (2024), "
    "“Mental Health dataset based on DASS-21”, Mendeley Data, V1, doi: 10.17632/br82d4xkj7.1"
)

