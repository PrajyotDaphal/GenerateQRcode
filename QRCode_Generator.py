import qrcode
import pickle
import os
from PIL import Image

# Load address data from JSON file
with open("E:\\Projects\\Python\\Advanced Voice Assistant\\Data\\pickle\\Address.pkl", 'rb') as R:
    address = pickle.load(R)

# Extract the directory path from the address [pkl]
qr_save_path = address['QRCode']  # This should be the path where you want to save the QR code

# Function to generate a customized QR code
def generate_qr_code(data, logo_path=None, qr_color="black", bg_color="white", error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4):
    # Set the error correction level and other parameters
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=error_correction,  # Level of error correction (H = 30% correction)
        box_size=box_size,  # Size of each box in the QR code
        border=border  # Thickness of the border
    )

    # Add the data (text or URL)
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the QR code image with specified colors
    img = qr.make_image(fill_color=qr_color, back_color=bg_color).convert('RGB')

    # If a logo is provided, embed it in the center of the QR code
    if logo_path:
        logo = Image.open(logo_path)

        # Resize logo to fit in the center of the QR code
        logo_size = int(box_size * 3)  # Adjust the size of the logo (3 boxes by default)
        logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)

        # Calculate the position to place the logo
        logo_position = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)

        # Paste the logo onto the QR code
        img.paste(logo, logo_position, mask=logo.convert("RGBA"))  # Use transparency (RGBA)

    return img

# Save file data (if applicable) and generate QR code
def handle_data_and_generate_qr(data, save_directory, logo_path=None):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)  # Create the directory if it doesn't exist

    # Generate the QR code with the provided data
    qr_code_img = generate_qr_code(data, logo_path, qr_color="black", bg_color="white")

    # Get the name for the QR code image from user input
    name = input("Name of QR Code: ")

    # Save the final QR code as an image file in the specified directory
    qr_code_img.save(os.path.join(save_directory, f"{name}.png"))
    print(f"QR code generated and saved as {os.path.join(save_directory, f'{name}.png')}")

# Example usage with data and saving the QR code to the path from the JSON
data = "ai"  # Replace this with any file path or URL
logo_path = None  # Path to your logo (set None if no logo)
handle_data_and_generate_qr(data, qr_save_path, logo_path)
