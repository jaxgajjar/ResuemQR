import qrcode


resume_url = "https://jaxgajjar.github.io/ResuemQR/"
img = qrcode.make(resume_url)
img.save("resume_qr.png")
print("QR code for resume generated and saved as 'resume_qr.png'.")