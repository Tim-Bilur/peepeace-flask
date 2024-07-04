import joblib
from PIL import Image
import numpy as np


class UrineColorPredictor:
    def __init__(self, model_path):
        self.model = self.load_model(model_path)
        self.depths = np.array([0, 1, 2, 3, 4, 5]).reshape(-1, 1)
        self.hex_colors = [
            "#f0f8ff",
            "#f5deb3",
            "#faebd7",
            "#ffd700",
            "#daa520",
            "#8b4513",
        ]

    def load_model(self, path):
        return joblib.load(path)

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

    def rgb_to_hex(self, rgb_color):
        return "#{:02x}{:02x}{:02x}".format(*rgb_color)

    def predict_color(self, depth):
        rgb_prediction = self.model.predict([[depth]])[0].astype(int)
        return self.rgb_to_hex(rgb_prediction)

    def load_image(self, image_path):
        image = Image.open(image_path).convert(
            "RGB"
        )  # Convert to RGB to ignore alpha channel
        image = image.resize((100, 100))  # Resize for faster processing
        image_array = np.array(image)
        avg_color = image_array.mean(axis=(0, 1))[
            :3
        ]  # Average color of the image, ignore alpha channel if present
        return tuple(avg_color.astype(int))

    def color_to_depth(self, avg_color):
        # Normalize RGB values to a range that matches the depth values
        normalized_color = np.array(avg_color) / 255 * 5
        depth = (
            normalized_color.mean()
        )  # Simplified assumption: average intensity as depth
        return depth

    def predict(self, image_path):
        avg_color = self.load_image(image_path)
        depth = self.color_to_depth(avg_color)
        predicted_color = self.predict_color(depth)
        return predicted_color, avg_color, depth


# Example usage
if __name__ == "__main__":
    model_path = "model/predict_color.pkl"
    predictor = UrineColorPredictor(model_path)
    image_path = "tmp/urine2.png"  # Replace with your image path
    predicted_color, avg_color, depth = predictor.predict(image_path)
    print(f"Average color of the image: {avg_color}")
    print(f"Predicted depth: {depth}")
    print(f"Predicted hex color: {predicted_color}")
