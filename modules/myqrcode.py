import qrcode

data = qrcode.make("www.youtube.com")

type(data)

data.save("new_qr.png")

print("qrcode created")


# import qrcode
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data('Some data')
# qr.make(fit=True)

# img = qr.make_image(fill_color="red", back_color="white")
# img.save("my_qr.png")