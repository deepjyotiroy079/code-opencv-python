import cv2
import numpy as np

# variables
drawing = False
ix = -1
iy = -1

# functions
def draw_rectangle(event, x, y, flags, params):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        # mouse is pressed
        # set drawing to true
        drawing = True
        # storing the current mouse position to the global space
        ix, iy = x, y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        # check if we are still drawing
        if drawing:
            # create a rectangle with one point as the global space and other with the current mouse position
            cv2.rectangle(img, (ix, iy), (x, y), color=(255, 0, 0), thickness = -1)
            
    elif event == cv2.EVENT_LBUTTONUP:
        
        # if you have lifted the left mouse button then stop drawing
        drawing = False
        
        # complete the rectangle
        cv2.rectangle(img, (ix, iy), (x, y), color=(255, 0, 0), thickness = -1)
        

# connect the function to cv2 and window
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_rectangle)

# display

img = np.zeros((512, 512, 3))

while True:
    cv2.imshow('Image', img)
    
    if cv2.waitKey(1) or 0xFF == 27:
        break
        
        
cv2.destroyAllWindows()