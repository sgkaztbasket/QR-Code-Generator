import qrcode
import sys

def generate_qr(data, output_file="qrcode.png"):
    """
    Generates a QR code from the provided data and saves it as an image file.

    Parameters:
    - data: str, the text or URL to encode in the QR code.
    - output_file: str, optional, the filename for the output image.
    """
    qr = qrcode.QRCode(
        version=1,  # QR code version (1 = 21x21 matrix)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"QR code saved as {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_qr.py '<text or URL>' [output_file.png]")
        sys.exit(1)
    data = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "qrcode.png"
    generate_qr(data, output_file)
