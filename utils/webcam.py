import cv2

# Initialize the camera
camera = cv2.VideoCapture(0)  # Use 0 for the first camera device

# Check if the camera is opened correctly
if not camera.isOpened():
    print("Error: Couldn't open camera. Make sure it is connected and not being used by another application.")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Define the codec (XVID is a widely supported codec)
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # Output file name, codec, frame rate, and resolution

while camera.isOpened():
    # Capture frame-by-frame
    ret, frame = camera.read()

    if ret:
        # Write the frame into the output video file
        out.write(frame)

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Check for the 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything when done
camera.release()
out.release()
cv2.destroyAllWindows()
