# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 01:03:46 2019

@author: yllzxzyq
"""

# TODO: Add import statements
import pandas as pd
from sklearn.linear_model import LinearRegression

# Assign the dataframe to this variable.
# TODO: Load the data
bmi_life_data = pd.read_csv('bmi_and_life_expectancy.csv')

# Make and fit the linear regression model
#TODO: Fit the model and Assign it to bmi_life_model
bmi_life_model = LinearRegression()

# Make a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931
bmi_life_model.fit(bmi_life_data[['BMI']] , bmi_life_data[['Life expectancy']])
laos_life_exp =bmi_life_model.predict(21.07931)