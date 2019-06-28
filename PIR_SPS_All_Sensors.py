#This is the PIR sensor code. It runs the other sensors when detecting motion
#and then when it does it takes a picture and prints out the data taken with the
#picture inside of the shell. It is stopped by the button command.

#import the necessary packages
from gpiozero import Button, MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause
import datetime
import time
import Three_chip_sensors_data

#create objects that refer to a button,
#a motion sensor and the PiCamera
button = Button(17)
pir = MotionSensor(4)   
camera = PiCamera()

#start the camera
camera.rotation = 180
camera.start_preview()

#image image names
#i = 0
date= datetime.datetime.now().strftime("%Y_%_m_%d_%H_%M_%S")

#stop the camera when the pushbutton is pressed
def stop_camera():
    #camera.stop_preview()
    #exit the program
    exit()
    
def run(runfile):
    with open(runfile, "r") as rnf:
        exec(rnf.read())
        
#take photo when motion is detected
def take_photo():
    print("Motion detected")
    run("Three_chip_sensors_data.py")
    date = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    camera.capture("/home/pi/Motion_and_Data/" +date+ ".jpg")
    print("A photo has been taken")
    

#assign a function that runs when the button is pressed
button.when_pressed = stop_camera
#assign a function that runs when motion is detected
pir.when_motion = take_photo

pause()
