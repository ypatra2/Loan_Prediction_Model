from turtle import color

from pkg_resources import declare_namespace
import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("/Users/u.v._ray/Downloads/Training Dataset.csv")
male = len(df["Gender"].apply(lambda x: x == "Male"))
print(male)
female = len(df["Gender"].apply(lambda x: x == "Female"))
print(female)

# sizes = [male, female]

# fig1, ax1 = plt.subplots()
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


# A = ax1.pie(sizes)
# st.pyplot(A)

# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Male', 'Female'
# sizes = [male, female]
# explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

col1, col2 = st.columns(2)

Income = df["ApplicantIncome"]
LoanAmt = df["LoanAmount"]

fig, ax = plt.subplots()
ax.hist(Income, bins=50,color= "cyan", ec = "black")
ax.set_xlabel('Bins', fontsize=10)
ax.set_ylabel('Values', fontsize=10)
ax.set_title('Applicant Income Histogram', fontsize=12)

fig2, ax = plt.subplots()
ax.hist(LoanAmt, bins=50, color="cyan", ec = "black")
ax.set_xlabel('Bins', fontsize=10)
ax.set_ylabel('Values', fontsize=10)
ax.set_title("Loan Amount Histogram")

fig3, ax = plt.subplots()
ax.scatter(Income, LoanAmt, color = "royalblue")
ax.set_xlabel('Income', fontsize=10)
ax.set_ylabel('Loan Amount', fontsize=10)
ax.set_title("Income and Loan Amount Scatterplot")

le=LabelEncoder()
df['Education']=le.fit_transform(df['Education'])
df['Dependents']=le.fit_transform(df['Dependents'])
df['Self_Employed']=le.fit_transform(df['Self_Employed'])
df['Gender']=le.fit_transform(df['Gender'])
df['Married']=le.fit_transform(df['Married'])
df['Property_Area']=le.fit_transform(df['Property_Area'])
df['Loan_Status']=le.fit_transform(df['Loan_Status'])
temp = df.iloc[:, 1:]
fig4 = plt.figure(figsize=(10, 4))
sns.heatmap(temp.corr(),cmap="Blues", fmt='.2f', linewidths = 2, annot=True)

dict = {'Loan Amount Histogram': fig2, 'Applicant Income Histogram': fig, 'Income v/s Loan Scatterplot': fig3, 'Heatmap of Dataset': fig4}

option = st.selectbox(
    'What plot would you like to make',
    ('Loan Amount Histogram', 'Applicant Income Histogram', 'Income v/s Loan Scatterplot', 'Heatmap of Dataset'))
    
st.pyplot(dict[option])

st.button("Re-run")