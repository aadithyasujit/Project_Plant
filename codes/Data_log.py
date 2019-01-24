import datetime
import serial
from beebotte import *
import time
import json
import sys

import gspread
from oauth2client.service_account import ServiceAccountCredentials

####################################################################################################
##############################----Google Spreadsheet Data Setup ----################################
####################################################################################################


GDOCS_OAUTH_JSON       = 'ProjectPlant-f697b8eaf2b9.json'

# Google Docs spreadsheet name.
GDOCS_SPREADSHEET_NAME = 'projectplant'

# How long to wait (in seconds) between measurements.

def login_open_sheet(oauth_key_file, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    try:
        scope =  ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1
        return worksheet
    except Exception as ex:
        print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)

#print('Logging sensor measurements to {0} every {1} seconds.'.format(GDOCS_SPREADSHEET_NAME, FREQUENCY_SECONDS))
#print('Press Ctrl-C to quit.')

worksheet = None

####################################################################################################
##############################----Google Spreadsheet logging function----###########################
####################################################################################################


def datalog(Temperature, Humidity, Brightness, SoilM):
    worksheet = None

    if worksheet is None:
        worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)

    #print('Temperature: {0:0.2f} C'.format(Temperature))
    #print('Humidity:    {0:0.2f} %'.format(Humidity))
    #print('Humidity:    {0:0.2f} %'.format(Brightness))
    #print('Humidity:    {0:0.2f} %'.format(SoilM))
    date_str = json.dumps(datetime.datetime.now().strftime("%Y-%m-%d"))
    time_str = json.dumps(datetime.datetime.now().strftime("%H:%M:%S"))
    #print(date_str)
    #print(time_str)

    worksheet.append_row((date_str, time_str, Temperature, Humidity, Brightness, SoilM))

    worksheet = None
    
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
##############################----Device port setup and main log loop ----################################
####################################################################################################

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
    datalog(Temperature, Humidity, Brightness, SoilM)
    print("Humidity:", Humidity ,"%", "Temperature:", Temperature ,"C", "Brightness:", Brightness ,"%","Soil:", SoilM ,"%")
    print('Write Successful to file'.format(GDOCS_SPREADSHEET_NAME))
    # Confirmation sake!!