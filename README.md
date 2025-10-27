Mental Health App (DASS-Based)

This DASS-based Mental Health App uses Machine Learning to predict your stress, anxiety, and depression scores. It also identifies if you are prone to any of these conditions and provides tips to help manage or reduce elevated levels.

🧠 About the Project

The app is designed to help users understand their mental health through the DASS Mental Health Survey data. By analyzing survey responses, the app provides personalized predictions and actionable guidance for maintaining mental well-being.

📊 Data

Source: DASS (Depression, Anxiety, Stress Scale) Mental Health Survey

Processing: All data operations were performed using Python libraries:

pandas & numpy for data manipulation

scikit-learn for machine learning models

seaborn & matplotlib for data visualization

⚙️ Machine Learning Models

The app uses two models to predict mental health scores:

Linear Regression – Predicts numerical scores for stress, anxiety, and depression.

Binary Logistic Regression – Determines whether the user is prone to each condition based on thresholds.

💻 Technologies Used

Python

Streamlit (for the web app interface)

Pandas, Numpy, Scikit-Learn, Seaborn, Matplotlib

🚀 How to Run

Clone the repository:

git clone <your-repo-link>


Navigate to the project folder:

cd "Mental Health Data Project/Mental Health App"


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run mental_health_app.py


Open the provided local URL in your browser.

📌 Features

Predicts Stress, Anxiety, and Depression scores

Identifies if the user is prone to any condition

Provides tips and recommendations to manage mental health

Visualizes survey data and predictions

⚠️ Disclaimer

This app is for educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the guidance of a qualified mental health professional regarding any mental health concerns.

Citation:
Rony, Golam Rabbany; Hossain, Md. Biplob; Chowdhury, ABM Alauddin; Ahmed, Foysal (2024), “Mental Health dataset based on DASS-21”, Mendeley Data, V1, doi: 10.17632/br82d4xkj7.1
