
import numpy as np
import cv2

camera = cv2.VideoCapture(0)
return_value, image = camera.read()
cv2.imwrite('opencv'+'.jpg', image)
del(camera)
# Load the image
image = cv2.imread('opencv.jpg')

height, width = image.shape[:2]
orange_overlay = np.full((height, width, 3), (0, 165, 255), dtype=np.uint8)

orange = 0.5 #adjusted the opacity of the image to 0.5 of the
orange_filtered_image = cv2.addWeighted(image, 1 - orange, orange_overlay, orange, 0)

# Display the original and orange-filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Orange Filtered Image', orange_filtered_image)
cv2.imwrite('orange_filtered'+'.jpg', orange_filtered_image)
cv2.waitKey(0)
