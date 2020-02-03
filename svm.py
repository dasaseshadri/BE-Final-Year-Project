from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import numpy as np
import serial
import serial.tools.list_ports
import time


def fit_model():
    dataset = np.loadtxt("./Cleaned_data/updated_features",delimiter=",")

    X = dataset[:20,1:9]
    Y = dataset[:20,0]

    # training a linear SVM classifier
    from sklearn.svm import SVC
    svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X,Y)
    svm_predictions = svm_model_linear.predict(X)
    print(svm_predictions)

    # model accuracy for X_test
    accuracy = svm_model_linear.score(X, Y)

    # creating a confusion matrix
    cm = confusion_matrix(Y, svm_predictions)
    print(accuracy,cm)
    return svm_model_linear

def record():

    p = list(serial.tools.list_ports.comports()) #listing the available ports

    arduino = " "

    for ports in p:             #identifying port address for arduino
    	arduino=ports.device

    #print(ports.device)
    print(arduino)
    print('Initializing device communication')

    ser = serial.Serial(arduino) #opening serial port for communication


    while(1):
        ch=input("\nBegin Sequence reading(enter y to continue)....\n")    #ask the participant to start recording gestures
        if(ch=='y'):
            #name = input("File to be created:\n")	#create a file to record gestures
            f = open('testseq','w')
            try:
                print("Reading into file")
                while(1):
                    time_var=time.time()			#note current time in seconds
                    p = ser.readline()				#reading values from the serial port
                    print(p)
                    try:
                        p = p.decode()				#decode the line which is in bytes to string
                    except UnicodeDecodeError:		# if error discard the value and continue with the next value
                        continue
                    s = str(time_var) + "\t" + str(p)
                    tmp = s.split('\t')
                    print(tmp,len(tmp))
                    if(len(tmp)==4):
                        f.write(s)
            except KeyboardInterrupt:				#use ctrl-c to stop once the gesture is completed
                pass
                f.close()								#close the file and repeat
        else:
            break

dataset = np.loadtxt('testseq',skiprows=10)
x = dataset[1:,1]
y = dataset[1:,2]
z = dataset[1:,3]

seq=[]

seq=[x.mean(),y.mean(),z.mean(),x.var(),y.var(),z.var(),x.std(),y.std(),z.std()]
seq = np.array(seq)

model = fit_model()
