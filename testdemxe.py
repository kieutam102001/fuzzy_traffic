import cv2
import time
from vehicle_detector import VehicleDetector

vd = VehicleDetector()
img=cv2.imread("images/pexels-scott-webb-2385546.jpg")
scale_percent = 80  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
test1 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

print("dang tinh")
vehicle_boxes = vd.detect_vehicles(test1)
vehicle_count = len(vehicle_boxes)
for box in vehicle_boxes:
        x, y, w, h = box
        cv2.rectangle(test1, (x, y), (x + w, y + h), (25, 0, 180), 3)

       # cv2.putText(test1, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

cv2.imshow("Cars", test1)
print(type(vehicle_count))
cv2.waitKey(0)