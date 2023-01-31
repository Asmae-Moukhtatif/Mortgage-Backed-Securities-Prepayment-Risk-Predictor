import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

import streamlit as st

import pickle

from warnings import filterwarnings
filterwarnings('ignore')



st.write("""
# Mortgage Backed Securities Prepayment Risk Predictor
This Web interface shows **wheather a Mortgage Backed Securities Delinquent or Not** 
""")
st.image('data:image/jpeg;base64,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MstlbIZ/zl9+ReWyaEyPDWuZrp9AgDUL11JRF6S+x87JZHOfJG10fCL3MMe/RzS7X/1Jhl9Tpz/lDWk6tdWqXJor1l9cObGNW6MD92gJ1HMH7tf1dFuHSDFkz8rIjjitTMmdC4Q2G1eUvAf7dFiPo/SibGGWLwkZcF0TGYGUybOGWklu3Qjt5a/asfk7jRxwZLRjkht14onS7o67LR1lEDSOWv4phfqNkWaozWKddsdtstphlY18BbsjO/a9+p5B206cj+GqlR2BRr8PTlsUJ3y2SaIiEMfEHCJjBDXPG3Unn71JqO6bvuROb+qxX76xP9w1Sqis39Viv31if7hqlVUjmWURFGir53F5K3dfNWquk1oMrwyttcD0exxy8SkbhrtH2L2+lmje2GAvqnLQ332BYYAYRVED4+ETu7ef4qyrBCu7LxQpMdLL2quSjge6Q0p4cTXIl2ekVa0zpJObzt1ILWk689q7KmIyW7FGy2xsq1L52vsMYW2nTNdCHcB5GgG7bp2e1WoAD/v3rKbuY0YQfR+pfp17UdqF0WtguhEk7Z5nM2NBfK5pLNSdfcpxEUa0xtGwiIjoREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREETm/qsV++sT/AHDVKqKzf1WK/fWJ/uGqVVZxzLKIijQREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERBE5v6rFfvrE/3DVKqKzf1WK/fWJ/uGqVVZxzLKIijQREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERBE5v6rFfvrE/3DVKqKzf1WK/fWJ/uGqVVZxzKK4PSjvHGfDpvmk4PSjvHGfDpvmlLIi29ong9KO8cZ8Om+aTg9KO8cZ8Om+aUsiFvaJ4PSjvHGfDpvmk4PSjvHGfDpvmlLIhb2ieD0o7xxnw6b5pOD0o7xxnw6b5pSyIW9ong9KO8cZ8Om+aTg9KO8cZ8Om+aUsiFvaJ4PSjvHGfDpvmk4PSjvHGfDpvmlLIhb2ieD0o7xxnw6b5pOD0o7xxnw6b5pSyIW9ong9KO8cZ8Om+aTg9KO8cZ8Om+aUsiFvaJ4PSjvHGfDpvmk4PSjvHGfDpvmlLIhb2ieD0o7xxnw6b5pOD0o7xxnw6b5pSyIW9ong9KO8cZ8Om+aTg9KO8cZ8Om+aUsiFvaJ4PSjvHGfDpvmk4PSjvHGfDpvmlLIhb2ieD0o7xxnw6b5pOD0o7xxnw6b5pSyIW9ong9KO8cZ8Om+aTg9KO8cZ8Om+aUsiFvaJ4PSjvHGfDpvmk4PSjvHGfDpvmlLIhb2ieD0o7xxnw6b5pOD0o7xxnw6b5pSyIW9ong9KO8cZ8Om+aTg9KO8cZ8Om+aUsiFvaJ4PSjvHGfDpvmk4PSjvHGfDpvmlLIhb2ieD0o7xxnw6b5pOD0o7xxnw6b5pSyIW9ong9KO8cZ8Om+aTg9KO8cZ8Om+aUsiFvaJ4PSjvHGfDpvmk4PSjvHGfDpvmlLIhb2ieD0o7xxnw6b5pOD0o7xxnw6b5pSyIW9ong9KO8cZ8Om+aTg9KO8cZ8Om+aUsiFvaJ4PSjvHGfDpvmk4PSjvHGfDpvmlLIhb2ieD0o7xxnw6b5pOD0o7xxnw6b5pSyIW9ong9KO8cZ8Om+aTg9KO8cZ8Om+aUsiFvaJ4PSjvHGfDpvmk4PSjvHGfDpvmlLIhb2ieD0o7xxnw6b5pOD0o7xxnw6b5pSyIW9oSWhnLLqYtZCi6GC5VtubDRkje4wPEmm507gOz9VTaIo6iBERFEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQeXO0BJ0AGpJJ0AA56lVTN9MH4i7VpxYma42zFDNDNFOGNkErgxu0cMjt5dqnMtj3ZOnJUbbnql72uMsGhd6p12uB5aH2qk5SqKNqOvdnmnneyMRzSSzRmcueAHBrHbQSeWg0WepqRp52mf8efVqqj+OH0KOVsgIBbvZoJGg6ljj7NV719/JQGJwlqpb9PsZG1KX1+E2o4NEMLDoQxx5ucW9gJKhq3RnpDWttm9KhdDAbhqxF79G8CKWHH6+r7OI8yf+n9VaUZjeXV9URGF3L2t+k5reWvrOA5e9Z1PP+v2KmdQ9Jp2VjcmhknjbLHvlsPlcGHIVbbGl20E6NY4dqO6P5oOzRhZXi9JmrzxPZak48z23/S3h0zWNdwy3UaO3nXkDt9UdbR+TyVf1XRCVVZ8b0vLYTBkZGl2Uuzzh1k+pVdMDXZGSwjRreTm6cye1eHYnpZJJZdYvuljZlqNuBjJ3RNfXisOkeAGM3DVpDS3XQ7e3mkRH5WdSY4hbNRz1QuAIBI1Ou37dOarEWEysc1Z3GjMcFuW4xpe87ZZhIxxI7Dp6pb9pKejdIQ6vEZXmxtuOjmc4yxwk12sBdIQNNzt20aHRdWR+Xm/c175olaFlcONivRV9tuQvk4kjm6vMjmRE+oxzz2kDtK7lw9lM3RvsIiKOhERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAUZfwuOyNvG3LIlM2PkEtbZK9jQ4OD/AFmjkewKTREmInkRERRERAREQFhZRAREQf/Z', width = 600)



