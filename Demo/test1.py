'''
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("E:\\CV\\wing\\wing.jpg",cv2.IMREAD_COLOR)
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.imshow(img)
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()
'''
'''
import numpy as np
import cv2

img = cv2.imread("E:\\CV\\wing\\wing.jpg",cv2.IMREAD_COLOR)
cv2.imshow('image',img)
k = cv2.waitKey(1000)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('S'):
    cv2.imwrite("E:\\CV\\wing\\wing.png", img)
    cv2.destroyAllWindows()
'''
'''
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
h = cap.get(3)
w = cap.get(4)
while(True):
  ret, frame = cap.read()
  
  gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY)
  
  cv2.imshow('frame',gray)
  if cv2.waitKey(1)&oxff == ord('Q'):
    break
  
cap.release()
cv2.destroyAllWindows()
'''
'''
import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)
#cv2.imshow("aaa",img)
#cv2.waitKey(1000)
img = cv2.line(img, (0,0), (511,511), (255,0,0),5)
#cv2.imshow("aaa",img)
#cv2.waitKey(1000)
img = cv2.rectangle(img, (384,0), (510,128), (0,255,0),3)
img = cv2.circle(img, (447,63), 63, (0,0,255),-1)
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV", (10,500), font, 4, (255,255,255), 2,cv2.LINE_AA)
cv2.imshow("aaa",img)
cv2.waitKey(1000)
'''
'''
import cv2
events = [i for i in dir(cv2) if 'EVENT' in i]
print events
'''
'''
import cv2
import numpy as np
def draw_circle(event,x,y,falgs,param):
    if event == cv2.EVENT_MBUTTONDBLCLK:
        cv2.circle(img, (x,y), 100, (255,255,255),-1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

cv2.imshow('image',img)
while(True):
    if cv2.waitKey(20) & 0xff == 27:
        break
    
cv2.destroyAllWindows()
'''
"""
import cv2
import numpy as np

drawing = True
mode = True
ix,iy = -1,-1

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)

img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(True):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xff
    if k == ord('M'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()
"""
"""
import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

switch = '0:off \n1 :on'
cv2.createTrackbar(switch,'image',0,1,nothing)

while(True):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) &0xff
    if k == 27:
        break
    
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')
    
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()
"""
import cv2
import numpy as np

img = cv2.imread("E:\\CV\\wing\\wing.jpg")
lei = img[280:340,330:390]
img[273:333,100:160] = lei
#px = img[100,100]
#print img.item(100,100,2)
#print img.dtype
cv2.imshow('lei',img)
cv2.waitKey(10000)