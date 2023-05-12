# -*- coding: utf-8 -*-
"""Assembly.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yLUqRELW6pO9tSrHVtaAM9MBDtPrmLHP
"""

import pandas as pd

data = pd.read_csv('Washing_machine_manufacturing_company-Assembly - Sheet2.csv')

data['Start Date '] = pd.to_datetime(data['Start Date '], errors='coerce', format='%m/%d/%Y')
data['END DATE'] = pd.to_datetime(data['END DATE'], errors='coerce', format='%m/%d/%Y')
data['duration'] = (pd.to_datetime(data['END DATE']) - pd.to_datetime(data['Start Date '])).dt.days

# split the dataset into training and testing sets
X = data[['process']]
y = data['duration']
unique_categories = data['process'].unique()
data.dropna(subset=['END DATE'], inplace=True)

X = pd.get_dummies(X)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor(random_state=42)
dt.fit(X, y)

y_pred = lr.predict(X_test)

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
print('Mean squared error:', mse)

import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel('Actual duration')
plt.ylabel('Predicted duration')
plt.show()

from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)

y_pred = dt.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print('Mean squared error:', mse)

plt.scatter(y_test, y_pred)
plt.xlabel('Actual duration')
plt.ylabel('Predicted duration')
plt.show()

new_process = pd.DataFrame(columns=unique_categories)

new_process.loc[0, 'Transmission Assembly'] = 1
new_process = new_process.fillna(0)