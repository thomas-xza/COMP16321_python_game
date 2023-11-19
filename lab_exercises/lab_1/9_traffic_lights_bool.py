#!/usr/bin/env python3

def printState():
    print("Red Light is " + str(redLight))
    print("Yellow Light is "+ str(yellowLight))
    print("Green Light is "+ str(greenLight))

redLight = True
yellowLight = False
greenLight = False

printState()
            
if type(redLight) == type(True):

    print("Boolean type detected")
