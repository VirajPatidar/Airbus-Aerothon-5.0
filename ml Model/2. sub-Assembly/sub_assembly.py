# -*- coding: utf-8 -*-
"""Sub-assembly.ipynb


First, we will load the data into a pandas dataframe
"""

import pandas as pd

data = pd.read_csv('Washing_machine_manufacturing_company - sub-assembly.csv (1)')

"""we need to preprocess the data. We will convert the start date and end date columns to datetime format and create a new column 'duration' to store the time required for each process"""

data['start date'] = pd.to_datetime(data['start date'], errors='coerce', format='%m/%d/%Y')
data['end date'] = pd.to_datetime(data['end date'], errors='coerce', format='%m/%d/%Y')
data['duration'] = (pd.to_datetime(data['end date']) - pd.to_datetime(data['start date'])).dt.days

"""Now, we can select the features and target variable for our prediction model"""

X = data[['process']]
y = data['duration']
unique_categories = data['process'].unique()
data.dropna(subset=['end date'], inplace=True)

"""We need to convert categorical features into numerical features using one-hot encoding"""

X = pd.get_dummies(X)

"""We will split the dataset into training and testing sets"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""Next, we will use linear regression to train our model"""

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

"""we can use decision tree based regression also to train the data"""

from sklearn.tree import DecisionTreeRegressor

dt = DecisionTreeRegressor(random_state=42)
dt.fit(X, y)

y_pred = lr.predict(X_test)

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
print('Mean squared error:', mse)

"""We can also visualize the predictions using a scatter plot"""

import matplotlib.pyplot as plt

plt.scatter(y_test, y_pred)
plt.xlabel('Actual duration')
plt.ylabel('Predicted duration')
plt.show()

"""To use decision tree algorithm, we will follow the same process as linear regression and replace it with decision tree algorithm"""

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

"""categories the process & map it"""

new_process = pd.DataFrame(columns=unique_categories)

new_process.loc[0, 'Transmission Assembly'] = 1

new_process = new_process.fillna(0)

"""Predict the duration for the process based on the trained model """

new_process = pd.DataFrame({
    'process_Transmission Assembly': 1,
    'Electrical Assembly': 0,
    'Mechanical assembly': 0,
    'Weld Assembly.': 0,
    'Spot Weld Assembly': 0,
    'Tub assemblies': 0
}, index=[0])

new_process = pd.get_dummies(new_process, prefix='process')

predicted_duration = dt.predict(new_process)[1]
print('Predicted duration:', predicted_duration)

