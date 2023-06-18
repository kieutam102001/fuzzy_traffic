import cv2
import time
from vehicle_detector import VehicleDetector


video_capture_0 = cv2.VideoCapture(0)
video_capture_1 = cv2.VideoCapture(0)
video_capture_0.set(3, 720)
video_capture_0.set(4, 680)
video_capture_1.set(3, 720)
video_capture_1.set(4, 640)


while True:
    # Capture frame-by-frame
    ret0, frame0 = video_capture_0.read()

    print("Da chup anh")
    cv2.imwrite('D:/Do an/anh/anh0.jpg', frame0)
    print("Da chup anh1")
    ret1, frame1 = video_capture_1.read()
    cv2.imwrite('D:/Do an/anh/anh1.jpg', frame1)
    print("Da chup xong")
    break

# Load Veichle Detector
vd = VehicleDetector()
img=cv2.imread("D:/Do an/anh/anh0.jpg")
scale_percent = 100  # percent of original size
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

        cv2.putText(test1, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

cv2.imshow("Cars", test1)
print(type(vehicle_count))
cv2.waitKey(0)
