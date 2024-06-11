import cv2
import subprocess

# Run libcamera-still command to capture an image
subprocess.run(['libcamera-still', '-o', 'image.jpg'])

# Read the captured image using OpenCV
image = cv2.imread('image.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Couldn't read the captured image.")
    exit()

# Display the captured image
cv2.imshow('Captured Image', image)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
