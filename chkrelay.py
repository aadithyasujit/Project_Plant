import datetime
import serial
import time
from serverwrite import beebotteconnect
from serverwrite import serverwrite
from serverwrite import cayenneconnect
####################################################################################################
##############################----Beebotte Setup  ------------------################################
####################################################################################################

bbt = beebotteconnect()
##print(bbt)

####################################################################################################
##############################----Cayenne Setup  ------------------################################
####################################################################################################

client = cayenneconnect()

####################################################################################################
##############################----Device port setup and main log loop ----################################
####################################################################################################

ser = serial.Serial("/dev/ttyACM0", 9600)

####################################################################################################
##############################----Main body ----################################
####################################################################################################
def rwonly(datatimer):
    ser.flushInput()    # Clearing buffer and garbage values
    ser.flushOutput()
    if(ser.in_waiting >0):
        client.loop()
        incomdata = ser.readline()  # Reads as Bytes format from ardu 
        print(incomdata)
        ser.flushInput()    # Clearing buffer and garbage values
        ser.flushOutput()
        serverwrite(incomdata, bbt, client)
        time.sleep(datatimer)

datatimer = 60
x = 1

while 1 :
            ser.flushInput()    # Clearing buffer and garbage values
            ser.flushOutput()

            ser.write(b'1')
            if(ser.in_waiting >0):
                client.loop()
                incomdata = ser.readline()  # Reads as Bytes format from ardu 
                print(incomdata)
                prodata=incomdata.decode()  # converting byte to string for data cleaup (#Python3 problems)
                prodata=prodata[:-2]  # Removing the 2 random shit char found after decode.
                print(prodata)
                ah,at,b1,b2,bavg,st,sm,r1,r2,r3,r4 = prodata.split(',') # spliting data with "," delimited and saving string variables
                Humidity=float(ah);       # Convert string to float type for Server
                Temperature=float(at);
                Brightness1=float(b1);
                Brightness2=float(b2);
                Brightnessavg=float(bavg);
                SoilT=float(st);
                SoilM=float(sm);
                Relay1=(r1);
                Relay2=(r2);
                Relay3=(r3);
                Relay4=(r4);
                #  Write to Cayenne server, matching resourse and Channel.
                client.luxWrite(1, Humidity)
                client.celsiusWrite(2, Temperature)
                client.luxWrite(3, Brightness1)
                client.luxWrite(4, Brightness2)
                client.luxWrite(5, Brightnessavg)
                client.celsiusWrite(6, SoilT)
                client.luxWrite(7, SoilM)
                client.luxWrite(8, Relay1)
                client.luxWrite(9, Relay2)
                client.luxWrite(10, Relay3)
                client.virtualWrite(11, Relay4)
                print('Print to cayenne sucessful')
                # Write to BeeBotte server, matching resourse and Channel.
                bbt.write('ProjectPlant', 'Humidity', Humidity)
                bbt.write('ProjectPlant', 'Temperature', Temperature)
                bbt.write('ProjectPlant', 'Brightness1', Brightness1)
                bbt.write('ProjectPlant', 'Brightness2', Brightness2)
                bbt.write('ProjectPlant', 'Brightnessavg', Brightnessavg)
                bbt.write('ProjectPlant', 'SoilM', SoilM)
                bbt.write('ProjectPlant', 'SoilT', SoilT)
                bbt.write('ProjectPlant', 'Relay1', Relay1)
                bbt.write('ProjectPlant', 'Relay2', Relay2)
                bbt.write('ProjectPlant', 'Relay3', Relay3)
                bbt.write('ProjectPlant', 'Relay4', Relay4)
                print('Print to beebotte sucessful')

##                ser.flushInput()    # Clearing buffer and garbage values
##                ser.flushOutput()
                #serverwrite(incomdata, bbt, client)
                #time.sleep(datatimer)      
      
