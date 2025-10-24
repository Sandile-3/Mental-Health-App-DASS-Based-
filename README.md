# 🧠 Mental Health Assessment App (DASS-21 Based)

This project is a **Mental Health Assessment Tool** built on the **DASS-21 (Depression, Anxiety, and Stress Scale)** survey. The app uses machine learning models to predict **stress, anxiety, and depression scores**, then provides **severity levels** and indicates whether a user is **prone to anxiety or depression**.

The goal is to give users insights into their mental well-being and provide guidance on potential areas of concern.

---

## 📊 Features
- Predicts **Stress, Anxiety, and Depression scores** using regression models.
- Displays **severity levels**:
  - Normal
  - Mild
  - Moderate
  - Severe
  - Extremely Severe
- Interactive questionnaire based on DASS-21 items.
- Simple, user-friendly interface built with **Streamlit**.

---

## 🛠️ Technologies Used
- **Python** – ML models, data preprocessing, calculations.
- **Streamlit** – Web app interface and user interaction.
- **Joblib** – Model serialization and loading.

---

## 📝 How It Works
1. The user selects an assessment: **Stress, Anxiety, or Depression**.
2. The app presents a **questionnaire** with DASS-21 items.
3. Users respond with numbers **0–3**, corresponding to the answer scale:
   - 0 – Did not apply to me at all  
   - 1 – Applied to me to some degree, or some of the time  
   - 2 – Applied to me to a considerable degree or a good part of the time  
   - 3 – Applied to me very much or most of the time  
4. The app predicts the **score** using the relevant regression model.
5. The **severity level** is calculated and displayed.
6. The **prone classification** (Yes/No) is shown using the relevant classification model.

---

## 📈 Dataset
This app uses the **DASS-21 mental health dataset**:  
Rony, Golam Rabbany; Hossain, Md. Biplob; Chowdhury, ABM Alauddin; Ahmed, Foysal (2024), “Mental Health dataset based on DASS-21”, Mendeley Data, V1, doi: [10.17632/br82d4xkj7.1](https://doi.org/10.17632/br82d4xkj7.1)

---

## 🚀 Usage
Run the app locally with Streamlit:

```bash
streamlit run mental_health_app.py

