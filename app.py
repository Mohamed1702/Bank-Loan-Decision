import streamlit as st
import pandas as pd
import numpy as np
import joblib
import sklearn

#@st.cache is a caching mechanism that allows your app to stay performant even when loading data from the web
#manipulating large datasets, or performing expensive computations.

inputs= joblib.load("input.h5")
Model = joblib.load("model.joblib")
st.header("Loan Predicator Decision Project")
# @st.cache(suppress_st_warning=True)
# def get_fvalue(val):
#     feature_dict = {"No":1,"Yes":2}
#     for key,value in feature_dict.items():
#         if val == key:
#             return value

# def get_value(val,my_dict):
#     for key,value in my_dict.items():
#         if val == key:
#             return value

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages
if app_mode=='Home':
    st.title('LOAN PREDICTION :')  
    st.image('Loan predict.jpg')
    st.markdown('Dataset :')
    data=pd.read_csv('loan.csv')
    st.write(data.head())
    st.markdown('Applicant Income VS Loan Amount ')
    st.bar_chart(data[['ApplicantIncome','LoanAmount']].head(20))
# Then in the Prediction page:
elif app_mode == 'Prediction':
    st.image('Loan decision.jpg')

    st.subheader('Sir/Mme , You need to fill all necessary informations in order to get a reply to your loan request !')
    st.sidebar.header("Informations about the client :")
def prediction(ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term,Credit_History,Gender,Married,Self_Employed,Education,Property_Area):
    
    if Gender == 'Male': 
        Gender = 1
    else:
        Gender = 0

    if Married == 'Yes': 
        Married = 1
    else:
        Married = 0 

    if Self_Employed == 'Yes': 
        Self_Employed = 1
    else:
        Self_Employed = 0 

    if Married == 'Graduate': 
        Education = 1
    else:
        Education = 0 

    if Property_Area == 'Urban': 
        Property_Area = 2

    elif Property_Area == 'Rural' :
        Property_Area = 0
    else:
        Property_Area = 1   
# Making predictions 
    prediction = Model.predict( 
        [[ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Gender,Married,Self_Employed,Education,Property_Area]])
     
    if prediction == 0:
        pred = 'According to our Calculations, you will not get the loan from Bank'
    else:
        pred = 'Congratulations!! you will get the loan from Bank'
    return pred        
#     gender_dict = {"Male":1,"Female":2}
#     feature_dict = {"No":1,"Yes":2}
#     edu={'Graduate':1,'Not Graduate':2}
#     prop={'Rural':1,'Urban':2,'Semiurban':3}
def main():
    Gender=st.sidebar.radio('Gender',('Male','Female'))
    Married=st.sidebar.radio('Married',('Yes','No'))
    Education=st.sidebar.radio('Education',('Graduate','Non Graduate'))
    ApplicantIncome=st.sidebar.slider('ApplicantIncome',0,10000,0,)
    CoapplicantIncome=st.sidebar.slider('CoapplicantIncome',0,10000,0,)
    Self_Employed=st.sidebar.radio('Self Employed',('Yes','No'))
    LoanAmount=st.sidebar.slider('LoanAmount in K EGP',9,700,200)
    Loan_Amount_Term=st.sidebar.selectbox('Loan_Amount_Term',(12,36,60,84,120,180,240,300.0,360,400,420,450,500,550,600))
    Credit_History=st.sidebar.radio('Credit_History',(0,1))
    Property_Area=st.sidebar.radio('Property_Area',('Urban','Semiurban','Rural'))
    result =""
#     Rural,Urban,Semiurban=0,0,0
#     if Property_Area == 'Urban' :
#         Urban = 1
#     elif Property_Area == 'Semiurban' :
#         Semiurban = 1
#     else :
#         Rural=1
#So we have seen both—when we label or one hot encoding our features and how to deal with it to successfully 
#created a working Streamlit app.
# data1={
#     'Gender':Gender,
#     'Married':Married,
#     'Education':Education,
#     'ApplicantIncome':ApplicantIncome,
#     'CoapplicantIncome':CoapplicantIncome,
#     'Self Employed':Self_Employed,
#     'LoanAmount':LoanAmount,
#     'Loan_Amount_Term':Loan_Amount_Term,
#     'Credit_History':Credit_History,
#     'Property_Area':[Rural,Urban,Semiurban],
#     }


#feature_list=[ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Gender,Married,Self_Employed,Education,Property_Area]

    single_sample = np.array(prediction).reshape(1,-1)
# if st.button("Predict"):
#     loaded_model = joblib.load('model.h5')
#     prediction = loaded_model.predict(single_sample)
#     if prediction[0] == 0:
#          st.error(
#     'According to our Calculations, you will not get the loan from Bank'
#     )
#     elif prediction[0] == 1:
#         st.success(
#     'Congratulations!! you will get the loan from Bank'
#     )
    if st.button("Predict"): 
        result = prediction(ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Gender,Married,Self_Employed,Education,Property_Area) 
        st.success('The Decision of loan is :  {}'.format(result))     
if __name__=='__main__': 
    main()


    
