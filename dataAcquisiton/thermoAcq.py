import serial
import json
from time import localtime

brewname = "My Brown Nuts"
ser = serial.Serial('/dev/ttyACM0', 9600)
datapoint = {'temperature': None,
             'timestamp': None,
             'brewname': brewname}

while True:
    datapoint['temperature'] = ser.readline()
    datapoint['timestamp'] = localtime()
    datapointjson = json.dumps(datapoint)

f.close()
ser.close()
