# -- import library --
import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
import serial
import time
import threading

# -- set tensorflow library --
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly

# -- set directory path --
directory = 'C:/TUMz/Freelance/detect_cars_windowsApp'
imageCapture = directory + '/public/'

# -- set webcam device --
vid1 = cv2.VideoCapture(1)
vid2 = cv2.VideoCapture(2)
vid3 = cv2.VideoCapture(3)
vid4 = cv2.VideoCapture(4)

# -- set serial arduino port --
serial = serial.Serial("COM3", 9600, timeout = 1)

# -- set serial monitor readline -- 
def read_from_port(serial):
    while True:
        ret1, frame1 = vid1.read() # read webcam
        ret2, frame2 = vid2.read()
        ret3, frame3 = vid3.read()
        ret4, frame4 = vid4.read()
        
        readline = serial.readline().decode('ISO-8859-1').strip()
        
        # if readline != "":
        #     print(readline)
        
        process(readline, frame1, frame2, frame3, frame4)    
    
# function main process 
def process(readline, frame1, frame2, frame3, frame4):
    if (readline == ""):
        serial.write("Camera1".encode())
        
    if (readline == "Camera1"):
        print("State : 1")
        
        # image_name = time.strftime("%d-%m-%Y%H%M%S")
        # cv2.imwrite(imageCapture + image_name + ".jpg", frame1)
        # imageSRC = (imageCapture + image_name + ".jpg")
        
        imageSCR = cv2.imread("./public/images/280137615_665992267830300_91390289259333793_n.jpg")
        box, label, count = cv.detect_common_objects(imageSCR)
        output = draw_bbox(imageSCR, box, label, count)
        # plt.imshow(output)
        # plt.show()
        cell_phone = 0
        car = 0

        cell_phone = label.count('cell phone')
        car = label.count('car')
        sum_count = cell_phone + car
        print("Total number of cars : " + str(sum_count))
        
        serial.write("Camera1".encode())
        
    if (readline == "Camera2"):
        print("State : 2")
        
        # image_name = time.strftime("%d-%m-%Y%H%M%S")
        # cv2.imwrite(imageCapture + image_name + ".jpg", frame2)
        # imageSRC = (imageCapture + image_name + ".jpg")
        
        imageSCR = cv2.imread("./public/images/279378609_1059759441315735_1189456443045940171_n.jpg")
        box, label, count = cv.detect_common_objects(imageSCR)
        output = draw_bbox(imageSCR, box, label, count)
        # plt.imshow(output)
        # plt.show()
        cell_phone = 0
        car = 0

        cell_phone = label.count('cell phone')
        car = label.count('car')
        sum_count = cell_phone + car
        print("Total number of cars : " + str(sum_count))
        
        serial.write("Camera2".encode())
        
    if (readline == "Camera3"):
        print("State : 3")
        
        # image_name = time.strftime("%d-%m-%Y%H%M%S")
        # cv2.imwrite(imageCapture + image_name + ".jpg", frame3)
        # imageSRC = (imageCapture + image_name + ".jpg")
        
        imageSCR = cv2.imread("./public/images/279710528_1084053202148064_6843525306553694311_n.jpg")
        box, label, count = cv.detect_common_objects(imageSCR)
        output = draw_bbox(imageSCR, box, label, count)
        # plt.imshow(output)
        # plt.show()
        cell_phone = 0
        car = 0

        cell_phone = label.count('cell phone')
        car = label.count('car')
        sum_count = cell_phone + car
        print("Total number of cars : " + str(sum_count))
        
        serial.write("Camera3".encode())
        
    if (readline == "Camera4"):
        print("State : 4")
        
        # image_name = time.strftime("%d-%m-%Y%H%M%S")
        # cv2.imwrite(imageCapture + image_name + ".jpg", frame4)
        # imageSRC = (imageCapture + image_name + ".jpg")
        
        imageSCR = cv2.imread("./public/images/280079686_693937488537735_1978017886745150351_n.jpg")
        box, label, count = cv.detect_common_objects(imageSCR)
        output = draw_bbox(imageSCR, box, label, count)
        # plt.imshow(output)
        # plt.show()
        cell_phone = 0
        car = 0

        cell_phone = label.count('cell phone')
        car = label.count('car')
        sum_count = cell_phone + car
        print("Total number of cars : " + str(sum_count))
        
        serial.write("Camera4".encode())
    
if __name__ == "__main__":
    # exit_event.set()
    thread = threading.Thread(target = read_from_port, args = (serial,))
    thread.start()