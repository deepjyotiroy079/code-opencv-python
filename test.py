import cv2
import numpy as np


# functions
def draw_circle(event, x, y, flags, params):
    # PRESSING THE LEFT MOUSE BUTTON
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), radius=40, color=(255, 0, 0), thickness=2)


# connecting cv2 with the functions and the window
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_circle)

# create an empty canvas and display the output
img = np.zeros((512, 512, 3))

while True:
    
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()