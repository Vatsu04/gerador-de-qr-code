import qrcode as qr


url = input("Enter the URL to encode in the QR code: ")

qr = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


qr.add_data(url)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")

file_name = input("Enter the filename to save the QR code (e.g., my_qrcode.png): ")

if not file_name:
    file_name = "my_qrcode.png"
elif not file_name.endswith('.png'):
    file_name += '.png'
elif file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
    print("Warning: JPEG format may not support transparency well. Consider using PNG format.")


img.save(file_name)


print("QR code generated and saved as my_qrcode.png")