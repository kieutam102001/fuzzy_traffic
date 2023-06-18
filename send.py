# ----- An UDP client in Python that sends temperature values to server-----

import socket
from time import sleep
import random
from fuzzy import fuzzy_controller_function
from struct import unpack


# A tuple with server ip and port

serverAddress = ("192.168.82.37", 7070)

# Create a datagram socket

tempSensorSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

        tempString = "%.2f" % 1
        tempSensorSocket.sendto(tempString.encode(), ("192.168.82.37", 7070))
        response = tempSensorSocket.recv(1024)
        x,y= unpack('2f',response)
        t = fuzzy_controller_function(str(int(x)), str(int(y)))
        print("Thoi gian den xanh mo rong: " + str(t))
        print("-------------------------")




        """
        a=str(response,'utf-8')
        print(a)
        
        """