import pyqrcode
import cv2
from pyzbar.pyzbar import decode


# generate qrcode
qr = pyqrcode.create('code')
qr.png('file_name.png', scale = 8)

frame = cv2.imread('gen1.png')
barcode = decode(frame)
print(barcode)
for obj in barcode:
	qrcode = obj.data.decode('ascii')
	print(qrcode)