from rembg import remove
from PIL import Image

input_image = Image.open("download.jpg")  # Load your image
output_image = remove(input_image)     # Remove background
output_image.save("download.png")        # Save the result