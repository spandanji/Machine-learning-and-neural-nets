import quandl, math, datetime 
#import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


forecast_col='Adj. Close'

def assignQuandlKey(key):
    #API KEY FOR QUANDL ACCOUNT.... CHANGE TO YOUR KEY
    quandl.ApiConfig.api_key = key

def retrieve(link):
    df = quandl.get(link)
    return df

def featureSelect(df):
    df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close'])/df['Adj. Close'] *100
    df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open'])/df['Adj. Open'] *100
    df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']] 
    return df

def labelGen(df,train_out=0.01):
    df.fillna(-99999,inplace=True)
    forecast_out = int(math.ceil(train_out*len(df)))
    df['label'] = df[forecast_col].shift(-forecast_out)
    print(forecast_out)
    return forecast_out,df

def matrixGen(df,forecast_out):
    X = np.array(df.drop(['label'],1))
    X = preprocessing.scale(X)
    X_lately = X[-forecast_out:]
    X = X[:-forecast_out]
    df.dropna(inplace=True)
    y = np.array(df['label'])
    y=np.array(df['label'])
    X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y, test_size=0.2)
    #print(accuracy*100)
    return X,y,X_train,y_train,X_test,y_test,X_lately

def trainAndTestLinear(X_train,y_train,X_test,y_test,X_lately):
    clf = LinearRegression(n_jobs=-1)
    clf.fit(X_train,y_train)
    accuracy = clf.score(X_test,y_test)
    forecast_set = clf.predict(X_lately)   
    return forecast_set,accuracy

def forecastAdd(df,forecast_set):
    df['Forecast']=np.nan
    prevDate=df.iloc[-1].name
    prevDateSec = prevDate.timestamp()
    one_day = 86400
    next_unix = prevDateSec + one_day
    for i in forecast_set:
        next_date = datetime.datetime.fromtimestamp(next_unix)
        next_unix = next_unix + one_day
        df.loc[next_date] = [np.nan for parse in range(len(df.columns)-1)] + [i]
    return df

def plotThem(df,forecast_out,accuracy):
    df['Adj. Close'].plot()
    df['Forecast'].plot()
    plt.legend(loc=4)
    plt.title(str(forecast_out)+ "days into the future..(Accuracy="+str(accuracy*100)+"%)")
    plt.xlabel('Date')
    plt.ylabel('Adjusted Close price')
    plt.show()


def main():
    quandlKey = 'KyDThnJDLaoE4Nk2xtoV'
    assignQuandlKey(quandlKey)
    df,outData= retrieve('WIKI/GOOGL'),0.01
    df = featureSelect(df)
    forecast_out,df = labelGen(df,train_out=outData)
    print(df.head())
    X,y,X_train,y_train,X_test,y_test,X_lately = matrixGen(df,forecast_out)
    forecast_set,accuracy = trainAndTestLinear(X_train,y_train,X_test,y_test,X_lately) 
    df = forecastAdd(df,forecast_set)
    plotThem(df,forecast_out,accuracy)
    # print(df.head())
    # print(df.tail())
   
if __name__ == '__main__' :
    main()