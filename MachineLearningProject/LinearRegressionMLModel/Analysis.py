import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymysql as  db
import pandas.io.sql as psql
import seaborn as sns

con = db.connect('localhost','root' ,'vaibhav','NewSave')

def Build_Data_Set_DelhiAnn():
    sql = "SELECT * FROM Delhi "
    # Readind data in data frame
    data = psql.read_sql(sql, con )
    #data = pd.read_excel("G:/Gzb/Ugzb.xlsx")
    # creating feature 
    feat = ['Year', 'Ann_Wdf' , 'Ann_Mtemp','Ann_Cloud']
    x = data[feat]
    # Creating Response variable 
    res = np.array(data['Annual_Rain'])
    y = pd.Series(res)
    return x,y

def AnnAnalysisDelhi():
    print("------------------Annual Rainfall Analysis for Delhi-------------- ")
    x,y = Build_Data_Set_DelhiAnn()
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=14)
    from sklearn.linear_model import LinearRegression

    lreg = LinearRegression()
    lreg.fit(x_train, y_train )
    ypred = lreg.predict(x_test)
    print("Intercept of regression line is",lreg.intercept_)
    print("Coefficent of regression line " , lreg.coef_)
    from sklearn.metrics import r2_score
    from sklearn import metrics
    print("The R2 Score  is : " , (r2_score(y_test, ypred)))
    print("The mean absolute error is: " , (metrics.mean_absolute_error(y_test , ypred)))
    print("The mean squared error is: " , (metrics.mean_squared_error(y_test , ypred)))
    print("The root mean squared error is: " ,(np.sqrt(metrics.mean_squared_error(y_test , ypred))))
    print("The median absolute error is:  ",(metrics.median_absolute_error(y_test, ypred)))
    
def Build_Data_Set_DelhiMOn():
    sql = "SELECT * FROM Delhi "
    data = psql.read_sql(sql, con )
    #data = pd.read_excel("G:/Gzb/Ugzb.xlsx")
    feat = ['Year', 'Jun_Sep_Wdf' , 'Jun_Sep_Mtemp','Jun_Sep_Cloud']
    x = data[feat]
 
    tar = np.array(data['Jun_Sep_Rain'])
    y = pd.Series(tar)
    return x,y

def MonAnalysisDelhi():
    print("---------------Monsoon Rainfall analysis od Delhi----------------")
    x,y = Build_Data_Set_DelhiMOn()
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=1)
    from sklearn.linear_model import LinearRegression

    lreg = LinearRegression()
    lreg.fit(x_train, y_train )
    ypred = lreg.predict(x_test)
    print("Intercept of regression line is",lreg.intercept_)
    print("Coefficent of regression line " , lreg.coef_)
    from sklearn.metrics import r2_score
    from sklearn import metrics
    print("The R2 Score  is : " , (r2_score(y_test, ypred)))
    print("The mean absolute error is: " , (metrics.mean_absolute_error(y_test , ypred)))
    print("The mean squared error is: " , (metrics.mean_squared_error(y_test , ypred)))
    print("The root mean squared error is: " ,(np.sqrt(metrics.mean_squared_error(y_test , ypred))))
    print("The median absolute error is:  ",(metrics.median_absolute_error(y_test, ypred)))
    
def Build_Data_Set_GzbAnn():
    
    sql = "SELECT * FROM Ghaziabad "
    data = psql.read_sql(sql, con )
    feat = ['Year', 'Ann_Wdf' , 'Ann_Mtemp','Ann_Cloud']
    x = data[feat]
 
    tar = np.array(data['Annual_Rain'])
    
    y = pd.Series(tar)
    
    return x,y

def AnnAnalysisGzb():
    print("--------------------Annual Rainfall Analysis of Ghaziabad-------------- ")
    x,y = Build_Data_Set_GzbAnn()
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=47)
    from sklearn.linear_model import LinearRegression

    lreg = LinearRegression()
    lreg.fit(x_train, y_train )
    ypred = lreg.predict(x_test)
    print("Intercept of regression line is",lreg.intercept_)
    print("Coefficent of regression line " , lreg.coef_)
    from sklearn.metrics import r2_score
    from sklearn import metrics
    print("The R2 Score  is : " , (r2_score(y_test, ypred)))
    print("The mean absolute error is: " , (metrics.mean_absolute_error(y_test , ypred)))
    print("The mean squared error is: " , (metrics.mean_squared_error(y_test , ypred)))
    print("The root mean squared error is: " ,(np.sqrt(metrics.mean_squared_error(y_test , ypred))))
    print("The median absolute error is:  ",(metrics.median_absolute_error(y_test, ypred)))

def Build_Data_Set_GzbMon():
    sql = "SELECT * FROM Ghaziabad "
    data = psql.read_sql(sql, con )
    #data = pd.read_excel("G:/Gzb/Ugzb.xlsx")
    feat = ['Year', 'Jun_Sep_Wdf' , 'Jun_Sep_Mtemp','Jun_Sep_Cloud']
    x = data[feat]
 
    tar = np.array(data['Jun_Sep_Rain'])
    y = pd.Series(tar)
    return x,y

