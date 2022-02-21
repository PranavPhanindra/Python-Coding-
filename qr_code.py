import pyqrcode
#this has features to create the qrcode

def qr_code():
    s = 'This is Power python class'
    #We would use this string and convert this into qrcode

    c = pyqrcode.create(s)
    #
    c.png('my_img.png',scale = 6)
    print('Code Execute')

if __name__ == '__main__' :
    qr_code()
