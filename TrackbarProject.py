import numpy as np
import cv2

def nothing():
    pass

cv2.namedWindow("image")
cv2.createTrackbar("Threshold","image",0,255,nothing)
cv2.createTrackbar("GaussianBlur","image",0,13,nothing)
cv2.createTrackbar("Canny1","image",0,13,nothing)
cv2.createTrackbar("Canny2","image",0,13,nothing)
cv2.createTrackbar("Erode","image",0,13,nothing)
cv2.createTrackbar("Switch","image",0,4,nothing)
print("press 0 ->thresh"
      "press 1-> gaussian blur"
      "press 2-> canny"
      "press 3-> erode"
      "press 4-> blue mask")

cap= cv2.VideoCapture(0)

def _thresh(frame,value):
    ret, thresh_img = cv2.threshold(frame, thresh=value, maxval=255, type=cv2.THRESH_BINARY)
    return thresh_img
def _gaussianblur(frame,value):
    gb = cv2.GaussianBlur(frame, ksize=(21,21), sigmaX=value)
    return gb
def _canny(frame,value1,value2):
    edges = cv2.Canny(image=frame, threshold1=value1, threshold2=value2)
    return edges
def _erode(frame,value):
    kernel = np.ones((3, 3), dtype=np.uint8)
    result = cv2.erode(frame, kernel, iterations=value)
    return result
def _bluemask(frame):
    mask = cv2.inRange(cv2.cvtColor(frame,cv2.COLOR_BGR2HSV), (85,90,0), (170,255,255))
    return mask


while True:
    success, frame= cap.read(0)
    global nimg;
    if success:
        t=cv2.getTrackbarPos("Threshold", "image")
        g = cv2.getTrackbarPos("GaussianBlur", "image")
        c = cv2.getTrackbarPos("Canny1", "image")
        c2 = cv2.getTrackbarPos("Canny2", "image")
        e = cv2.getTrackbarPos("Erode", "image")
        s = cv2.getTrackbarPos("Switch", "image")
        if cv2.waitKey(1) & 0xFF== ord('q'):
            break
        elif s==0:
            nimg=_thresh(frame,t)
        elif s == 1:
            nimg = _gaussianblur(frame, g)
        elif s==2:
            nimg=_canny(frame,c,c2)
        elif s==3:
            nimg=_erode(frame,e)
        elif s==4:
            nimg=_bluemask(frame)
    cv2.imshow("image",nimg)

cap.release()
cv2.destroyAllWindows()