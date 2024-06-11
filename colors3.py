import cv2
import numpy as np


def predict_urine_color_from_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Calculate the histogram of the hue channel
    hist = cv2.calcHist([hsv_image], [0], None, [180], [0, 180])
    # Get the dominant color (hue) value
    dominant_hue = np.argmax(hist)
    # Map the dominant hue value to the corresponding HEX color
    hex_color = "#{:02X}{:02X}{:02X}".format(int(dominant_hue), 255, 255)
    return hex_color


image_path = "./tmp/urine3.webp"
predicted_color = predict_urine_color_from_image(image_path)
print("Predicted urine color:", predicted_color)
