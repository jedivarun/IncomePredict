import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import streamlit as st


pickle_a=open("salary_predict.pickle","rb")
regressor=pickle.load(pickle_a) # our model

def predict_income(YearsExperience):
    prediction=regressor.predict([[YearsExperience]]) #predictions using our model
    return prediction

def main():
    st.title("Income prediction APP using ML") #simple title for the app
    html_temp="""
        <div>
        <h2>Income Prediction ML app</h2>
        </div>
        """
    st.markdown(html_temp,unsafe_allow_html=True) #a simple html 
    YearsExperience=st.text_input("Years of Experience") #giving inputs as used in building the model
    result=""
    if st.button("Predict"):
        result=predict_income(YearsExperience) #result will be displayed if button is pressed
    st.success("Expected Income for this level of experience is {}".format(result))
        
if __name__=='__main__':
    main()