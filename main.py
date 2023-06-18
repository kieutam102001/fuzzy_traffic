from gpiozero import LED
from time import sleep
from gpiozero import LEDCharDisplay
import time
import cv2
from vehicle_detector import VehicleDetector
from fuzzy import fuzzy_controller_function
import socket
from fuzzy import fuzzy_controller_function
from struct import unpack

display = LEDCharDisplay(18, 23, 24, 25, 8, 7, 12, active_high=False) #do2
display1 = LEDCharDisplay(26, 9, 6, 13, 19, 11, 5, active_high=False) #xanh1
green = LED(20)
red = LED(4)
yellow = LED(21)
green2 = LED(17)
red2 = LED(22)
yellow2 = LED(27)
serverAddress = ("192.168.82.37", 7070)

# Create a datagram socket
Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


class TrafficLightStates:
    # s = 1 a=G b=R
    # s = 2 a=G+ b=R
    # s = 3 a=Y b=R
    # s = 4 a=R b=G
    # s = 5 a=R b=G+
    # s = 6 a=R b=Y
    GR = 1
    GER = 2
    YR = 3
    RG = 4
    RGE = 5
    RY = 6


class TrafficLightLEDs:
    RED = 9
    AMBER = 10
    GREEN = 11


currentState = TrafficLightStates.GR
s = 0


def time1(x):
    for x in range(x, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        print(f"{seconds:2}")
        time.sleep(1)
    time.sleep(1)

def dis1(x):
    if (x==1):
        for char in '10':
            display1.value = char
            sleep(1)
    if (x==2):
        for char in '210':
            display1.value = char
            sleep(1)
    if (x==3):
        for char in '3210':
            display1.value = char
            sleep(1)
    if (x==4):
        for char in '43210':
            display1.value = char
            sleep(1)
    if (x==5):
        for char in '543210':
            display1.value = char
            sleep(1)
    if (x==6):
        for char in '6543210':
            display1.value = char
            sleep(1)
def dis(x):
    if (x==1):
        for char in '10':
            display.value = char
            sleep(1)
    if (x==2):
        for char in '210':
            display.value = char
            sleep(1)
    if (x==3):
        for char in '3210':
            display.value = char
            sleep(1)
    if (x==4):
        for char in '43210':
            display.value = char
            sleep(1)
    if (x==5):
        for char in '543210':
            display.value = char
            sleep(1)
    if (x==6):
        for char in '6543210':
            display.value = char
            sleep(1)

while True:
    if (currentState == TrafficLightStates.GR):
        currentState = TrafficLightStates.GER
        print("----------------------------")
        print(" ")
        print("Den xanh 1, den do 2")
        green.on()
        red.off()
        yellow.off()
        green2.off()
        red2.on()
        yellow2.off()
        for char in '9876543210':
            display.value = char
            display1.value = char
            sleep(1)
    elif (currentState == TrafficLightStates.GER):
        currentState = TrafficLightStates.YR
        print("----------------------------")
        print(" ")
        print("Den xanh mo rong 1, den do 2")
        green.on()
        red2.on()
        tempString = "%.2f" % 1
        Socket.sendto(tempString.encode(), ("192.168.82.37", 7070))
        response = Socket.recv(1024)
        x, y = unpack('2f', response)
        t = fuzzy_controller_function(str(int(x)), str(int(y)))
        print("Thoi gian den xanh mo rong: " + str(t))
        dis1(t)
    elif (currentState == TrafficLightStates.YR):
        currentState = TrafficLightStates.RG
        print("----------------------------")
        print(" ")
        print("Den vang 1, den do 2")
        green.off()
        red2.on()
        yellow.on()
        for char in '210':
            display1.value = char
            sleep(1)
    elif (currentState == TrafficLightStates.RG):
        currentState = TrafficLightStates.RGE
        print("----------------------------")
        print(" ")
        print("Den do 1, den xanh 2")
        yellow.off()
        red2.off()
        red.on()
        green2.on()
        for char in '9876543210':
            display.value = char
            display1.value = char
            sleep(1)
    elif (currentState == TrafficLightStates.RGE):
        currentState = TrafficLightStates.RY
        print("----------------------------")
        print(" ")
        print("Den do 1, den xanh mo rong 2")
        red.on()
        green2.on()
        tempString = "%.2f" % 1
        Socket.sendto(tempString.encode(), ("192.168.82.37", 7070))
        response = Socket.recv(1024)
        x,y= unpack('2f',response)
        t = fuzzy_controller_function(str(int(y)), str(int(x)))
        print("Thoi gian den xanh mo rong: " + str(t))
        dis(t)
    elif (currentState == TrafficLightStates.RY):
        currentState = TrafficLightStates.GR
        print("----------------------------")
        print(" ")
        print("Den do 1 ,  den vang 2")
        red.on()
        green2.off()
        yellow2.on()
        for char in '210':
            display.value = char
            sleep(1)