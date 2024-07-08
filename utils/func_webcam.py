import cv2
import time

def capture_image():
    # Initialize the camera
    camera = cv2.VideoCapture(0)  # Use 0 for the first camera device

    # Check if the camera is opened correctly
    if not camera.isOpened():
        print("Error: Couldn't open camera. Make sure it is connected and not being used by another application.")
        return

    # Countdown for 5 seconds
    for i in range(5, 0, -1):
        print(f"Capturing in {i} seconds...")
        time.sleep(1)

    print("Chess")  # Print "Chess" after the countdown

    # Capture a frame
    ret, frame = camera.read()

    if ret:
        # Save the captured image
        cv2.imwrite('tmp/captured_image.jpg', frame)
        print("Image captured successfully.")

    else:
        print("Error: Couldn't capture image.")

    # Release the camera
    camera.release()
