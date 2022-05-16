import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv

from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly

imageSCR = cv2.imread("./public/images/280137615_665992267830300_91390289259333793_n.jpg")
box, label, count = cv.detect_common_objects(imageSCR)
output = draw_bbox(imageSCR, box, label, count)

plt.imshow(output)
plt.show()

cell_phone = 0
car = 0

cell_phone = label.count('cell phone')
car = label.count('car')
sum_count = cell_phone + car

print("Total number of cars : " + str(sum_count))