def MonAnalysisGzb():
    print("--------------------Monsoon Rainfall Analysis of Ghaziabad-----------")
    x,y = Build_Data_Set_GzbMon()
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=1)
    from sklearn.linear_model import LinearRegression

    lreg = LinearRegression()
    lreg.fit(x_train, y_train )
    ypred = lreg.predict(x_test)
    print("Intercept of regression line is",lreg.intercept_)
    print("Coefficent of regression line " , lreg.coef_)
    from sklearn.metrics import r2_score
    from sklearn import metrics
    print("The R2 Score  is : " , (r2_score(y_test, ypred)))
    print("The mean absolute error is: " , (metrics.mean_absolute_error(y_test , ypred)))
    print("The mean squared error is: " , (metrics.mean_squared_error(y_test , ypred)))
    print("The root mean squared error is: " ,(np.sqrt(metrics.mean_squared_error(y_test , ypred))))
    print("The median absolute error is:  ",(metrics.median_absolute_error(y_test, ypred)))
def Build_Data_Set_KolMon():
    sql = "SELECT * FROM Kolkatta "
    data = psql.read_sql(sql, con )
    #data = pd.read_excel("G:/Gzb/Ugzb.xlsx")
    feat = ['Year', 'Jun_Sep_Wdf' , 'Jun_Sep_Mtemp','Jun_Sep_Cloud']
    x = data[feat]
 
    tar = np.array(data['Jun_Sep_Rain'])
    y = pd.Series(tar)
    return x,y

def MonAnalysisKol():
    print("---------------Monsoon Rainfall analysis of Kolkata----------------")
    x,y = Build_Data_Set_KolMon()
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=6)
    from sklearn.linear_model import LinearRegression

    lreg = LinearRegression()
    lreg.fit(x_train, y_train )
    ypred = lreg.predict(x_test)
    print("Intercept of regression line is",lreg.intercept_)
    print("Coefficent of regression line " , lreg.coef_)
    from sklearn.metrics import r2_score
    #print(r2_score(y_test, ypred))
    from sklearn import metrics
    print("The R2 Score  is : " , (r2_score(y_test, ypred)))
    print("The mean absolute error is: " , (metrics.mean_absolute_error(y_test , ypred)))
    print("The mean squared error is: " , (metrics.mean_squared_error(y_test , ypred)))
    print("The root mean squared error is: " ,(np.sqrt(metrics.mean_squared_error(y_test , ypred))))
    print("The median absolute error is:  ",(metrics.median_absolute_error(y_test, ypred)))
def Build_Data_SetKolAnn():
    sql = "SELECT * FROM Kolkatta "
    data = psql.read_sql(sql, con )
    #data = pd.read_excel("G:/Gzb/Ugzb.xlsx")
    feat = ['Year', 'Ann_Wdf' , 'Ann_Mtemp','Ann_Cloud']
    x = data[feat]
 
    tar = np.array(data['Annual_Rain'])
    y = pd.Series(tar)
    return x,y

def AnnAnalysisKol():
    print("------------Annual Rainfall analysis of Kolkata------------------------ ")
    x,y = Build_Data_SetKolAnn()
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=1)
    from sklearn.linear_model import LinearRegression

    lreg = LinearRegression()
    lreg.fit(x_train, y_train )
    ypred = lreg.predict(x_test)
    print("Intercept of regression line is",lreg.intercept_)
    print("Coefficent of regression line " , lreg.coef_)
    from sklearn.metrics import r2_score
    #print(r2_score(y_test, ypred))
    from sklearn import metrics
    print("The R2 Score  is : " , (r2_score(y_test, ypred)))
    print("The mean absolute error is: " , (metrics.mean_absolute_error(y_test , ypred)))
    print("The mean squared error is: " , (metrics.mean_squared_error(y_test , ypred)))
    print("The root mean squared error is: " ,(np.sqrt(metrics.mean_squared_error(y_test , ypred))))
    print("The median absolute error is:  ",(metrics.median_absolute_error(y_test, ypred)))
def Build_Data_SetAnnMas():
    sql = "SELECT * FROM Chennai "
    data = psql.read_sql(sql, con )
    #data = pd.read_excel("G:/Gzb/Ugzb.xlsx")
    feat = ['Year', 'Ann_Wdf' , 'Ann_Mtemp','Ann_Cloud']
    x = data[feat]
 
    tar = np.array(data['Annual_Rain'])
    y = pd.Series(tar)
    return x,y

def AnnAnalysisMas():
    print("------------------Annual Rainfall Analysis of Chennai-----------------")
    x,y = Build_Data_SetAnnMas()
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=4)
    from sklearn.linear_model import LinearRegression

    lreg = LinearRegression()
    lreg.fit(x_train, y_train )
    ypred = lreg.predict(x_test)
    print("Intercept of regression line is",lreg.intercept_)
    print("Coefficent of regression line " , lreg.coef_)
    from sklearn.metrics import r2_score
    print(r2_score(y_test, ypred))
    from sklearn import metrics
    print("The R2 Score  is : " , (r2_score(y_test, ypred)))
    print("The mean absolute error is: " , (metrics.mean_absolute_error(y_test , ypred)))
    print("The mean squared error is: " , (metrics.mean_squared_error(y_test , ypred)))
    print("The root mean squared error is: " ,(np.sqrt(metrics.mean_squared_error(y_test , ypred))))
    print("The median absolute error is:  ",(metrics.median_absolute_error(y_test, ypred)))
