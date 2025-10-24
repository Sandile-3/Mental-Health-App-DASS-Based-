import streamlit as st
import numpy as np
import joblib

# === Load Models ===
stress_model = joblib.load('model.joblib')
anxiety_model = joblib.load('amodel.joblib')
prone_anxiety_model = joblib.load('amodel2.joblib')
depression_model = joblib.load('dmodel.joblib')
prone_depression_model = joblib.load('dmodel1.joblib')

# === Dictionaries ===
stress_questions = {
    1: "I found it hard to wind down",
    6: "I tended to over-react to situations",
    8: "I felt that I was using a lot of nervous energy",
    11: "I found myself getting agitated",
    12: "I found it difficult to relax",
    14: "I was intolerant of anything that kept me from getting on with what I was doing",
    18: "I felt that I was rather touchy"
}

anxiety_questions = {
    2: "I was aware of dryness of my mouth",
    4: "I experienced breathing difficulty",
    7: "I experienced trembling",
    9: "I was worried about situations in which I might panic",
    15: "I felt I was close to panic",
    19: "I was aware of the action of my heart in the absence of physical exertion",
    20: "I felt scared without any good reason"
}

depression_questions = {
    3: "I couldn’t seem to experience any positive feeling at all",
    5: "I found it difficult to work up the initiative to do things",
    10: "I felt that I had nothing to look forward to",
    13: "I felt down-hearted and blue",
    16: "I was unable to become enthusiastic about anything",
    17: "I felt I wasn’t worth much as a person",
    21: "I felt that life was meaningless"
}

# === Helper Functions ===
def get_anxiety_severity(score):
    if 0 <= score <= 7:
        return "Normal"
    elif 8 <= score <= 9:
        return "Mild"
    elif 10 <= score <= 14:
        return "Moderate"
    elif 15 <= score <= 19:
        return "Severe"
    elif score >= 20:
        return "Extremely Severe"
    else:
        return "Invalid score"  # Handles negative or unexpected values

def get_depression_severity(score):
    if 0 <= score <= 9:
        return "Normal"
    elif 10 <= score <= 13:
        return "Mild"
    elif 14 <= score <= 20:
        return "Moderate"
    elif 21 <= score <= 27:
        return "Severe"
    elif score >= 28:
        return "Extremely Severe"
    else:
        return "Invalid score"  # Handles negative or unexpected values

# === Streamlit UI ===
st.title("🧠 Mental Well-being Assessment Tool (DASS-Based)")

assessment_type = st.selectbox("Select Assessment Type", ["Stress", "Anxiety", "Depression"])

questions = {
    "Stress": stress_questions,
    "Anxiety": anxiety_questions,
    "Depression": depression_questions
}[assessment_type]

responses = []

st.header(f"{assessment_type} Assessment")
st.write("Rate each statement from 0 to 3:")
st.write("0 = Did not apply at all | 1 = Some degree | 2 = Considerable degree | 3 = Most of the time")

for key, question in questions.items():
    value = st.selectbox(question, [0, 1, 2, 3], key=key)
    responses.append(value)

if st.button("Submit Assessment"):
    input_data = np.array(responses).reshape(1, -1)
    
    if assessment_type == "Stress":
        score = stress_model.predict(input_data)[0]
        st.success(f"Predicted Stress Score: {score:.2f}")

    elif assessment_type == "Anxiety":
          score = anxiety_model.predict(input_data)[0]
          prone_score = prone_anxiety_model.predict([[score]])[0]
    
          st.success(f"Predicted Anxiety Score: {score:.2f}")
          st.info(f"Severity Level: {get_anxiety_severity(score)}")  # <-- use score here
    
          # Optional: also show prone to anxiety classification
          #st.warning(f"Prone to Anxiety: {'Yes' if prone_score == 1 else 'No'}")

    elif assessment_type == "Depression":
          score = depression_model.predict(input_data)[0]
          prone_score = prone_depression_model.predict([[score]])[0]
          st.success(f"Predicted Depression Score: {score:.2f}")
          st.info(f"Severity Level: {get_depression_severity(score)}")  # <-- use score here
          # Optional: also show prone to depression classification
          #st.warning(f"Prone to Depression: {'Yes' if prone_score == 1 else 'No'}")

