import qrcode

def generate_qrcode(url):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(url)
    qr.make()



    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode_generator/qrcode.png')

generate_qrcode("google.com")