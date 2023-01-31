## Mortgage-Backed-Securities-Prepayment-Risk-Predictor
Prepayment is a risk for mortgage lenders and mortgage-backed securities (MBS) investors that people will pay their loans off earlier than the full term. This prevents them from getting interest payments for the long amount of time as they'd counted on.

## Aim of the this Project 
to Predict the MBS Prepayment risk using Machine Learning models.

## About Dataset : 
The data is obtained from Freddie Mac official portal for home loans. The size of the home loans data is (291452 x 28). 
It contains 291452 data points and 28 columns or parameters which denote different features of the data. Some of the noteworthy features of the dataset are: 
#### Credit score of the client 
#### The maturity date of the mortgage
#### The amount or percentage of insurance on the mortgage
#### Debt to income ration of the borrower 
#### Mortgage interest rate 
#### Prepayment Penalty Mortgage - denotes if there is any penalty levied on prepayment of loan
#### Loan sequence number — denotes the unique loan ID 
#### The purpose of the loan
#### The number of borrowers issued on the loan.
#### The property type, the state in which property is and its postal code and address
#### The information about the seller and service company.
#### HARP indicator denotes if the loan is HARP or non-HARP
#### Interest only indicator — Denotes if the loan requires only the interest payments over the period of maturity or not. 
and other variables described on the pdf file for more information.

## EDA : Exploratory Data Analysis
it is the first step to be performed in this project and it involves : 
Data Cleaning: 
handling missing values : 
<img width="210" alt="image" src="https://user-images.githubusercontent.com/79838714/215777501-85b930e1-74e4-440b-b659-e258d4ab0e98.png">

removing duplicates and outliers in some variables : 
<img width="264" alt="image" src="https://user-images.githubusercontent.com/79838714/215778221-11ad1d64-4d70-4c29-bb61-beb332992a8a.png">
<img width="268" alt="image" src="https://user-images.githubusercontent.com/79838714/215778296-d86847e3-5c5a-4fb8-906b-9dfbf74736ec.png">
<img width="262" alt="image" src="https://user-images.githubusercontent.com/79838714/215778385-b20b923b-851f-479f-ab0c-e94f09f80f9f.png">

## Univariate Analysis: 
Analyzing individual variables to gain insights into the data.
<img width="313" alt="image" src="https://user-images.githubusercontent.com/79838714/215777861-b2faf96d-17f9-490d-aac3-ce8aece54eb0.png">

## Creating New Columns from existing variables : 
CS_Range that contains the credit score range : poor , fair , good , very good or excellent
LTV_range = Low , Medium and High
Repay_range in years created from MonthsInRepayment
Plotting the Balance of the columns just created :
<img width="689" alt="image" src="https://user-images.githubusercontent.com/79838714/215780124-1a248825-6448-4235-be3c-08c4fb9e2b01.png">
<img width="689" alt="image" src="https://user-images.githubusercontent.com/79838714/215780375-c5eb608d-dd43-4519-8efe-002ad4ad14c1.png">

## Encoding Variables : 
<img width="701" alt="image" src="https://user-images.githubusercontent.com/79838714/215781473-f7635553-5871-48d8-b35e-e6771af45e46.png">

## Balancing Data ( target Variable ) 
Before the balance : 
<img width="182" alt="image" src="https://user-images.githubusercontent.com/79838714/215780797-a81956b7-15ee-43ce-92fa-6a94a3f0af6c.png">

After Balancing using SMOTE Technique :
<img width="185" alt="image" src="https://user-images.githubusercontent.com/79838714/215780951-06110c85-c98a-4ca2-9869-ed6343d1d674.png">

## Feature Engineering :
This step involves : feature extraction ( important feature ) and dimensionality reduction ( PCA ) 

Mitual Information as a feature selection technique to identify the most relevant features in a dataset for building predictive models.
<img width="398" alt="image" src="https://user-images.githubusercontent.com/79838714/215782236-dc7cbf7a-728f-4672-ac87-8358665e2a26.png">
 
 ## PCA (Principal Component Analysis) : 
 to identify the principal components that explain the most variance in the data.
 <img width="340" alt="image" src="https://user-images.githubusercontent.com/79838714/215782738-acdf4463-af48-43f1-a838-2d1a5102e292.png">
 
After performing PCA, the feature importances can be determined by examining the explained variance by each principal component. 
<img width="559" alt="image" src="https://user-images.githubusercontent.com/79838714/215783923-97cf223b-2197-4133-8c59-8cea9f086fa9.png">

The features that contribute the most to the principal components with the highest explained variance are considered the most important. 

## Building ML Models
LR : Logistic Regression : is a simple and interpretable model that is widely used in many fields , can be used to make binary predictions ( Delinquent or Not delinquent )
<img width="217" alt="image" src="https://user-images.githubusercontent.com/79838714/215785431-202b4011-b111-41e5-b038-cfc382ed62c8.png">

KNN : (K-Nearest Neighbors) , in a binary classification problem, if most of the K nearest neighbors belong to a particular class, the new data point is classified as belonging to that class.KNN can be slow for large datasets and can be sensitive to the choice of K and the distance metric used to measure similarity between data points. Actually K used in this project are : K=5 and K=30 but we only got 54% as accuracy.

We acheived best accuracy using LR model that is 69%. Therefore we have used this model for Deployment.


## Model Deployment 
We have used StreamLit Framework to create web app for our model:
we have created a python file as "deploy.py" in out deployment folder have loaded pickle file for LR model

## this is a preview of the web interface of our app : 
<img width="428" alt="image" src="https://user-images.githubusercontent.com/79838714/215788648-3c44487e-2717-4399-8dd3-dd3f61240285.png">
<img width="407" alt="image" src="https://user-images.githubusercontent.com/79838714/215788779-fac52d3d-76dc-4c93-9b12-3832eefd2be5.png">


## Conclusion 
Prepayment risk is the risk that borrowers will pay off their mortgages early, which can impact the cash flow and value of MBS investments. 
This model predict wheather the loan is delinquent or not , So the prepayment risk predictor can help investors make informed decisions about their investments, such as when to buy or sell MBS. Additionally, by providing banks with insight into prepayment risk, they can manage their portfolio of MBS investments more effectively, reducing their exposure to prepayment risk and ensuring that they are able to meet their financial obligations.
The predictor can also help banks and investors to price MBS accurately, taking into account the risk of prepayments, which can result in more efficient and effective investment strategies. Overall, a MBS prepayment risk predictor can help investors and banks to better manage their investments, reduce their exposure to risk, and make informed decisions about buying and selling MBS.
