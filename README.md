# QR Code Generator

This Python script generates a QR code from a given URL or text string and saves it as an image file.

## Features

- Accepts any text or URL as input via command line.
- Outputs a QR code image (`.png` format) with customizable filename.
- Easy to use and lightweight.

## Requirements

- Python 3.x
- `qrcode` library (with Pillow for image support)

Install the required library with:
```bash
pip install qrcode[pil]
```

## Usage

1. Save the script as `generate_qr.py`.
2. Run it from the command line:

```bash
python generate_qr.py "https://example.com" my_qr.png
```

- The first argument is the text or URL to encode.
- The second argument (optional) is the output filename (defaults to `qrcode.png`).

## Example

```bash
python generate_qr.py "Hello, World!"
```
This creates a file named `qrcode.png` with the QR code for "Hello, World!".

## License

This project is licensed under the MIT License.
