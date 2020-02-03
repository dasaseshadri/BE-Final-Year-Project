from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM
import numpy as np


dataset = np.loadtxt("/Cleaned_data/updated_features",delimiter=",")

X = dataset[:,1:9]
Y = dataset[:,0]

#Y = labelencoder_y_1.fit_transform(Y)

print(X)
print(Y)

model = Sequential()





model.add(Dense(10,input_dim=8,activation='relu'))
model.add(Dense(3,activation='relu'))
model.add(Dense(1,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
history=model.fit(X,Y,epochs=2000)
scores = model.evaluate(X,Y)

print("%s: %.2f%%" %(model.metrics_names[1],scores[1]*100))
#print(history.history.keys())
