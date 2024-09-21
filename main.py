import pyqrcode

url = input("QR kod oluşturulacak adresi giriniz: ")

qr_code = pyqrcode.create(url)
qr_code.svg('qrcode.svg', scale=8)