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
  
  
  #print x
  time.sleep(0.1)
  if '#Players:1' in x:
   current_player=1
  if '#Players:2' in x:
   current_player=2
  if '#Players:4' in x:
   current_player=3
  if '#Players:8' in x:
   current_player=4
  if '#Players:16' in x:
   current_player=5
  if '#Players:32' in x:
   current_player=6
  if '#Players:64' in x:
   current_player=7
  if '#Players:128' in x:
   current_player=8    
  if '#Bar1:' in x:
    if current_player==1:
     bar1 = x[6:27] 
    if current_player==3:
     bar3 = x[6:27] 	
    if current_player==5:
     bar5 = x[6:27] 		
    if current_player==7:
     bar7 = x[6:27] 		
  if '#Bar2:' in x:
    if current_player==2:
     bar2 = x[33:54] 
    if current_player==4:
     bar4 = x[33:54] 	
    if current_player==6:
     bar6 = x[33:54] 		
    if current_player==8:
     bar8 = x[33:54] 			
  if bar1 != 0:
    myList[0]='#Player1:'+bar1+'@'
  if bar2 != 0:
    myList[1]='#Player2:'+bar2+'@'
  if bar3 != 0:
    myList[2]='#Player3:'+bar3+'@'
  if bar4 != 0:
    myList[3]='#Player4:'+bar4+'@'
  if bar5 != 0:
    myList[4]='#Player5:'+bar5+'@'
  if bar6 != 0:
    myList[5]='#Player6:'+bar6+'@'
  if bar7 != 0:
    myList[6]='#Player7:'+bar7+'@'
  if bar8 != 0:
    myList[7]='#Player8:'+bar8+'@' 	
  print myList[counter]
  disp.write(myList[counter])
  disp.write("\n")
  counter += 1
  if counter == 8:
   counter = 0
  
  
