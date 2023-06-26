import cv2 

image = cv2.imread("solar-system.jpg")
cv2.putText(image,
            "SUN",
            (58,151),
            cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color=(255,255,255))
cv2.putText(image,
            "Mercury",
            (199,131),
            cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color=(255,255,255))

cv2.putText(image,
            " Venus,",
            (130,133),
            cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color=(255,255,255))

cv2.putText(image,
            "EARTH",
            (278,133),
            cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color=(255,255,255))

cv2.putText(image,
            "mars,",
            (400,123),
            cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color=(255,255,255))

cv2.putText(image,
            "Jupiter,",
            (600,123),
            cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color=(255,255,255))

cv2.putText(image,
            " Saturn,",
            (750,180),
            cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color=(255,255,255))

cv2.putText(image,
            "Uranus,",
            (940,161),
            cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color=(255,255,255))

cv2.putText(image,
            "Neptune",
            (1100,150),
            cv2.FONT_HERSHEY_COMPLEX,
            fontScale= 0.5,
            color=(255,255,255))




cv2.imshow("output",image)
cv2.waitKey(0)




