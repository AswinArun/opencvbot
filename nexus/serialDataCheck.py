import serial
import time

port = 'COM11'

baud_rate = 9600
 
ser = serial.Serial(port, baud_rate)

delay = 2

'''data_to_send = "Hello, HC-05!"
ser.write(data_to_send.encode())'''

try: 
    while True:
        value = 1.2
        dataToSend = str(value)
        ser.write(dataToSend.encode())

        time.sleep(delay)

except KeyboardInterrupt:
    pass
