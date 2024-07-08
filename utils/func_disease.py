from utils.func_colorPrediction import predict_closest_color


# Define a function to predict diseases based on urine color
def predict_disease_from_urine_color(rgb_tuple):
    color_to_disease = {
        "Clear": "Hidrasi normal",
        "Pale Yellow": "Hidrasi normal",
        "Transparent Yellow": "Hidrasi normal",
        "Dark Yellow": "Dehidrasi",
        "Amber or Honey": "Dehidrasi parah",
        "Dark Amber or Brown": "Penyakit hati",
        "Pink or Red": "Darah dalam urine (hematuria)",
        "Orange": "Kondisi hati atau saluran empedu",
        "Blue": "Kondisi medis yang mungkin (jarang)",
        "Green": "Kondisi medis yang mungkin (jarang)",
        "Foaming or Fizzy": "Kondisi medis yang mungkin (jarang)",
    }

    # Predict closest urine color based on RGB tuple
    predicted_color = predict_closest_color(rgb_tuple)

    # Convert predicted_color to regular string if it's numpy.str_
    predicted_color = str(predicted_color)

    # Lookup disease based on predicted color
    predicted_disease = color_to_disease.get(predicted_color, "Unknown")

    return predicted_color, predicted_disease


# Define a function to predict diseases based on urine pH value
def predict_disease_from_urine_ph(ph_value):
    # Example mappings (replace with actual disease mappings)
    ph_to_disease = {
        5.0: "Acidosis ringan",
        5.5: "Acidosis",
        6.0: "Normal",
        6.5: "Normal",
        7.0: "Normal",
        7.5: "Alkalosis",
        8.0: "Alkalosis",
        8.5: "Alkalosis ringan",
    }

    # Lookup disease based on pH value
    predicted_disease = ph_to_disease.get(ph_value, "Unknown")

    return predicted_disease


# Define a function to predict diseases based on both urine color (rgb_tuple) and pH value
def predict_disease_from_urine(rgb_tuple, ph_value):
    # Predict disease from urine color
    predicted_color, disease_from_color = predict_disease_from_urine_color(rgb_tuple)

    # Predict disease from urine pH
    disease_from_ph = predict_disease_from_urine_ph(ph_value)

    # Combine or choose one of the predictions based on your application logic
    # For example, here we choose to return the prediction from color if available, otherwise from pH
    if disease_from_color != "Unknown":
        return {
            "pH": ph_value,
            "name_color": predicted_color,
            "disease": disease_from_color,
        }
    else:
        return {"pH": ph_value, "name_color": "Unknown", "disease": disease_from_ph}
