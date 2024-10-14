import pyqrcode

# enter a text for which you want to generate a QR code
text = input ("Enter the text to generate QR code: ")

# creating a pyqrcode object by calling the create() method
# we are using our text as an argument
qr_code = pyqrcode.create(text)

# calling the svg() method of the qr_code object
# creating the file named qr_code in svg format
# the scale argument determines the size of generated QR code
qr_code.svg ("qr_code.svg", scale = 8)