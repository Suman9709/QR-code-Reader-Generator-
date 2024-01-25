import qrcode

features = qrcode.QRCode(version=1,box_size=30,border=2) #we can increment or decreent size of box and border
features.add_data('https://shivalikcollege.edu.in/')

features.make(fit=True)

generate_image = features.make_image(fill_color="black", back_color="white")

generate_image.save("qrcode.png")