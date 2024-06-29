import qrcode
import image

# Create a QRCode object
qr = qrcode.QRCode(
    version=15,  # 15 means the version of the QR code. Higher the number, the bigger and more complicated the QR code image.
    box_size=10,  # Size of the box where the QR code will be displayed.
    border=5  # Border size in all 4 sides with white color.
)

# Data to be encoded in the QR code
data = "https://www.instagram.com/adiiiii.__/"

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill="black", back_color="white")

# Save the image
img.save("test.png")
