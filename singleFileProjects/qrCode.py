import pyqrcode
from pyzbar import decode
from PIL import Image

qr = pyqrcode.create("Learn Python codeing ? ")
qr.png("qrImg.png", scale=8)

d=decode(Image.open("qrImg.png"))

print(d)

print(d[0].data.decode("ascii"))







"""
# Another Way
import qrCode
img = qrCode.make(input("What is qr code ?"))
img.save('saved.png')
img.show('saved.png')

"""


