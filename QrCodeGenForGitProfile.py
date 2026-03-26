#Simple QR code generation

import qrcode as qr
img = qr.make("https://github.com/1a1anMandal")
img.save("MySimpGitQR.png")

#Customize QR code generation

import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_H, 
    box_size=10, 
    border=10,
)

qr.add_data("https://github.com/1a1anMandal")
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")

img.save("MyCustmGitQR.png")