#import the libraries
import stocks as st

quandlKey = 'KyDThnJDLaoE4Nk2xtoV'
st.assignQuandlKey(quandlKey)

df,pctDataOut= st.retrieve('WIKI/CCE'),0.005

#df,pctDataOut== st.retrieve('WIKI/TCS'),0.01
#df,pctDataOut== st.retrieve('WIKI/GOOGL'),0.01
#df,pctDataOut== st.retrieve('WIKI/MSFT'),0.01

df = st.featureSelect(df)
forecast_out,df = st.labelGen(df,train_out=pctDataOut)
print(df.head())

X,y,X_train,y_train,X_test,y_test,X_lately = st.matrixGen(df,forecast_out)
forecast_set,accuracy = st.trainAndTestLinear(X_train,y_train,X_test,y_test,X_lately) 

df = st.forecastAdd(df,forecast_set)
st.plotThem(df,forecast_out,accuracy)


'''
Control the plot

add at the top,

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.title(str(forecast_out)+ "days into the future..(Accuracy="+str(accuracy*100)+"%)")
plt.xlabel('Date')
plt.ylabel('Predict Close price')
plt.show()

'''
