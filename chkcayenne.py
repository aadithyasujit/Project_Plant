import datetime
import serial
from beebotte import *
import json
import sys
import cayenne.client
import time

####################################################################################################
##############################----Beebotte Setup  ------------------################################
####################################################################################################

### Connect using Token and Hostname
_hostname   = 'api.beebotte.com'
_token      = 'token_wF8Nu5PEWfuRpd5s'
bbt = BBT(token = _token, hostname = _hostname)

### Connect using API and secret Key
# Replace API_KEY and SECRET_KEY with those of your account
#bbt = BBT('cc8V3veG79lduSgL9OyFEdL5', 'mTJiWUDr8URA4O0kmjOYLQ7Qb5kCZKwi',hostname = 'cc8V3veG79lduSgL9OyFEdL5.beebotte.com')

####################################################################################################
##############################----Cayenne Setup  ------------------################################
####################################################################################################


# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "2bb34e70-5540-11e9-bd24-d78d0eb46731"
MQTT_PASSWORD  = "2ce7ceb30a5fc9629c45ad6f17e22fcf9046ab84"
MQTT_CLIENT_ID = "d642e9b0-5543-11e9-a260-01b3f7f2fd21"

  # The callback for when a message is received from Cayenne.
#def on_message(message):
  #print("message received: " + str(message))
    # If there is an error processing the message return an error string, otherwise return nothing.

client = cayenne.client.CayenneMQTTClient()
#client.on_message = on_message
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)
  # For a secure connection use port 8883 when calling client.begin:
  # client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, port=8883)

####################################################################################################
##############################----Device port setup and main log loop ----################################
####################################################################################################
#datatimerate  = 1;

ser=serial.Serial('/dev/ttyACM0',9600) # Check port and address before start 

while 1 :
  client.loop()
  
   
    
    #ser.write("P")
    
  incomdata = ser.readline()  # Reads as Bytes format from ardu 
    #print(incomdata)
  ser.flushInput()    # Clearing buffer and garbage values
  ser.flushOutput()
  prodata=incomdata.decode()  # converting byte to string for data cleaup (#Python3 problems)
  prodata=prodata[:-2]  # Removing the 2 random shit char found after decode.
  #print(prodata)
  ah,at,b1,b2,bavg,st,sm = prodata.split(',') # spliting data with "," delimited and saving string variables
  Humidity=float(ah);       # Convert string to float type for Server
  Temperature=float(at);
  Brightness1=float(b1);
  Brightness2=float(b2);
  Brightnessavg=float(bavg);
  SoilT=float(st);
  SoilM=float(sm);
    
    #  Write to Cayenne server, matching resourse and Channel.
  client.luxWrite(1, Humidity)
  client.celsiusWrite(2, Temperature)
  client.luxWrite(3, Brightness1)
  client.luxWrite(4, Brightness2)
  client.luxWrite(5, Brightnessavg)
  client.celsiusWrite(6, SoilT)
  client.luxWrite(7, SoilM)
  print('Print to cayenne sucessful')
    #  Write to BeeBotte server, matching resourse and Channel.
  bbt.write('ProjectPlant', 'Humidity', Humidity)
  bbt.write('ProjectPlant', 'Temperature', Temperature)
  bbt.write('ProjectPlant', 'Brightness1', Brightness1)
  bbt.write('ProjectPlant', 'Brightness2', Brightness2)
  bbt.write('ProjectPlant', 'Brightnessavg', Brightnessavg)
  bbt.write('ProjectPlant', 'SoilM', SoilM)
  bbt.write('ProjectPlant', 'SoilT', SoilT)
  print('Print to beebotte sucessful')


