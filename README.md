# Project_Plant

Project Plant is an attempt to automate a Garden monitoring system. New to IoT, curious to see how far can this attempt go. With a vision 
to completely monitor and control environmental conditions to trigger seed germination and assist sapling growth until the plant is ready 
to join the main garden. 

I have decided try my hands on a very basic garden monitering and feedback system. But have included stages for as far and fancy as I could envision.    

Sensor Systems classification :: 

  - Build a system to sense ambient conditions such as light , humidity and temperature. This can also act as a local wheather station. 
  - Build ground sensor system to measure temperature and moisture of soil. 
  - Integrate 3 other light sensors - ambient around plant, 3 light sensors on the ground bed(avg value). 
  - Raspberry Pi camera for sensing plant changes. 
  
 Actuator Systems classification :: 

  - Lighting system: Led strip with grow light module. (variable brightness) 
  - Pump for irrigation system. 
  - Heat mat control
 
 Cloud based data for front end:: 

  - Ambient Temperature display 
  - Humidity % display + gauge
  - Soil Moisture % display + gauge
  - Soil Temperature display + gauge
  - Overall, Bed avg and zonal brightness values + chart
  - Light pump and mat on/off status!
  - Overall plant status! 
  - Time line notification since plant start! 
  - Diagnosis chek : pi temp, mat, light and pump working duration chart!  

 Data base for back end:: 

  - All the above mentioned with timestamp. 
