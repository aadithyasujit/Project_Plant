import RPi.GPIO as GPIO
import subprocess
while True:
    GPIO.cleanup()   
    subprocess.Popen("simpletest.py", shell=True)

#    sensor = Adafruit_DHT.DHT11
#    pin = 4
#    ldr = LightSensor(17)
#         
##    while True:
#       
#
#    light = ldr.value
#    print('Light Source={0:0.1f}%'.format(light*100))
#    if (light == 0 or light < 0.15):
#        print('Bright light available')
#    elif (light > 0.15 and light < 0.7):
#        print ('Partial light available')
#    else:
#        print ('Not sufficient light')
#
time.sleep(10)
#    
