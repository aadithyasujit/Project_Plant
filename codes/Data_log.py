import serial

ser = serial.Serial('/dev/ttyUSB0',9600) # Check port and address before start 

while 1 :
    
    incomdata = ser.readline()  # Reads as Bytes format from ardu 
    
    print(incomdata)
    
    ser.flushInput()    # Clearing buffer and garbage values
    ser.flushOutput()
 
    prodata=incomdata.decode()  # converting byte to string for data cleaup (#Python3 problems)
    prodata=prodata[:-2]  # Removing the 2 random shit char found after decode.
#   print(prodata)
    
    Humidity,Temperature,Brightness,SoilM = prodata.split(',') # spliting data with "," delimited
    
    print("Humidity:", Humidity ,"%", "Temperature:", Temperature ,"C", "Brightness:", Brightness ,"%","Soil Moisture:", SoilM ,"%")
# Confirmation sake!!
