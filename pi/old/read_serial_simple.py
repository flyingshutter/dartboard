#!/usr/bin/env python
import time
import serial

ser = serial.Serial(
      port='/dev/ttyACM0',
      baudrate = 115200,
      parity=serial.PARITY_NONE,
      stopbits=serial.STOPBITS_ONE,
      bytesize=serial.EIGHTBITS,
      timeout=0

)

disp = serial.Serial(
              
               port='/dev/ttyAMA0',
               baudrate = 115200,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=0
           )
  

#time.sleep(1)


bar1=0
bar2=0
bar3=0
bar4=0
bar5=0
bar6=0
bar7=0
bar8=0
current_player=0
counter=0
myList=["","","","","","","",""]
while 1:
  ser.write('A')
  x=ser.readline()
  
  
  print x
  #time.sleep(0.1)
  
