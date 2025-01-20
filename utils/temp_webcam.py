import cv2

# Initialize camera
camera = cv2.VideoCapture(0, cv2.CAP_V4L2)

if not camera.isOpened():
    print("Error: Couldn't open camera.")
else:
    print("Camera opened successfully.")
    
    while True:
        # Capture frame-by-frame
        ret, frame = camera.read()
        if not ret:
            print("Error: Couldn't capture frame.")
            break

        # Display the resulting frame
        cv2.imshow("Real-time Capture", frame)

        # Wait for key press
        key = cv2.waitKey(1) & 0xFF  # Wait for 1ms and capture key press
        if key == ord('q'):  # Exit if 'q' is pressed
            print("Exiting real-time capture.")
            break
        elif key == ord('s'):  # Save frame if 's' is pressed
            cv2.imwrite('captured_image.jpg', frame)
            print("Image saved as 'captured_image.jpg'")

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
