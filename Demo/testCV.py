"""
from PIL import Image
from pylab import *

im = array(Image.open('wing.jpg'))
imshow(im)

x = [100,200,400,400]
y = [100,200,200,500]

plot(x,y,'r*')
plot(x[:2],y[:2],'w')

title('plotting:"wing.jpg"')
axis('off')
show()
"""
"""
from PIL import Image
from pylab import *

im = array(Image.open('wing.jpg').convert('L'))
figure()
gray()
contour(im,origin='image')
axis('equal')
figure()
hist(im.flatten(),128)
show()
"""
"""
from PIL import Image
from pylab import *

im = array(Image.open('wing.jpg'))
imshow(im)

print 'please click 3 points'
x = ginput(3)
print 'you clicked :',x
show()
"""
import cv2
im = cv2.imread('wing.jpg')
h,w = im.shape[:-1]
print h,w

#cv2.imwrite('')