import serial
import time

port = 'COM6'   #COM3 incoming & COM4 outgoing

baud_rate = 9600
 
ser = serial.Serial(port, baud_rate)

data_to_send = "Hello, HC-05!"
ser.write(data_to_send.encode())

