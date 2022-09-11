import qrcode
data = 'website link'
img = qrcode.make(data)
img.save('phone_roster.png')
