# Importing library
import qrcode

# Data to be encoded
data = 'https://www.phoneroster.com'

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('VMU2_phone_roster.png')
