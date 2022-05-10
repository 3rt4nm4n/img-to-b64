import base64
from PIL import Image
import pyperclip #install this module for further use (console>pip install pyperclip)

sizex=sizey=150 #image width height
image = Image.open('targetimage.jpeg')
resizedimage=image.resize((sizex,sizey))#resizing image
resizedimage.save('resizedimage.jpeg') #saves resized image

with open("resizedimage.jpeg","rb") as img_file: #open image file
    base64_string = base64.b64encode(img_file.read()) #encoding image to base64 string
pyperclip.copy(base64_string.decode('utf-8'))  #decodes from bytes to string and copies to clipboard