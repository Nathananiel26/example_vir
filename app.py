import streamlit as st
import joblib
import warnings



st.title(" Best Additional Model")

with st.form(key = "mode"): 
    num1 = st.number_input("Enter your first number ", min_value = 0, max_value = 2000)
    num2 = st.number_input("Enter your second number" , min_value = 0, max_value = 2000)
    submit_button = st.form_submit_button("prediction")

if submit_button:
    model = joblib.load("Best_Model")
    answer = model.predict([[num1,num2]])
    st.success(f"the predicted value is : {answer[0]}")
    st.balloons()
    
