import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="Salary Prediction App", 
    page_icon="💼",  
    layout="wide"    
)
st.sidebar.title("Sidebar")
st.sidebar.write("Use the links below to view other files:")
st.sidebar.write("[Sales Prediction](http://localhost:8501/)", unsafe_allow_html=True)
st.sidebar.write("[AskMe](http://localhost:8501/AskMe)", unsafe_allow_html=True)

st.title("Salary Prediction App")
st.divider()

st.write("With this App, you can get estimations for the salaries of the company employees.")

years = st.number_input("Enter the years in company", value=1, step=1, min_value=0)
jobrate = st.number_input("Enter the JobRate", value=3.5, step=0.5, min_value=0.0)

X = [years, jobrate]
st.divider()

model = joblib.load("linearmodel.pkl")

predict = st.button("Press the button for salary prediction")
st.divider()

if predict:
    st.balloons()

    X1 = np.array([X])
    prediction = model.predict(X1)[0]

    st.write(f"Salary Prediction is {prediction:,.2f}")
else:
    st.write("Press the button to make the prediction")
