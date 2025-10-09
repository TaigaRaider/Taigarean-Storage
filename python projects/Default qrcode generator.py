import qrcode

data = input(f"Enter text or URL ").strip()
reference = input(f"Enter filename and file extension ").strip()
img = qrcode.make(data)  #my name is tabitha can be replaced with another form of data e.g., a link,descriptive data for the qr-code etc.
type(img)  # qrcode.image.pil.PilImage
img.save(reference)

# 'my name is Tabitha.'