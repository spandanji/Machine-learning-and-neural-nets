#!/usr/bin/python3
import stocks as st

# quandlKey = 'KyDThnJDLaoE4Nk2xtoV'
# st.assignQuandlKey(quandlKey)
#So Simple...

df, pctDataOut = st.retrieve('WIKI/TCS'), 0.05
df = st.featureSelect(df)
forecast_out, df = st.labelGen( df, train_out=pctDataOut)
X,y,X_train,y_train,X_test,y_test,X_lately = st.matrixGen(df,forecast_out)
forecast_set,accuracy = st.trainAndTestLinear(X_train,y_train,X_test,y_test,X_lately) 
df = st.forecastAdd(df,forecast_set)

st.plotThem(df,forecast_out,accuracy)