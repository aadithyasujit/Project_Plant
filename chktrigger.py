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
portal = "/dev/ttyACM0"
ser = serial.Serial(portal, 9600)

###################################################################################################
##############################----Main body ----################################
####################################################################################################
datatimer = 60

while 1 :
        ser.flushInput()    # Clearing buffer and garbage values
        ser.flushOutput()

        ser.write(b'1')

        if(ser.in_waiting > 0):
                client.loop()
                incomdata = ser.readline()  # Reads as Bytes format from ardu 
                print(incomdata)
                ser.flushInput()    # Clearing buffer and garbage values
                ser.flushOutput()
                serverwrite(incomdata, bbt, client)
##                dataprocess()      # add to process status and datas 
                time.sleep(datatimer)

