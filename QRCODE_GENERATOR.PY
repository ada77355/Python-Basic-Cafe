import qrcode
img=qrcode.make("HI I AM ADARSH")
img.save("qrcode.png")
print("QR Code generated and saved as qrcode.png")