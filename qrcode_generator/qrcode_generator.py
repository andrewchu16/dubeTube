import qrcode

def generate_qrcode(url: str, id: str):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(url)
    qr.make()



    img = qr.make_image(fill='black', back_color='white')
    img.save(f'static/qrcode{id}.png')
    return f'static/qrcode{id}.png'
