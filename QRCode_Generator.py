import qrcode
import os
from PIL import Image

def generate_qr_code(data, logo_path=None, qr_color="black", bg_color="white", error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4):
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=error_correction,  # Level of error correction (H = 30% correction)
        box_size=box_size,  # Size of each box in the QR code
        border=border  # Thickness of the border
    )

    qr.add_data(data)  
    qr.make(fit=True)

    img = qr.make_image(fill_color=qr_color, back_color=bg_color).convert('RGB')  
    if logo_path:
        logo = Image.open(logo_path)  # Load the logo
        logo_size = int(box_size * 3)  # Resize logo to fit in the center of the QR code
        logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)
        logo_position = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, logo_position, mask=logo.convert("RGBA"))  

    return img

def handle_data_and_generate_qr(data, logo_path=None):
    save_directory = "path_to_save_qr"  #
    
    if not os.path.exists(save_directory):
        os.makedirs(save_directory) 

    qr_code_img = generate_qr_code(data, logo_path, qr_color="black", bg_color="white")  

    name = input("Name of QR Code: ")  # Get the name of the QR code

    qr_code_img.save(os.path.join(save_directory, f"{name}.png"))  
    print(f"QR code generated and saved as {os.path.join(save_directory, f'{name}.png')}")

data = "ai"  
logo_path = None  # No logo
handle_data_and_generate_qr(data, logo_path)
