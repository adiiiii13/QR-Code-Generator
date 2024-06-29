# QR Code Generator

This repository contains a simple Python script for generating QR codes using the `qrcode` library. The script can be used to create QR codes for URLs, text, or any other data.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This project demonstrates how to generate a QR code using Python. The script allows you to encode any data, such as URLs or text, into a QR code image. This can be useful for sharing information easily and efficiently.

## Features

- Generate QR codes for URLs, text, or any data
- Customize the size and border of the QR code
- Save the generated QR code as an image file

## Technologies Used

- **Python**: Programming language
- **qrcode**: Library for generating QR codes
- **Pillow (PIL)**: Library for image processing

## Installation

To get a local copy up and running, follow these steps:

1. **Clone the repository**:

   ```sh
   git clone https://github.com/adiiiii13/QR-Code-Generator.git
   ```

2. **Navigate to the project directory**:

   ```sh
   cd QR-Code-Generator
   ```

3. **Install the required libraries**:

   ```sh
   pip install qrcode[pil]
   ```

## Usage

1. Open the `generate_qr.py` file in your preferred text editor.

2. Modify the `data` variable to the URL or text you want to encode in the QR code.

   ```python
   data = "https://www.instagram.com/adiiiii.__/"
   ```

3. Run the script:

   ```sh
   python generate_qr.py
   ```

4. The generated QR code will be saved as `test.png` in the project directory.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request or open an issue.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Aditya - aditya04slg@gmail.com

Project Link: [https://github.com/adiiiii13/QR-Code-Generator](https://github.com/adiiiii13/QR-Code-Generator)

---

Feel free to customize this template according to your project's specifics and personal preferences.
