import cv2
import time

def capture_image():
    # Initialize the camera
    camera = cv2.VideoCapture(0)  # Use 0 for the first camera device

    # Check if the camera is opened correctly
    if not camera.isOpened():
        print("Error: Couldn't open camera. Make sure it is connected and not being used by another application.")
        return

    print("Chess")  # Print "Chess" after the countdown

    # Capture 20 frames
    for i in range(20):
        ret, frame = camera.read()
        if not ret:
            print("Error: Couldn't capture image.")
            return
        if i == 19:  # Save the last frame
            cropped_zoomed_frame = crop_and_zoom(frame)
            cv2.imwrite('tmp/captured_image.jpg', cropped_zoomed_frame)
            print("Image captured successfully.")

    # Release the camera
    camera.release()

def crop_and_zoom(frame):
    # Get the dimensions of the image
    height, width = frame.shape[:2]

    # Define the size of the crop
    crop_size = 300

    # Calculate the center of the image
    center_x, center_y = width // 2, height // 2

    # Calculate the cropping box
    start_x = max(center_x - crop_size // 2, 0)
    start_y = max(center_y - crop_size // 2, 0)
    end_x = start_x + crop_size
    end_y = start_y + crop_size

    # Crop the image
    cropped_frame = frame[start_y:end_y, start_x:end_x]

    # Zoom the image by resizing it to 8x the crop size
    zoom_factor = 8
    zoomed_frame = cv2.resize(cropped_frame, (crop_size * zoom_factor, crop_size * zoom_factor), interpolation=cv2.INTER_LINEAR)

    return zoomed_frame

# Call the function to capture the image
capture_image()
