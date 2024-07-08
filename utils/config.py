from dotenv import dotenv_values


def get_firebase():
    config = dotenv_values(".env")
    firebase_url = config.get("FIREBASE_URL")

    return firebase_url


def get_imgkit():
    config = dotenv_values(".env")

    private_key = config.get("IMG_KIT_PRIVATE_KEY")
    public_key = config.get("IMG_KIT_PUBLIC_KEY")
    url_endpoint = config.get("IMG_KIT_URL_ENDPOINT")

    return private_key, public_key, url_endpoint
