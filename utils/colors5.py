import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from PIL import Image

# Example dataset: depth (intensity) values mapped to RGB colors
depths = np.array([0, 1, 2, 3, 4, 5]).reshape(-1, 1)
hex_colors = ["#f0f8ff", "#f5deb3", "#faebd7", "#ffd700", "#daa520", "#8b4513"]


# Convert hex to RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


# Convert RGB to hex
def rgb_to_hex(rgb_color):
    return "#{:02x}{:02x}{:02x}".format(*rgb_color)


# Prepare RGB dataset
rgb_colors = np.array([hex_to_rgb(color) for color in hex_colors])

# Image Preprocessing


# Train a linear regression model for each RGB channel
models = []
for i in range(3):
    model = LinearRegression()
    model.fit(depths, rgb_colors[:, i])
    models.append(model)


# Function to predict hex color based on depth
def predict_color(depth):
    rgb_prediction = [int(model.predict([[depth]])[0]) for model in models]
    return rgb_to_hex(rgb_prediction)


# Function to load image and calculate average color
def load_image(image_path):
    image = Image.open(image_path)
    image = image.resize((100, 100))  # Resize for faster processing
    image_array = np.array(image)
    avg_color = image_array.mean(axis=(0, 1))  # Average color of the image
    return tuple(avg_color.astype(int))


# Function to map average color to a depth value (simplified assumption)
def color_to_depth(avg_color):
    # Normalize RGB values to a range that matches the depth values
    normalized_color = np.array(avg_color) / 255 * 5
    depth = normalized_color.mean()  # Simplified assumption: average intensity as depth
    return depth


# Load and process image
# image_path = "path/to/your/image.jpg"  # Replace with your image path
image_path = "./tmp/urine3.webp"
avg_color = load_image(image_path)
depth = color_to_depth(avg_color)
predicted_color = predict_color(depth)

print(f"Average color of the image: {avg_color}")
print(f"Predicted depth: {depth}")
print(f"Predicted hex color: {predicted_color}")
