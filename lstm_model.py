import numpy as np
from numpy import array
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import LSTM
from keras.utils.np_utils import to_categorical
import os


batch_size = 100
timesteps = 400
data_dim = 3

def sample(seq):
    seq_length = len(seq)
    mid = int(seq_length/2)
    low = mid - 200
    high = mid + 200
    num = np.array(seq[low:high,1:])
    #print(num,len(num),num.shape)
    return num

def fit_lstm(x_train,y_train):
    model = Sequential()
    model.add(LSTM(10, return_sequences=True,input_shape=(timesteps, data_dim)))
    model.add(LSTM(32, return_sequences=True))
    model.add(LSTM(32))
    model.add(Dense(10, activation='softmax'))
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    history=model.fit(x_train,y_train,epochs=50)
    scores = model.evaluate(x_train,y_train)

    print("%s: %.2f%%" %(model.metrics_names[1],scores[1]*100))


def main():
    list_dir = os.listdir('.')
    y_lab = []
    #print(list_dir)

    num_original=np.array([])
    #num_original=num_original.reshape(300,3,1)

    flag=1
    for l in list_dir:
        if(l=='features.py' or l =='updated_features' or l=='lstm_model.py'):
            continue
        d=os.chdir(l)
        #print(l)
        list_files = os.listdir(d)
        #print(list_files)
        for f in list_files:
            sequence = np.loadtxt(f)
            y_lab.append(l)
            num3d=sample(sequence)
            num3d=num3d.reshape((1,num3d.shape[0],num3d.shape[1]))
            if flag==1:
                num_original=num3d
                flag=0
                continue
            #print(num3d.shape)
            num_original=np.vstack((num_original,num3d))
            #print(num_original.shape)

        os.chdir('..')
        #print(y_lab)
    y_lab = array(y_lab)
    return num_original,y_lab


x,y = main()
#print(xtrain,ytrain)
print(x.shape[1],x.shape[2],y.shape)

y = to_categorical(y, num_classes=None)
fit_lstm(x,y)
