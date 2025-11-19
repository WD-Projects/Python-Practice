import qrcode
def generate_qr():
    with open ("QR code generator/input.txt", "r") as file:
        lines = file.readlines()

    store_image = qrcode.make(lines[0])
    store_image.save(lines[1])

generate_qr()