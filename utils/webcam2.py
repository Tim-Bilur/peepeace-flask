import cv2
import time

# Initialize the camera
camera = cv2.VideoCapture(0)  # Use 0 for the first camera device

# Check if the camera is opened correctly
if not camera.isOpened():
    print("Error: Couldn't open camera. Make sure it is connected and not being used by another application.")
    exit()

# Countdown for 10 seconds
for i in range(10, 0, -1):
    print(f"Capturing in {i} seconds...")
    time.sleep(1)

print("Chess")  # Print "Chess" after the countdown

# Capture a frame
ret, frame = camera.read()

if ret:
    # Save the captured image
    cv2.imwrite('captured_image.jpg', frame)

    # Display the captured image
    cv2.imshow('Captured Image', frame)

    # Wait for a key press to close the window
    cv2.waitKey(0)
else:
    print("Error: Couldn't capture image.")

# Release the camera and close the window
camera.release()
cv2.destroyAllWindows()
