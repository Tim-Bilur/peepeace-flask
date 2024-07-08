from utils.func_colorPrediction import extract_rgb_from_image
from utils.func_disease import predict_disease_from_urine
from utils.func_imgkit import upload_image


def main():
    image_path = "tmp/test5.png"  # Replace with your image path

    # Extract RGB values from the image
    rgb_value = extract_rgb_from_image(image_path)

    # pH value input (example)
    ph_value = 7.0

    # Predict disease based on urine color and pH
    result = predict_disease_from_urine(rgb_value, ph_value)

    upload_result = upload_image(image_path)
    if upload_result:
        print("Upload result:", upload_result)

    print(result)


if __name__ == "__main__":
    main()
