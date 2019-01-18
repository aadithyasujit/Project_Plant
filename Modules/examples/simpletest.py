import Adafruit_DHT
import time
from gpiozero import LightSensor
import datetime

sensor = Adafruit_DHT.DHT11
pin = 4
ldr = LightSensor(17) 

  
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    light = ldr.value
    now = datetime.datetime.now()
    
    print ("Current date and time : ")
    print (now.strftime("%Y-%m-%d %H:%M:%S"))
    print('Temperature={0:0.1f}*C'.format(temperature))
    print('Humidity={0:0.1f}%'.format(humidity))
    print('Light Source={0:0.1f}%'.format(light*100))

    print('Light Source={0:0.1f}%'.format(light*100))
    
    if (light == 0 or light < 0.15):
        print('Bright light available')
    elif (light > 0.15 and light < 0.7):
        print ('Partial light available')
    else:
        print ('Not sufficient light')


    