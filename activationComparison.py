import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
  



def splitDataset(data,steps):
    X,Y = [],[]
    print("===========")
    for i in range(len(data)):
        endix = i+steps
        if endix > len(data)-1:
            break
        dataX,dataY = data[i:endix],data[endix]
        X.append(dataX)
        Y.append(dataY)
    return np.array(X),np.array(Y)


def activationComparison(data,fonk,kat):
    winSize=4
    features = 1
 
    x,y = splitDataset(data,winSize)
    
    model = Sequential()
    model.add(LSTM(kat,activation=fonk,input_shape=(winSize,features)))
    model.add(Dense(1))
    model.compile(loss="mean_squared_error",optimizer="adam")

    x = x.reshape((x.shape[0],x.shape[1],features))

    model.fit(x,y,epochs=100,batch_size=1,verbose=0)

    inp = np.array([110,120,130,140])
    inp = inp.reshape((1,winSize,features)) 
    predict = model.predict(inp,verbose=0)
    print(predict[0])
    df = pd.DataFrame(columns=["FunctionName","Prediction"])
    dic = {
            "FunctionName":fonk,
            "NumOfLayers":kat,
            "Prediction":predict[0]
        }
    df = df.append(dic,ignore_index=True)

    return df
            
   
df = pd.DataFrame()
data = np.array([10,20,30,40,50,60,70,80,90,100])
funcList = ["relu",
            "sigmoid",
            "softmax",
            "tanh"]

layers = [150,200,250]


for func in funcList:
    for lay in layers:
        df = df.append(activationComparison(data,func,lay))
print("The Value That Must Be:" + str(150))
print(df)
