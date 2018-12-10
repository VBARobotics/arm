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

print "***testcode***"
ElbowDn=[0,1,0]
#MoveArm(1,ElbowDn)

iFile=sys.argv[1]
#"motions.txt"

with open(iFile) as f:
    polyShape = []
    for line in f:
           row= map(int, line.split(','))
           print row
           MoveArm(1,row)
