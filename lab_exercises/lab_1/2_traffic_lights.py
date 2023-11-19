#!/usr/bin/env python3

def printState():
    print("Red Light is " + str(redLight))
    print("Yellow Light is "+ str(yellowLight))
    print("Green Light is "+ str(greenLight))

redLight = 1
yellowLight = 0
greenLight = 0

printState()
            
if type(redLight) == type("String"):

    print("String type detected")
