from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import cv2

# Example dataset (RGB tuples and color names)
X_train = np.array(
    [
        [240, 255, 255],  # Clear
        [255, 255, 153],  # Pale Yellow
        [255, 255, 0],  # Transparent Yellow
        [255, 204, 0],  # Dark Yellow
        [255, 153, 0],  # Amber or Honey
        [153, 76, 0],  # Dark Amber or Brown
        [255, 0, 102],  # Pink or Red
        [255, 165, 0],  # Orange
        [0, 0, 255],  # Blue
        [0, 255, 0],  # Green
        [255, 255, 240],  # Foaming or Fizzy
    ]
)

y_train = np.array(
    [
        "Clear",
        "Pale Yellow",
        "Transparent Yellow",
        "Dark Yellow",
        "Amber or Honey",
        "Dark Amber or Brown",
        "Pink or Red",
        "Orange",
        "Blue",
        "Green",
        "Foaming or Fizzy",
    ]
)


def extract_rgb_from_image(image_path):
    # Load image
    image = cv2.imread(image_path)

    # Resize image (if needed)
    # image = cv2.resize(image, (width, height))

    # Convert image to RGB (OpenCV loads BGR by default)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate average RGB values
    avg_color_per_row = np.average(image_rgb, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)

    # Round and convert to integer
    avg_color = np.round(avg_color).astype(int)

    return avg_color


def predict_closest_color(rgb_tuple):
    # Initialize the KNN classifier
    knn = KNeighborsClassifier(n_neighbors=1)

    # Train the classifier
    knn.fit(X_train, y_train)

    # Predict the closest color for the given RGB tuple
    predicted_color = knn.predict([rgb_tuple])

    return predicted_color[0]
