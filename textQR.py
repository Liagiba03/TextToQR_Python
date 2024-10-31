import qrcode

#TEXTO
text = "Texto para convertir"

qr = qrcode.QRCode(version=1,
                   box_size=10, #Tamaño del qr
                   border = 2)

qr.add_data(text)

qr.make(fit = True)

#Generate the QR image
image_qr = qr.make_image(fill_color = "black",
                         back_color = "white")

image_qr.save("codigoQR.png")