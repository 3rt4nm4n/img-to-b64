import base64
import os
from PIL import Image
# install this module for further use (console>pip install pyperclip)
import pyperclip 

# ---------------------------------SECTION I--------------------------------- #

# get the image from the user
fpath=input("Paste the complete path of the image:")
image = Image.open(fpath)

# ---------------------------------SECTION II-------------------------------- #

# get image width&height in pixel, image is considered to be in 1:1 ratio

sizex=sizey=input("Type the size for the image (Enter for default 150px):")  
if not sizex and not sizey:
    # if size is empty pass 150 as default sizes into the resize function
    resizedimage=image.resize((150,150))
else:
    # if size is not empty, pass the value to the resize function
    resizedimage=image.resize((int(sizex),int(sizey)))
    
# --------------------------------SECTION III-------------------------------- #

# split filename and extension name
head,tail=os.path.splitext(fpath)
# save resized image
resizedimage.save(head+"_resized.jpeg") 

# ---------------------------------SECTION IV-------------------------------- #

# open image file
with open(os.path.basename(fpath)+"resized.jpeg","rb") as img_file:
    #   encode image to base64 string
    base64_string = base64.b64encode(img_file.read())
    
# --------------------------------SECTION V---------------------------------- #

# decode from bytes to string and copy to clipboard
pyperclip.copy(base64_string.decode('utf-8'))  
