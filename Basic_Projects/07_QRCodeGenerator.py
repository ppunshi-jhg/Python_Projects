import qrcode

class MyQR:
    def __init__(self, size, padding):
        self.qr = qrcode.QRCode(box_size = size, border = padding)
    
    def create_qr(self, filename:str, fg: str, bg:str):
        data = input(f"Enter the data to encode in QR code: ")
        
        try:
            self.qr.add_data(data)
            self.qr.make(fit= True)
            img = self.qr.make_image(fill_color = fg, back_color = bg)
            img.save(filename)
            print(f"QR code saved as {filename}")
        except Exception as e:
            print(f"An error occured: {e}")

def main():
    myqr = MyQR(size = 30, padding = 4)
    myqr.create_qr(filename = "my_qr_code.png", fg = "black", bg = "white")

if __name__ == "__main__":
    main()