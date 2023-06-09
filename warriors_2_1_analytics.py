# -*- coding: utf-8 -*-
"""Warriors 2.1 Analytics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-VaESE6fhBt-iY0UmcjQyx70FQwTDsxD

```
# This is formatted as code
```
<h1>Implementation of Internet of Things in Developing Hybrid Energy Harvesting System </h1>
<h3><p>ADRIAN I. DELA CRUZ </p>
<p>JAMES FREDERIC B. DULO </p>
<p>GELAN M. NICOLAN </p>
<p>ARVENELL ABAD </p>
"""

# Commented out IPython magic to ensure Python compatibility.
#Importing libraries
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
df = pd.read_csv("Hybrid Panel testing.csv", index_col=0)
#Display the dataset
df

#Preprocessing
df = df.drop(['Average Solar\nVoltage\n(V)','Average Solar\nCurrent (A)','Average Piezo\nVoltage\n(V)','Average Piezo\nCurrent \n(A)', 'Average Piezo\nPower\n(W)'], axis=1)

df.describe()

#check for null values
df.isnull().sum()

#Get the correlation of the attributes
corr = df.corr()
corr

plt.scatter(df['Average\nHeat Index\n(°C)'], df['Average Solar\nPower\n(W)'], color='red')
plt.title(' Heat index Vs Solar Power', fontsize=14)
plt.xlabel('Solar Power', fontsize=14)
plt.ylabel('Heat index', fontsize=14)
plt.grid(True)
plt.show()

plt.scatter(df['Average\nHumidity\n(%)'], df['Average Solar\nPower\n(W)'], color='red')
plt.title(' Humidity Vs Solar Power', fontsize=14)
plt.xlabel('Solar Power', fontsize=14)
plt.ylabel('Humidity', fontsize=14)
plt.grid(True)
plt.show()

#Visualize Correlation
# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))
# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)
# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr,cmap=cmap, vmax=.9, square=True, linewidths=.5, ax=ax)

#Split the dataset to training and testing set
#Lets consider TV and radio to determine the advertising sales
df_train, df_test = train_test_split(df, test_size=0.25, random_state=35)

x_train = df_train[['Average\nHeat Index\n(°C)', 'Average\nHumidity\n(%)']]
y_train = df_train['Average Solar\nPower\n(W)']

x_test = df_test[['Average\nHeat Index\n(°C)', 'Average\nHumidity\n(%)']]
y_test = df_test['Average Solar\nPower\n(W)']

#Instantiate the Scaler
scaler = StandardScaler()
#Fit to the TRAIN set
scaler.fit(x_train)
#Apply to the TRAIN set
x_train_s = scaler.transform(x_train)
#Apply to the TEST set
x_test_s = scaler.transform(x_test)

x_train_s
df.head()

#Instantiate the Linear Regression Algorithm
linreg = linear_model.LinearRegression()
#Train the Model
linreg.fit(x_train_s, y_train)

#Verifying Coefficient
pd.DataFrame(linreg.coef_, index=x_train.columns, columns=['Coef'])

# Validate the Model
# Predict the values
y_pred = linreg.predict(x_test_s)
y_pred

#PERFORMANCE METRICS

df_results = pd.DataFrame(y_test)
df_results["Predicted Solar Power"] = y_pred
df_results

# Create a new dataframe containing the predictor variables, test results, and predicted results
results_df = pd.DataFrame({'Heat Index (°C)': x_test['Average\nHeat Index\n(°C)'],
                           'Humidity (%)': x_test['Average\nHumidity\n(%)'],
                           'Actual Solar Power (W)': y_test,
                           'Predicted Solar Power (W)': y_pred})
results_df

#Measure the performance of the model
r2 = r2_score(y_test, y_pred) * 100
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred) 
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(("r2: %.2f") %r2)
print(("mae: %.2f") %mae)
print(("mse: %.2f") %mse)
print(("rmse: %.2f") %rmse)

x_test.columns

#x_test.rename(columns={'Average\nHeat Index\n(°C)': 'Averageheatindex', 'Average\nHumidity\n(%)': 'Averagehumidity'})

#visualizing results
plt.scatter(y_test, y_pred, label='Predicted vs Actual')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', label='Ideal Predictions')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Linear Regression Results')
plt.legend(loc='lower right')
plt.show()

