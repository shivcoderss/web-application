# 🌸 Iris Flower Species Prediction App

A simple and interactive Streamlit web application to deploy a trained machine learning model for predicting Iris flower species based on user inputs. Built with Python, Streamlit, and a Random Forest Classifier.

## 🚀 Features

- User-friendly sliders for inputting flower measurements.
- Real-time prediction of Iris species.
- Visualized prediction probabilities with bar charts.
- Uses a trained Random Forest model.
- Deployable with Streamlit Cloud.

## 📊 Model Details

- **Dataset:** Iris dataset (150 samples, 3 classes)
- **Model:** RandomForestClassifier (100 estimators)
- **Target Labels:**
  - Setosa
  - Versicolor
  - Virginica

## 🛠️ Technologies Used

- Python
- Scikit-learn
- Streamlit
- Seaborn & Matplotlib
- Pandas & Numpy

## 📁 Project Structure

- streamlit_ml_app/
- ├── app.py # Streamlit web app
- ├── model.pkl # Trained ML model
- ├── save_model.py # Script to train and save model
- └── requirements.txt # Dependencies


## 💡 How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/streamlit-iris-app.git
   cd streamlit-iris-app
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:

  ```bash
   streamlit run app.py
   ```
