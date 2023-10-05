import serial, os
ser = serial.Serial('/dev/ttyAMA1', 9600, timeout=1)
ser.reset_input_buffer()
smd = "a\n"
smds = smd.encode('utf-8')
ser.write(smds)
os.system('echo $(date) >> $HOME/Desktop/Proyecto/logs/pulses.log')
