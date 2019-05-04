#import the USB and Time librarys into Python
import usb.core, usb.util, time, csv, sys

#Allocate the name 'RoboArm' to the USB device
RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x001)
#RoboArm = usb.core.find(idVendor=1267, idProduct=0001)

#Check if the arm is detected and warn if not
if RoboArm is None:
    raise ValueError("Arm not found - Check that arm is turned on and plugged in")

#Create a variable for duration
Duration=0.5

#Define a procedure to execute each movement
def MoveArm(Duration, ArmCmd):
    #Start the movement
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)
    #Stop the movement after waiting a specified duration
    time.sleep(Duration)
    ArmCmd=[0,0,0]
    RoboArm.ctrl_transfer(0x40,6,0x100,0,ArmCmd,3)

#MoveArm(1,[0,1,0]) #Rotate base anti-clockwise
#MoveArm(1,[0,2,0]) #Rotate base clockwise
#MoveArm(1,[64,0,0]) #Shoulder up
#MoveArm(1,[128,0,0]) #Shoulder down
#MoveArm(1,[16,0,0]) #Elbow up
#MoveArm(1,[32,0,0]) #Elbow down
#MoveArm(1,[4,0,0]) #Wrist up
#MoveArm(1,[8,0,0]) # Wrist down
#MoveArm(1,[2,0,0]) #Grip open
#MoveArm(1,[1,0,0]) #Grip close
#MoveArm(1,[0,0,1]) #Light on
#MoveArm(1,[0,0,0]) #Light off

print ("Saving Motions to file: arm_motions.txt")

print ("x -Exit")
print ("j -Rotate base counter-clockwise")
print ("k -Rotate base clockwise")
print ("i -Shoulder up")
print ("m -Shoulder down")
print ("u -Elbow up")
print ("n -Elbow down")
print ("y -Wrist up")
print ("b -Wrist down")
print ("t -Grip open")
print ("v -Grip close")
print ("r - light on")
print ("c - light off")

ElbowDn=[0,1,0]
#MoveArm(1,ElbowDn)

import readchar
f = open('arm_motions.txt', 'w')
    
while True:
  key=repr(readchar.readchar())
#  print(key)
  if key=="'x'":
    f.close()
    break
  if key=="'u'":
    f.write('16,0,0\n')
    MoveArm(1,[16,0,0])
  if key=="'n'":
    f.write('32,0,0\n')
    MoveArm(1,[32,0,0])
  if key=="'j'":
    f.write('0,2,0\n')
    MoveArm(1,[0,2,0])
  if key=="'k'":
    f.write('0,1,0\n')
    MoveArm(1,[0,1,0])
  if key=="'i'":
    f.write('64,0,0\n')
    MoveArm(1,[64,0,0])
  if key=="'m'":
    f.write('128,0,0\n')
    MoveArm(1,[128,0,0])
  if key=="'y'":
    f.write('4,0,0\n')
    MoveArm(1,[4,0,0])
  if key=="'b'":
    f.write('8,0,0\n')
    MoveArm(1,[8,0,0])
  if key=="'t'":
    f.write('2,0,0\n')
    MoveArm(1,[2,0,0])
  if key=="'v'":
    f.write('1,0,0\n')
    MoveArm(1,[1,0,0])
  if key=="'r'":
    f.write('0,0,1\n')
    MoveArm(1,[0,0,1])
  if key=="'c'":
    f.write('0,0,0\n')
    MoveArm(1,[0,0,0])





