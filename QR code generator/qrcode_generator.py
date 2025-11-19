import qrcode
def generate_qr():
    with open ("QR code generator/input.txt", "r") as file:
        lines = file.readlines() #readlines() simply return an list like [https://www.youtube.com/?, youtube.png]

    store_image = qrcode.make(lines[0])
    store_image.save(lines[1])

generate_qr()