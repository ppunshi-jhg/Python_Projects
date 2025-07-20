import qrcode

class QrCodeGenerator:
    def __init__(self, size, padding):
        self.qr = qrcode.QRCode(box_size=size, border=padding)
        
    def qrcode_create(self, filename: str, fg: str, bg: str):
        data = input(f"Enter the data to encode in QR code: ")
        
        self.qr.add_data(data)
        self.qr.make(fit=True)
        img = self.qr.make_image(fill_color=fg, back_color=bg)
        img.save(filename)
        print(f"QR code saved as {filename}")
        

if __name__ == "__main__":
    qr_generator = QrCodeGenerator(size=30, padding=4)
    qr_generator.qrcode_create(filename="my_qr_code.png", fg="black", bg="white")