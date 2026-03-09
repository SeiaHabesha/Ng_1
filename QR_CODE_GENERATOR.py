
import qrcode
from IPython.display import display

# የሜኑ ዝርዝር
data = """
   _-_-_-_-_-_-_-_
      TODAY MENU
   _-_-_-_-_-_-_-_
   FOOD LIST     PRICE
   Doro Wet:     250 ETB
   Injera:        40 ETB
   Rice:          50 ETB
   Beans:         20 ETB
   Milk:          20 ETB
   Meat:         200 ETB
   Egg:           10 ETB
   _-_-_-_-_-_-_-_
   ENJOY YOUR MEAL!!
   -_-_-_-_-_-_-_-
"""

qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
display(img)

img.save("Restaurant_Menu_QR.png")
