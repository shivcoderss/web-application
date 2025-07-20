import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Iris Flower Predictor", layout="centered")
st.title("🌸 Iris Flower Species Prediction")
st.write("Input flower measurements to predict the species")

sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.8)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.3)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.3)

input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(input_data)
probabilities = model.predict_proba(input_data)

species = ["Setosa", "Versicolor", "Virginica"]
predicted_species = species[prediction[0]]

st.subheader("Prediction:")
st.success(f"The predicted Iris species is: **{predicted_species}**")

st.subheader("Prediction Probabilities:")
fig, ax = plt.subplots()
sns.barplot(x=species, y=probabilities[0], palette="Set2")
ax.set_ylabel("Probability")
st.pyplot(fig)

st.write(pd.DataFrame(probabilities, columns=species))