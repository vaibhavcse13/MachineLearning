import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymysql as  db
import pandas.io.sql as psql
con = db.connect('localhost','root' ,'vaibhav','NewSave')

def Build_Data_Set(state):
    sql = "SELECT * FROM %s "%state
    data = psql.read_sql(sql, con )
    feat = ['Year', 'Ann_Wdf' , 'Ann_Mtemp','Ann_Cloud']
    x = data[feat]
 
    tar = np.array(data['Annual_Rain'])
    y = pd.Series(tar)
    return x,y

def Analysis():
    x,y = Build_Data_Set("Delhi")
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=1)
    from sklearn.linear_model import LinearRegression

    lreg = LinearRegression()
    z = lreg.fit(x_train, y_train )
    ypred = z.predict(x_test)
    #print(z.intercept_)
    #print(z.coef_)
    from sklearn.metrics import r2_score
    #print(r2_score(y_test, ypred))
    #from sklearn import metrics
    #print(metrics.mean_absolute_error(y_test , ypred))
    #print(metrics.mean_squared_error(y_test , ypred))
    #print(np.sqrt(metrics.mean_squared_error(y_test , ypred)))
    return z


def Build_Cloud(yr):
    sql = "SELECT Ann_Cloud ,Year FROM Chennai "
    #data = psql.read_sql(sql, con )
    cloud_data = psql.read_sql(sql, con )
    x = cloud_data[['Year']]
    y = cloud_data[['Ann_Cloud']]
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=1)
    from sklearn.linear_model import LinearRegression
    cldreg = LinearRegression()
    cldreg.fit(x_train, y_train )
    ypred = cldreg.predict(x_test)
    #print(cldreg.intercept_)
    #print(cldreg.coef_)
    from sklearn.metrics import r2_score
    #print(r2_score(y_test, ypred))
    from sklearn import metrics
    #print(metrics.mean_absolute_error(y_test , ypred))
    #print(metrics.mean_squared_error(y_test , ypred))
    #print(np.sqrt(metrics.mean_squared_error(y_test , ypred)))
    c = cldreg.predict(yr)
    return c
    
    
def Temp_Analysis(yr):
    sql = "SELECT Ann_Mtemp ,Year FROM Delhi "
    #data = psql.read_sql(sql, con )
    cloud_data = psql.read_sql(sql, con )
    x = cloud_data[['Year']]
    y = cloud_data[['Ann_Mtemp']]
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=11)
    from sklearn.linear_model import LinearRegression
    treg = LinearRegression()
    treg.fit(x_train, y_train )
    ypred = treg.predict(x_test)
    #print(treg.intercept_)
    #print(treg.coef_)
    from sklearn.metrics import r2_score
    #print(r2_score(y_test, ypred))
    from sklearn import metrics
    #print(metrics.mean_absolute_error(y_test , ypred))
    #print(metrics.mean_squared_error(y_test , ypred))
    #print(np.sqrt(metrics.mean_squared_error(y_test , ypred)))
    #yr = float(input("Enter year"))
    t = treg.predict(yr)
    
    return t
    
def Wet_Day_Analysis(yr):
    sql = "SELECT Ann_Wdf ,Year FROM Delhi "
    #data = psql.read_sql(sql, con )
    cloud_data = psql.read_sql(sql, con )
    x = cloud_data[['Year']]
    y = cloud_data[['Ann_Wdf']]
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=10)
    from sklearn.linear_model import LinearRegression
    wdfreg = LinearRegression()
    wdfreg.fit(x_train, y_train )
    ypred = wdfreg.predict(x_test)
    #print(wdfreg.intercept_)
    #print(wdfreg.coef_)
    from sklearn.metrics import r2_score
    #print(r2_score(y_test, ypred))
    from sklearn import metrics
    #print(metrics.mean_absolute_error(y_test , ypred))
    #print(metrics.mean_squared_error(y_test , ypred))
    #print(np.sqrt(metrics.mean_squared_error(y_test , ypred)))
    #yr = float(input("Enter year"))
    t = wdfreg.predict(yr)
    return t 

def Prediction(year):
    z = Analysis()
    #print(z.coef_)
    #print(z.intercept_)
    p = Build_Cloud(year)
    q = Wet_Day_Analysis(year)
    r = Temp_Analysis(year)
    
    
    x = np.array([year , q,  r, p])
    t = x.reshape(1,-1)
    y = z.predict(t)
    print(y)
#to test this script remove the comment and enter the year 
#Prediction(*Enter Year*)
