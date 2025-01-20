import qrcode
async def send_qrcode(user):
    img = qrcode.make(user)
    img.save("38.png")