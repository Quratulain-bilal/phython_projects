import qrcode

# Apni website ka link do
website_link = "https://www.instagram.com/sas_here7?igsh=M2xvcWhkMWR3YjM3"

# QR Code generate karo
qr = qrcode.make(website_link)

# QR Code save karo
qr.save("website_qr.png")

print("QR Code saved as website_qr.png")

