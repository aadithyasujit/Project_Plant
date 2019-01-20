from gpiozero import LightSensor

ldr = LightSensor(17)

while True

light = ldr.value

   print('Light Source={0:0.1f}%'.format(light*100))
    
if (light == 0 or light < 0.15):
        print('Bright light available')
elif (light > 0.15 and light < 0.7):
        print ('Partial light available')
else:
        print ('Not sufficient light')


    