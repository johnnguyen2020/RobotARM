#cool
import serial # import the serial library
import time # import the time library
from time import sleep
#import RPi.GPIO as GPIO
from tkinter import * #import Tkinter GUI library



#Variable declarations
DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
DIR2 = 22
STEP2 = 27
DIR3 = 19
STEP3 = 26



CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 1   # Steps per Revolution (360 / 7.5)

'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)
GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)
GPIO.output(DIR2, CW)
GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(STEP3, GPIO.OUT)
GPIO.output(DIR3, CW)



MODE = (14, 15, 18)   # Microstep Resolution GPIO Pins
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}
GPIO.output(MODE, RESOLUTION['Full'])

'''
step_count = SPR * 1
delay = .0208 / 1



class StepperActions:
    
    def __init__(self):
        self.logicLeft = False
        self.logicRight = False
        self.logicUp = False
        self.logicDown = False
        self.logicForward = False
        self.logicBackward = False
        self.trigger = 0



##        self.GPIO.setmode(self.GPIO.BCM)
##        self.GPIO.setup(DIR, self.GPIO.OUT)
##        self.GPIO.setup(STEP, self.GPIO.OUT)
##        self.GPIO.output(DIR, CW)
##        self.GPIO.setup(DIR2, self.GPIO.OUT)
##        self.GPIO.setup(STEP2, self.GPIO.OUT)
##        self.GPIO.output(DIR2, CW)
##        self.GPIO.setup(DIR3, self.GPIO.OUT)
##        self.GPIO.setup(STEP3, self.GPIO.OUT)
##        self.GPIO.output(DIR3, CW)
        
    def angle_2_step(self, floatNum):
        self.angle = floatNum
        
#defining the functions
    def Right(self, resultnum):
        GPIO.output(DIR3, CW)
        print("CW")
        for x in range(int(round(resultnum/2))):
            GPIO.output(STEP3, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP3, GPIO.LOW)
            sleep(delay)

    def Left(self, resultnum):
        GPIO.output(DIR3, CCW)
        print("CCW")
        for x in range(int(round(resultnum/2))):
            GPIO.output(STEP3, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP3, GPIO.LOW)
            sleep(delay)

    def Up(self, resultnum):
        GPIO.output(DIR, CW)
        print("Up")
        for x in range(int(round(resultnum/2))):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)

    def Down(self, resultnum):
        GPIO.output(DIR, CCW)
        print("Down")
        for x in range(int(round(resultnum/2))):
            GPIO.output(STEP, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP, GPIO.LOW)
            sleep(delay)

    def Forward(self, resultnum):
        GPIO.output(DIR2, CW)
        print("forward")
        for x in range(int(round(resultnum/2))):
            GPIO.output(STEP2, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP2, GPIO.LOW)
            sleep(delay)

    def Backward(self, resultnum):
        GPIO.output(DIR2, CCW)
        print("backward")
        for x in range(int(round(resultnum/2))):
            GPIO.output(STEP2, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STEP2, GPIO.LOW)
            sleep(delay)
    