st.subheader('Please Fill in the fields below')
st.write('''Please input as 0 if you dont have any value''')




CreditScore = st.number_input('Credit Score')
FirstTimeHomebuyer = st.selectbox('First Time Homebuyer [0 : No, 1 : Yes]',[0,1])
MSA = st.number_input('MSA')
MIP = st.number_input('MIP')
Units = st.number_input('Units')
Occupancy = st.selectbox('Occupancy [O: 1, S: 2, I: 3]', [1,2,3])
OCLTV = st.number_input('OCLTV')
DTI = st.number_input('DTI')
OrigUPB = st.number_input('Original UPB')
LTV = st.number_input('LTV')
OrigInterestRate = st.number_input('OrigInterest Rate')
Channel = st.selectbox('Channel [T: 1, R: 2, C:3, B:4]', [1,2,3,4])
PropertyType = st.selectbox('Property Type [SF: 1, PU: 2, CO:3, CP:4, MH:5, LH:6]', [1,2,3,4,5,6])
LoanPurpose = st.selectbox('Loan Purpose [P: 1, N: 2, C:3]', [1,2,3])
OrigLoanTerm = st.number_input('Orig LoanTerm')
NumBorrowers = st.number_input('Number of Borrowers')
MonthsInRepayment = st.number_input('Months In Repayment')






input_parameters = {'CreditScore' : CreditScore,'FirstTimeHomebuyer' : FirstTimeHomebuyer, 'MSA' : MSA, 'MIP' : MIP, 'Units' : Units, 'Occupancy' : Occupancy, 'OCLTV' : OCLTV, 'DTI' : DTI, 'OrigUPB' : OrigUPB,  'LTV' : LTV, 'OrigInterestRate' : OrigInterestRate, 'Channel' : Channel, 'PropertyType' : PropertyType, 'LoanPurpose' : LoanPurpose, 'OrigLoanTerm' : OrigLoanTerm, 'NumBorrowers' : NumBorrowers, 'MonthsInRepayment' : MonthsInRepayment}
user_input = pd.DataFrame(input_parameters, index = [0])


st.subheader('Given Input parameters')
st.write(user_input)


# bins = [-1, 0, 20, 32, 52]
# groups = ['NO MIP', 'Low', 'Med', ' High']
# user_input['MIPEdit'] = pd.cut(user_input['MIP'], bins=bins, labels=groups)

# bins = [-1, 32, 60, 89, 110]
# groups = ['Low', 'Med', 'good', ' High']
# user_input['OCLTVEdit'] = pd.cut(user_input['OCLTV'], bins=bins, labels=groups)

bins = [-1,0, 650, 700, 750, 850]
groups = ['poor', 'fair', 'good', ' very good', 'excellent']
user_input['CS_Range'] = pd.cut(user_input['CreditScore'], bins=bins, labels=groups)

bins = [-1, 50, 80, 100]
groups = ['Low', 'Medium',' High']
user_input['LTV_range'] = pd.cut(user_input['LTV'], bins=bins, labels=groups)

bins = [0, 48, 96, 144, 192, 240]
groups = ['0-4years', '4-8years', '8-12years', ' 12-16years', 'more than 16years']
user_input['Repay_range'] = pd.cut(user_input['MonthsInRepayment'], bins=bins, labels=groups)




cleanup_nums = {
                "CS_Range": {"poor":1,"fair":2,"good":3," very good":4,"excellent":5},
                "LTV_range": {"Low":1,"Medium":2," High":3},
                "Repay_range": { "0-4years":1,"4-8years":2,"8-12years":3," 12-16years":4,"more than 16years":5}
                }

user_input = user_input.replace(cleanup_nums)
#user_input = user_input.drop('CreditScore', axis = 1)


st.subheader('Input parameters for predicting')
st.write(user_input)


rfc = pickle.load((open('model.pkl', 'rb')))


if st.button('Predict'):
    prediction = rfc.predict(user_input)
    #prediction_proba = rfc.predict_proba(user_input)
    if prediction == 1:
        st.write("This Loan is Delinquent")
        #st.write('probability : ', prediction_proba[0,1])
    else:
        st.write("This Loan is Not Delinquent")
        #st.write('probability : ', prediction_proba[0,0])