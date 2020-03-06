# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:15:37 2020

@author: Intern
"""

import cv2


img=cv2.imread("monalisa.jpeg")

averaging=cv2.blur(img, (5, 5))

cv2.imshow("Original image", img)
cv2.imshow("Averaging", averaging)

cv2.waitKey(0)
cv2.destroyAllWindows()