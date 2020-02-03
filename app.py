from flask import Flask
from flask import render_template
import serial
import serial.tools.list_ports
import time

def record():
    p = list(serial.tools.list_ports.comports()) #listing the available ports
    arduino = " "
    for ports in p:             #identifying port address for arduino
    	arduino=ports.device
    ser = serial.Serial(arduino)
    while(1):
    	ch=input("\nBegin Sequence reading(enter y to continue)....\n")    #ask the participant to start recording gestures
    	if(ch=='y'):
    		#name = input("File to be created:\n")	#create a file to record gestures
    		#f = open(name,'a+')
    		try:
    			#print("Reading into file")
    			while(1):
    				#time_var=time.time()			#note current time in seconds
    				p = ser.readline()				#reading values from the serial port
    				print(p)
    				try:
    					p = p.decode()				#decode the line which is in bytes to string
    				except UnicodeDecodeError:		# if error discard the value and continue with the next value
    					continue
    				s = str(time_var) + "\t" + str(p) #convert time to string-type and append it along with the data.
    				#f.write(s)
    		except KeyboardInterrupt:				#use ctrl-c to stop once the gesture is completed
    			pass
    		#f.close()								#close the file and repeat
    	else:
    		break									#if the user enters anything but 'y' break from while

app = Flask(__name__)

@app.route('/')
def main():
   
   return render_template('template.html')

if __name__ == '__main__':
   app.run()
