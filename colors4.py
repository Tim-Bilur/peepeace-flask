from skimage import io, color
from sklearn.cluster import KMeans
import numpy as np


def predict_urine_color_from_image(image_path):
    # Load the image
    image = io.imread(image_path)
    # Remove alpha channel if present
    if image.shape[-1] == 4:
        image = image[:, :, :3]
    # Convert the image to LAB color space
    lab_image = color.rgb2lab(image)
    # Reshape the image into a 2D array
    reshaped_image = lab_image.reshape((-1, 3))
    # Use KMeans clustering to find the dominant colors
    kmeans = KMeans(n_clusters=1)
    kmeans.fit(reshaped_image)
    dominant_color_lab = kmeans.cluster_centers_.squeeze()
    # Convert the dominant color back to RGB color space
    dominant_color_rgb = color.lab2rgb([[dominant_color_lab]])[0][0]
    # Convert RGB values to HEX format
    hex_color = "#{:02X}{:02X}{:02X}".format(
        int(dominant_color_rgb[0] * 255),
        int(dominant_color_rgb[1] * 255),
        int(dominant_color_rgb[2] * 255),
    )
    return hex_color


# Example usage
image_path = "./tmp/urine.jpg"
predicted_color = predict_urine_color_from_image(image_path)
print("Predicted urine color:", predicted_color)