def Build_Data_SetMonMas():
    sql = "SELECT * FROM Chennai"
    data = psql.read_sql(sql, con )
    #data = pd.read_excel("G:/Gzb/Ugzb.xlsx")
    feat = ['Year', 'Jun_Sep_Wdf' , 'Jun_Sep_Mtemp','Jun_Sep_Cloud']
    x = data[feat]
 
    tar = np.array(data['Jun_Sep_Rain'])
    y = pd.Series(tar)
    return x,y

def MonAnalysisMas():
    print("------------------Monsoon Rainfall Analysis of Chennai------------------")
    x,y = Build_Data_SetMonMas()
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=11)
    from sklearn.linear_model import LinearRegression

    lreg = LinearRegression()
    lreg.fit(x_train, y_train )
    ypred = lreg.predict(x_test)
    print("Intercept of regression line is",lreg.intercept_)
    print("Coefficent of regression line " , lreg.coef_)
    from sklearn.metrics import r2_score
    from sklearn import metrics
    print("The R2 Score  is : " , (r2_score(y_test, ypred)))
    print("The mean absolute error is: " , (metrics.mean_absolute_error(y_test , ypred)))
    print("The mean squared error is: " , (metrics.mean_squared_error(y_test , ypred)))
    print("The root mean squared error is: " ,(np.sqrt(metrics.mean_squared_error(y_test , ypred))))
    print("The median absolute error is:  ",(metrics.median_absolute_error(y_test, ypred)))
def Build_Data_SetAnnAld():
    sql = "SELECT * FROM Allahabad "
    data = psql.read_sql(sql, con )
    #data = pd.read_excel("G:/Gzb/Ugzb.xlsx")
    feat = ['Year', 'Ann_Wdf' , 'Ann_Mtemp','Ann_Cloud']
    x = data[feat]
 
    tar = np.array(data['Annual_Rain'])
    y = pd.Series(tar)
    return x,y

def AnnAnalysisAld():
    print("-----------------Annual Ranfall Analysis of Allahabad-----------------")
    x,y = Build_Data_SetAnnAld()
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=1)
    from sklearn.linear_model import LinearRegression

    lreg = LinearRegression()
    lreg.fit(x_train, y_train )
    ypred = lreg.predict(x_test)
    print("Intercept of regression line is",lreg.intercept_)
    print("Coefficent of regression line " , lreg.coef_)
    from sklearn.metrics import r2_score
    from sklearn import metrics
    print("The R2 Score  is : " , (r2_score(y_test, ypred)))
    print("The mean absolute error is: " , (metrics.mean_absolute_error(y_test , ypred)))
    print("The mean squared error is: " , (metrics.mean_squared_error(y_test , ypred)))
    print("The root mean squared error is: " ,(np.sqrt(metrics.mean_squared_error(y_test , ypred))))
    print("The median absolute error is:  ",(metrics.median_absolute_error(y_test, ypred)))
def Build_Data_SetMonAld():
    sql = "SELECT * FROM Allahabad"
    data = psql.read_sql(sql, con )
    #data = pd.read_excel("G:/Gzb/Ugzb.xlsx")
    feat = ['Year', 'Jun_Sep_Wdf' , 'Jun_Sep_Mtemp','Jun_Sep_Cloud']
    x = data[feat]
 
    tar = np.array(data['Jun_Sep_Rain'])
    y = pd.Series(tar)
    return x,y

def MonAnalysisAld():
    print("--------------Monsoon Rainfall Analysis Of Allahabad------------------")
    x,y = Build_Data_SetMonAld()
    from sklearn.cross_validation import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x ,y ,test_size=20, random_state=1)
    from sklearn.linear_model import LinearRegression

    lreg = LinearRegression()
    lreg.fit(x_train, y_train )
    ypred = lreg.predict(x_test)
    print("Intercept of regression line is",lreg.intercept_)
    print("Coefficent of regression line " , lreg.coef_)
    from sklearn.metrics import r2_score
    #print(r2_score(y_test, ypred))
    from sklearn import metrics
    print("The R2 Score  is : " , (r2_score(y_test, ypred)))
    print("The mean absolute error is: " , (metrics.mean_absolute_error(y_test , ypred)))
    print("The mean squared error is: " , (metrics.mean_squared_error(y_test , ypred)))
    print("The root mean squared error is: " ,(np.sqrt(metrics.mean_squared_error(y_test , ypred))))
    print("The median absolute error is:  ",(metrics.median_absolute_error(y_test, ypred)))
AnnAnalysisDelhi()
MonAnalysisDelhi()
AnnAnalysisGzb()
MonAnalysisGzb()
MonAnalysisKol()
AnnAnalysisKol()
AnnAnalysisMas()
MonAnalysisMas()
AnnAnalysisAld()
MonAnalysisAld()