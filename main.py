import pyqrcode
url=input("enter url to generate qr code: ")

qr_code = pyqrcode.create(url)
qr_code.png("qrcode.png", scale=8)
#1 qr_code.svg("qrcode.svg", scale=10)   QR Koda link vs eklemek için

#qr_code.eps("qrcode.eps", scale=2) Baskı ve matbaa işlerinde kullanılan .eps vektör formatında kaydeder.

print("QR kod başarıyla oluşturuldu")