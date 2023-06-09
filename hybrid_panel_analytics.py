# -*- coding: utf-8 -*-
"""Hybrid panel analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A1g0CoO1h8PchKa8c3_-0vAMG9j2cr2b
"""

# Commented out IPython magic to ensure Python compatibility.
#Inporting Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
sns.set_context("poster")
# %matplotlib inline

#Train-Test Split Module
from sklearn.model_selection import train_test_split
#Linear Regression Algorithm from sklearn
from sklearn import linear_model
#Metrics to measure model performance
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
#Standard Scaler for Standardization
from sklearn.preprocessing import StandardScaler
#warnings
import warnings
warnings.filterwarnings('ignore')

#Load the dataset
df1 = pd.read_csv("Day1_Testing.csv", index_col=0)
#Display the dataset
df1

#Load the dataset
df2 = pd.read_csv("Day2_Testing.csv", index_col=0)
#Display the dataset
df2

#Merging datasets for solar testing only
dfsolar = pd.merge(df1, df2)
dfsolar.dtypes

dfsolar

#Load the dataset
df3 = pd.read_csv("Day3_Testing.csv", index_col=0)
#Display the dataset
df3

#Load the dataset
df4 = pd.read_csv("Day4_Testing.csv", index_col=0)
#Display the dataset
df4

#Load the dataset
df5 = pd.read_csv("Day5_Testing.csv", index_col=0)
#Display the dataset
df5

#Merging datasets for hybrid testing
df6 = pd.merge(df3,df4)
dfhybrid = pd.merge(df6,df5)
dfhybrid.dtypes

dfhybrid

#Data preprocessing
dfsolar1 = dfsolar.drop(['Device ID','Channel','Sensor ID','Data Type','Unit'], axis=1)

#Check for remaining values
dfsolar1



#Data preprocessing
dfhybrid1 = dfhybrid.drop(['Device ID','Channel','Sensor ID','Data Type','Unit'], axis=1)

#Check for remaining values
dfhybrid1

