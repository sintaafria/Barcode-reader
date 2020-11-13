import numpy as np 
import cv2
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	
	barcode = decode(frame)
	for obj in barcode:
		qrcode = obj.data.decode('ascii')
		print(qrcode)

	for img in barcode:
		rect = img.rect
		cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height), (0, 225, 0), 2)
		cv2.putText(frame, qrcode, (rect.left, rect.top), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 225), 1)

	cv2.imshow("img", frame)
	key = cv2.waitKey(1)
	if key == 27:
		break

