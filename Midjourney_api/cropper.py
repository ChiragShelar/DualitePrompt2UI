from PIL import Image
import os

def crop_images(file_paths, crop_size=1024):
    for input_path in file_paths:
        # Open the image file
        img = Image.open(input_path)

        # Crop the image from the top-left corner
        cropped_img = img.crop((0, 0, crop_size, crop_size))

        # Get the directory and filename from the input path
        directory, filename = os.path.split(input_path)

        # Construct the output path by joining the directory and filename
        output_path = os.path.join(directory, filename)

        # Save the cropped image
        cropped_img.save(output_path)

        print(f"Image cropped and saved to {output_path}")

