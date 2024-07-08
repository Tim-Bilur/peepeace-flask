from imagekitio import ImageKit
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions
import uuid
from utils.config import get_imgkit

# Get ImageKit configuration
private_key, public_key, url_endpoint = get_imgkit()

# Initialize ImageKit instance
imagekit = ImageKit(
    private_key=private_key,
    public_key=public_key,
    url_endpoint=url_endpoint,
)


def upload_image(image_path):
    # Generate a shorter UUID
    short_uuid = str(uuid.uuid4())[:5]  # Use the first 5 characters of the UUID

    # Append the original file extension to the UUID
    file_extension = image_path.split(".")[-1]
    random_file_name = f"urine_{short_uuid}.{file_extension}"

    try:
        # Upload file
        upload = imagekit.upload_file(
            file=open(image_path, "rb"),
            file_name=random_file_name,
            options=UploadFileRequestOptions(use_unique_file_name=False),
        )
        print("Upload successful:", upload)
        return upload  # Return the upload response if needed

    except Exception as e:
        print("An error occurred during upload:", e)
        return None
