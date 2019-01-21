import datetime
import serial
from beebotte import *
import time

### Connect using Token and Hostname
_hostname   = 'api.beebotte.com'
_token      = 'token_wF8Nu5PEWfuRpd5s'
bbt = BBT(token = _token, hostname = _hostname)

### Connect using API and secret Key
# Replace API_KEY and SECRET_KEY with those of your account
#bbt = BBT('cc8V3veG79lduSgL9OyFEdL5', 'mTJiWUDr8URA4O0kmjOYLQ7Qb5kCZKwi',hostname = 'cc8V3veG79lduSgL9OyFEdL5.beebotte.com')

ser = serial.Serial('/dev/ttyUSB0',9600) # Check port and address before start 

#### Change channel name and resource names as suits you


while 1 :
    
    incomdata = ser.readline()  # Reads as Bytes format from ardu 
    
    #print(incomdata)
    
    ser.flushInput()    # Clearing buffer and garbage values
    ser.flushOutput()
 
    prodata=incomdata.decode()  # converting byte to string for data cleaup (#Python3 problems)
    prodata=prodata[:-2]  # Removing the 2 random shit char found after decode.
#   print(prodata)
    
    h,t,b,sm = prodata.split(',') # spliting data with "," delimited and saving string variables

    Humidity=float(h);       # Convert string to float type for Server
    Temperature=float(t);
    Brightness=float(b);
    SoilM=float(sm);

#  Write to BeeBotte server, matching resourse and Channel.

    bbt.write('ProjectPlant', 'Humidity', Humidity)
    bbt.write('ProjectPlant', 'Temperature', Temperature)
    bbt.write('ProjectPlant', 'Brightness', Brightness)
    bbt.write('ProjectPlant', 'Soil', SoilM)

#    ts = datetime.datetime.now()
#    print(ts)

    print("Humidity:", Humidity ,"%", "Temperature:", Temperature ,"C", "Brightness:", Brightness ,"%","Soil:", SoilM ,"%")
    # Confirmation sake!!
