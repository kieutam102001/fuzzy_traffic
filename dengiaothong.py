import time
import cv2
from vehicle_detector import VehicleDetector
from fuzzy import fuzzy_controller_function
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
  RY= 6
class TrafficLightLEDs:
  RED = 9
  AMBER = 10
  GREEN = 11
currentState = TrafficLightStates.GR
s=0

def mocam():
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        if ret:
            cv2.imshow('cam', frame)
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            print("Turning off camera.")
            cam.release()
            print("Camera off.")
            cv2.destroyAllWindows()
            break

def time1(x):
        for x in range(x, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600)
            print(f"{seconds:2}")
            time.sleep(1)
        time.sleep(1)

while True:
    if (currentState == TrafficLightStates.GR):
        currentState=TrafficLightStates.GER
        print("Den xanh 1, den do 2")
        time1(5)
        mocam()
    elif(currentState==TrafficLightStates.GER):
        currentState = TrafficLightStates.YR
        print("Den xanh mo rong 1, den do 2")
        vd = VehicleDetector()
        cam1 = cv2.imread("saved_img.jpg")
        cam2 = cv2.imread("images/pexels-erik-mclean-4928599.jpg")
        vehicle_boxes1 = vd.detect_vehicles(cam1)
        vehicle_count1 = len(vehicle_boxes1)
        vehicle_boxes2 = vd.detect_vehicles(cam2)
        vehicle_count2 = len(vehicle_boxes2)
        t = fuzzy_controller_function(str(vehicle_count1), str(vehicle_count2))
        print("Thoi gian den xanh 1 mo rong: " + str(t))
        for x in range(t, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600)
            print("Xanh " + f"{minutes:02}:{seconds:02}")
            time.sleep(1)
    elif (currentState == TrafficLightStates.YR):
        currentState = TrafficLightStates.RG
        print("Den vang 1, den do 2")
        time1(2)
    elif (currentState == TrafficLightStates.RG):
        currentState = TrafficLightStates.RGE
        print("Den do 1, den xanh 2")
        time1(5)
        mocam()
    elif (currentState == TrafficLightStates.RGE):
        currentState = TrafficLightStates.RY
        print("Den do 1, den xanh mo rong 2")
        vd = VehicleDetector()
        cam1 = cv2.imread("images/pexels-scott-webb-2385546.jpg")
        cam2 = cv2.imread("images/pexels-scott-webb-2385546.jpg")
        vehicle_boxes1 = vd.detect_vehicles(cam1)
        vehicle_count1 = len(vehicle_boxes1)
        vehicle_boxes2 = vd.detect_vehicles(cam2)
        vehicle_count2 = len(vehicle_boxes2)
        t = fuzzy_controller_function(str(vehicle_count1), str(vehicle_count2))
        print("Thoi gian den xanh 2 mo rong: " + str(t))
        for x in range(t, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600)
            print("Xanh " + f"{minutes:02}:{seconds:02}")
            time.sleep(1)
    elif (currentState == TrafficLightStates.RY):
        currentState = TrafficLightStates.GR
        print("Den do 1, den vang 2")
        time1(2)
