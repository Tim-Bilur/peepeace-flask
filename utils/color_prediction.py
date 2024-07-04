# import joblib
# from PIL import Image
# import numpy as np


# class UrineColorPredictor:
#     def __init__(self, model_path):
#         self.model = self.load_model(model_path)
#         self.depths = np.array([0, 1, 2, 3, 4, 5]).reshape(-1, 1)
#         self.hex_colors = [
#             "#f0f8ff",  # AliceBlue
#             "#f5deb3",  # Wheat
#             "#faebd7",  # AntiqueWhite
#             "#ffd700",  # Gold
#             "#daa520",  # GoldenRod
#             "#8b4513",  # SaddleBrown
#         ]
#         self.disease_mapping = {
#             "#f5deb3": "Dehidrasi",
#             "#f0f8ff": "Overdehidrasi",
#             "#faebd7": "Diabetes",
#             "#daa520": "Infeksi Saluran Kemih (ISK)",
#             "#8b4513": "Batu Ginjal",
#             "#8b4513": "Penyakit Hati",
#             "#faebd7": "Hematuria",
#             "#f5deb3": "Proteinuria",
#             "#daa520": "Asidosis Metabolik",
#             "#f0f8ff": "Alkalosis Metabolik",
#         }

#     def load_model(self, path):
#         return joblib.load(path)

#     def hex_to_rgb(self, hex_color):
#         hex_color = hex_color.lstrip("#")
#         return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

#     def rgb_to_hex(self, rgb_color):
#         return "#{:02x}{:02x}{:02x}".format(*rgb_color)

#     def predict_color(self, depth):
#         rgb_prediction = self.model.predict([[depth]])[0].astype(int)
#         return self.rgb_to_hex(rgb_prediction)

#     def load_image(self, image_path):
#         image = Image.open(image_path).convert(
#             "RGB"
#         )  # Convert to RGB to ignore alpha channel
#         image = image.resize((100, 100))  # Resize for faster processing
#         image_array = np.array(image)
#         avg_color = image_array.mean(axis=(0, 1))[
#             :3
#         ]  # Average color of the image, ignore alpha channel if present
#         return tuple(avg_color.astype(int))

#     def color_to_depth(self, avg_color):
#         # Normalize RGB values to a range that matches the depth values
#         normalized_color = np.array(avg_color) / 255 * 5
#         depth = (
#             normalized_color.mean()
#         )  # Simplified assumption: average intensity as depth
#         return depth

#     def predict(self, image_path):
#         avg_color = self.load_image(image_path)
#         depth = self.color_to_depth(avg_color)
#         predicted_color = self.predict_color(depth)
#         return predicted_color, avg_color, depth

#     def closest_color(self, hex_color):
#         rgb_color = self.hex_to_rgb(hex_color)
#         min_distance = float("inf")
#         closest_hex = None
#         for hex_code in self.disease_mapping.keys():
#             current_rgb = self.hex_to_rgb(hex_code)
#             distance = np.sqrt(
#                 sum((a - b) ** 2 for a, b in zip(rgb_color, current_rgb))
#             )
#             if distance < min_distance:
#                 min_distance = distance
#                 closest_hex = hex_code
#         return closest_hex

#     def predict_disease(self, hex_color, pH):
#         closest_hex = self.closest_color(hex_color)
#         disease = self.disease_mapping.get(
#             closest_hex, "No specific disease identified"
#         )
#         return disease


# # Example usage
# if __name__ == "__main__":
#     model_path = "model/predict_color.pkl"
#     predictor = UrineColorPredictor(model_path)
#     image_path = "tmp/urine.jpg"  # Replace with your image path
#     predicted_color, avg_color, depth = predictor.predict(image_path)
#     print(f"Average color of the image: {avg_color}")
#     print(f"Predicted depth: {depth}")
#     print(f"Predicted hex color: {predicted_color}")

#     # Dynamic pH value
#     pH = 5.6  # Replace with your actual pH value
#     disease_prediction = predictor.predict_disease(predicted_color, pH)
#     print(f"Disease prediction: {disease_prediction}")

##########################

import joblib
from PIL import Image
import numpy as np


class UrineColorPredictor:
    def __init__(self, model_path):
        self.model = self.load_model(model_path)
        self.depths = np.array([0, 1, 2, 3, 4, 5]).reshape(-1, 1)
        self.hex_colors = [
            "#f0f8ff",  # AliceBlue
            "#f5deb3",  # Wheat
            "#faebd7",  # AntiqueWhite
            "#ffd700",  # Gold
            "#daa520",  # GoldenRod
            "#8b4513",  # SaddleBrown
        ]
        self.disease_mapping = {
            "#f5deb3": ["Dehidrasi"],
            "#f0f8ff": ["Overdehidrasi"],
            "#faebd7": ["Diabetes", "Alkalosis Metabolik"],
            "#daa520": ["Infeksi Saluran Kemih (ISK)", "Asidosis Metabolik"],
            "#8b4513": ["Batu Ginjal", "Penyakit Hati"],
        }

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

    def closest_color(self, hex_color):
        rgb_color = self.hex_to_rgb(hex_color)
        min_distance = float("inf")
        closest_hex = None
        for hex_code in self.disease_mapping.keys():
            current_rgb = self.hex_to_rgb(hex_code)
            distance = np.sqrt(
                sum((a - b) ** 2 for a, b in zip(rgb_color, current_rgb))
            )
            if distance < min_distance:
                min_distance = distance
                closest_hex = hex_code
        return closest_hex

    def predict_disease(self, hex_color, pH):
        closest_hex = self.closest_color(hex_color)
        diseases = self.disease_mapping.get(
            closest_hex, ["No specific disease identified"]
        )

        # Adjust diseases based on pH value
        adjusted_diseases = []
        for disease in diseases:
            if pH < 5.5 and disease == "Overdehidrasi":
                adjusted_diseases.append("Dehidrasi")
            elif pH > 7.5 and disease == "Dehidrasi":
                adjusted_diseases.append("Overdehidrasi")
            else:
                adjusted_diseases.append(disease)

        return adjusted_diseases


if __name__ == "__main__":
    model_path = "model/predict_color.pkl"
    predictor = UrineColorPredictor(model_path)
    image_path = "tmp/urine.jpg"  # Replace with your image path
    predicted_color, avg_color, depth = predictor.predict(image_path)
    print(f"Predicted hex color: {predicted_color}")

    # Dynamic pH value
    pH = 5.0  # Replace with your actual pH value
    disease_prediction = predictor.predict_disease(predicted_color, pH)

    # Example when the client gets "Dehidrasi"
    if disease_prediction == "Dehidrasi":
        print("Client got Dehidrasi.")
    else:
        print(f"Client got {disease_prediction}.")
