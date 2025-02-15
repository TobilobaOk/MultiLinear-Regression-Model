
import pickle
import streamlit as st
import numpy as np
import pandas as pd

# load the file that contain the model(model.pkl)
with open("model.pkl","rb") as f:
  model=pickle.load(f)

#give the streamlit app page a title

st.title("Vehicle One Year Resale Value Predictor")

# input widget for getting user value for X (feature matrix value)
price= st.slider("Price[thousand dollars]",min_value=0, max_value=100,value=20)
price= st.slider("Horsepower",min_value=0, max_value=100,value=20)
price= st.slider("Engine_size",min_value=0, max_value=100,value=20)

# After selecting price, the user then submits the price value
if st.button("Predict"):
  #take the price value, and format the value in the right way
  prediction = model.predict([[price]])[0].round(2)
  st.write("The predicted one year resale value of your vechile is",prediction,"thousand dollars")
