import cv2
import numpy as np

# global variables
drawing = False # this will become true when mouse is pressed down and false while mouse button is up.
ix = -1
iy = -1
font = cv2.FONT_HERSHEY_SIMPLEX
# functions
def draw_rectangle(event, x, y, flags, params):
    global drawing, ix, iy # these are global variables
    
    if event == cv2.EVENT_LBUTTONDOWN: # you have started drawing the rectangle
        """ THIS IS THE POINT WHERE WE STARTED DRAWING THE RECTANGLE """
        drawing = True # setting the drawing variable to true
        ix, iy = x, y # tracking the current mouse position in the global space
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            # ix, iy are the points where we have clicked the left mouse button
            # x,y are the current mouse position
            cv2.rectangle(img, (ix, iy), (x,y), color=(255, 0, 0), thickness=-1)
            print(x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        
        # STOP DRAWING
        drawing = False
        
        # finish the rectangle 
        cv2.rectangle(img, (ix, iy), (x,y), color=(255, 0, 0), thickness=-1)
        print(x, y)
        
        
# connecting cv2 through named window
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_rectangle)

# creating the blank screen
# img = np.zeros((512, 512, 3))
img = cv2.imread('Images/public_place.jpg')
img = cv2.resize(img, (1000, 500))

while True:
    cv2.imshow('Image', img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
