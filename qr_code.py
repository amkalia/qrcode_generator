from datetime import datetime
import os 

from PIL import Image 
import qrcode




input_data = input("Enter data for QRCode\n>")

# Create an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=12,
        border=5
)

qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

try:
        filename = "_"+str(len([name for name in os.listdir('qrcodes') if os.path.isfile(name)]))+"_"+datetime.today().strftime("%d-%m-%y")
        print(f"Created file : qrcodes/qrcode{filename}.png")
except FileNotFoundError:
        print("Image directory for QRCode not found. Creating...")
        os.mkdir("qrcodes")
        filename = "_"+str(len([name for name in os.listdir('qrcodes') if os.path.isfile(name)]))+"_"+datetime.today().strftime("%d-%m-%y")
        print(f"Created file : qrcodes/qrcode{filename}.png")


img.save(f'qrcodes/qrcode{filename}.png')
Image.open(f'qrcodes/qrcode{filename}.png').show()

