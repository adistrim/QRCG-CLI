import argparse
import os
from pathlib import Path
import qrcode
from PIL import Image

def create_qr(data, logo_path, output_path):
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    if logo_path:
        logo = Image.open(logo_path).convert("RGBA")

        logo_size = qr_image.size[0] // 4
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

        mask = logo.split()[3]

        black_logo = Image.new("RGB", logo.size, "black")

        white_square_size = int(logo_size * 1.3)
        white_square = Image.new("RGB", (white_square_size, white_square_size), "white")

        square_position = ((qr_image.size[0] - white_square_size) // 2, 
                           (qr_image.size[1] - white_square_size) // 2)

        qr_image.paste(white_square, square_position)

        logo_position = ((qr_image.size[0] - logo_size) // 2, 
                         (qr_image.size[1] - logo_size) // 2)

        qr_image.paste(black_logo, logo_position, mask)

    qr_image.save(output_path)

def main():
    parser = argparse.ArgumentParser(description="Generate a QR code with an optional logo.")
    parser.add_argument("--data", type=str, required=True, help="The data for the QR code.")
    parser.add_argument("--logo", type=str, required=False, help="Path to the logo image (optional).")

    args = parser.parse_args()

    downloads_path = str(Path.home() / "Downloads")
    output_path = os.path.join(downloads_path, "qr.png")

    create_qr(args.data, args.logo, output_path)

    print(f"QR code saved to {output_path}")

if __name__ == "__main__":
    main()
