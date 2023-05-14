# -*- coding: utf-8 -*-
"""Fabrication.ipynb

we will import the necessary libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

"""Next, we will load the data into a pandas dataframe

"""

data = pd.read_csv('Washing_machine_manufacturing_company - fabrication (1).csv')

"""We will then convert the date columns to datetime objects"""

data['in date'] = pd.to_datetime(data['in date'])
data['out date'] = pd.to_datetime(data['out date'])

"""Next, we will group the data by raw material and calculate the weekly quantity

"""

data = data.groupby(['raw material', pd.Grouper(key='in date', freq='W-MON')])['Quantity'].sum().reset_index().sort_values('in date')

"""We will then pivot the data so that each raw material has its own column"""

data = data.pivot(index='in date', columns='raw material', values='Quantity')

"""We will fill any missing values with 0"""

data = data.fillna(0)

"""Next, we will split the data into training and testing sets"""

train = data.iloc[:-4]
test = data.iloc[-4:]

"""convert the columns to numeric """

train = train.apply(pd.to_numeric)

"""to fix issue related to out of bound index in data

"""

train = train.reset_index(drop=True)

"""ARIMA model requires univariate data, so we train model on the actual data 

"""

for col in train.columns:
    model = ARIMA(train[col], order=(1, 1, 1))
    model_fit = model.fit()
    predictions = model_fit.forecast(steps=4)[1]
    plt.plot(test.index, test[col], label='Actual')
    predictions_series = pd.Series(predictions, index=pd.date_range(start=test.index[0], periods=4, freq='D'))
    plt.plot(predictions_series.index, predictions_series, label='Predicted')
    plt.title(col)
    plt.legend()
    plt.show()