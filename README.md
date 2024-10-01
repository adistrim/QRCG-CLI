# QR Code Generator CLI

This is a Python-based CLI tool for generating QR codes with optional logos, which can be installed and used to generate QR codes directly from the command line.

## Features

- Generates QR codes from provided data (URL, text, etc.).
- Optionally add a logo or icon to the center of the QR code.
- Automatically saves the generated QR code to the `Downloads` folder.

## Complete Installation Steps

Here’s a complete step-by-step guide to install and use the tool:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/adistrim/QRCG-CLI.git
   cd QRCG-CLI
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # OR
   .\.venv\Scripts\activate   # On Windows
   ```

3. **Install the project locally**:
   ```bash
   pip install .                # pip3 or pip depending on your setup
   ```

4. **Run the CLI tool**:
   You can now run the CLI tool from the terminal:
   ```bash
   qr_code_generator --data "https://example.com" --logo "/path/to/logo.png"
   ```

## Usage

Once installed, you can generate a QR code by running the following command:

```bash
qr_code_generator --data "https://example.com" --logo "/path/to/logo.png"
```

- `--data` (required): The data for the QR code (e.g., a URL or text).
- `--logo` (optional): Path to a logo image to place in the center of the QR code.

The generated QR code will be saved to the `Downloads` folder as `qr.png`.

### Example:

To generate a QR code with the URL `https://sabrang.jklu.edu.in` and an optional logo:

```bash
qr_code_generator --data "https://sabrang.jklu.edu.in" --logo "./sabrang.png"
```

If no logo is provided, the tool will still generate a QR code with just the data.

## Contact | Getting Help

For questions or support mail me at [adistrim.dev@gmail.com](mailto:adistrim.dev@gmail.com) or please file an issue in this repository's Issue Tracker.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
