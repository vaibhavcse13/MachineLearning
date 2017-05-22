# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 15:10:13 2016

@author: vaibhav
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Build_Data_Set():
    data = pd.read_excel("G:/Gzb/Ugzb.xlsx")
    feat = ['Year', 'Wdf' , 'T','Cloud']
    x = data[feat]
 
    tar = np.array(data['Jun-Sep'])
    y = pd.Series(tar)
    return x,y

def Analysis():
    x,y = Build_Data_Set()
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=1)
    from sklearn.linear_model import LinearRegression

    lreg = LinearRegression()
    lreg.fit(x_train, y_train )
    ypred = lreg.predict(x_test)
    print(lreg.intercept_)
    print(lreg.coef_)
    from sklearn.metrics import r2_score
    print(r2_score(y_test, ypred))
    from sklearn import metrics
    print(metrics.mean_absolute_error(y_test , ypred))
    print(metrics.mean_squared_error(y_test , ypred))
    print(np.sqrt(metrics.mean_squared_error(y_test , ypred)))

    
Analysis()