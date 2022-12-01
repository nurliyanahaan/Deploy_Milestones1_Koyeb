import streamlit as st
import requests

# Give the Name of the Application
st.title('Prediction Telco Customer Churn')

# Create Submit Form
with st.form(key='form_parameters'):
    tenure = st.slider('tenure', min_value=0, step=1, value=32,max_value=72)
    TotalCharges = st.number_input('TotalCharges', min_value=18.80, step=0.01,value=2283.30,max_value=8684.80)
    MonthlyCharges = st.number_input('MonthlyCharges', min_value=18.25, step=0.05,value=64.76,max_value=118.75)
    Contract = st.sidebar.selectbox(label='Contract', options=['Month-to-month','One year','Two year'])
    PaymentMethod = st.sidebar.selectbox(label='PaymentMethod', options=['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])
    InternetService = st.sidebar.selectbox(label='InternetService', options=['No','DSL','Fiber optic'])
    SeniorCitizen = st.sidebar.selectbox(label='SeniorCitizen', options=[0,1])
    Dependents = st.sidebar.selectbox(label='Dependents', options=['No', 'Yes'])
    
    submitted = st.form_submit_button('Predict')

# inference
if submitted:
    URL = 'https://churn-fadhilsadeli.koyeb.app/predict'
    param = {
    'tenure': tenure,
    'TotalCharges': TotalCharges,
    'MonthlyCharges': MonthlyCharges,
    'Contract': Contract,
    'PaymentMethod': PaymentMethod,
    'InternetService': InternetService,
    'SeniorCitizen': SeniorCitizen,
    'Dependents': Dependents
    }

    r = requests.post(URL, json=param)
    if r.status_code == 200:
        res = r.json()
        st.title('Telco Customer Churn is {}'.format(res['label_names']))
    else:
        st.title("Unexpected Error")
        st.write(r.status_code)
