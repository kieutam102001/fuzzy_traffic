# ----- An UDP server in Python that receives temperature values from clients-----
import cv2
import time
from vehicle_detector import VehicleDetector
import socket
from time import sleep
import datetime
from struct import pack
# Define the IP address and the Port Number
vd = VehicleDetector()
img=cv2.imread("images/pexels-ashley-fontana-705774.jpg")
scale_percent = 50  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
test1 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

video_capture_0 = cv2.VideoCapture(1)
video_capture_1 = cv2.VideoCapture(0)
video_capture_0.set(3, 720)-
video_capture_0.set(4, 640)
video_capture_1.set(3, 720)
video_capture_1.set(4, 640)


def cam():

    while True:
        # Capture frame-by-frame
        ret0, frame0 = video_capture_0.read()
        cv2.imwrite('D:/Do an/anh/anh0.jpg', frame0)
        ret1, frame1 = video_capture_1.read()
        cv2.imwrite('D:/Do an/anh/anh1.jpg', frame1)
        print("Da chup xong")
        break

ip = "172.20.10.8"

port = 7070

listeningAddress = (ip, port)

# Create a datagram based server socket that uses IPv4 addressing scheme

datagramSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

datagramSocket.bind(listeningAddress)
print("ok")
while (True):


    tempVal, sourceAddress = datagramSocket.recvfrom(128)
    print("Temperature at %s is %s" % (sourceAddress, tempVal.decode()))
    """vehicle_boxes1 = vd.detect_vehicles(test1)
    vehicle_count1 = len(vehicle_boxes1)
    response = str(vehicle_count1)
    datagramSocket.sendto(response.encode(), sourceAddress)"""
    cam()
    vd = VehicleDetector()
    cam1 = cv2.imread("D:/Do an/anh/anh0.jpg")
    cam2 = cv2.imread("D:/Do an/anh/anh1.jpg")
    vehicle_boxes1 = vd.detect_vehicles(cam1)
    vehicle_count1 = len(vehicle_boxes1)
    vehicle_boxes2 = vd.detect_vehicles(cam2)
    vehicle_count2 = len(vehicle_boxes2)
    print(vehicle_count1, vehicle_count2)
    response = pack('2f', vehicle_count1, vehicle_count2)
    datagramSocket.sendto(response, sourceAddress)
    print("-----------------")
