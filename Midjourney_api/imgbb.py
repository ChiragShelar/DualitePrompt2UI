import requests
import base64

def upload_image_to_imgbb(api_key, image_path):
    # ImgBB API endpoint for image upload
    api_endpoint = "https://api.imgbb.com/1/upload"

    # Open the image file in binary mode
    with open(image_path, "rb") as file:
        # Prepare the payload for the API request
        payload = {
            "key": api_key,
            "image": base64.b64encode(file.read())
        }

        # Make the API request to upload the image
        response = requests.post(api_endpoint, data=payload)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response to get the image link
            image_link = response.json()["data"]["url"]
            return image_link
        else:
            print(f"Image upload failed. Status code: {response.status_code}")
            return None
