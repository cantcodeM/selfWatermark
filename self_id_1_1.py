"""
Marchal Tony
v1.1
01/11/2022
"""
import os
from tkinter import image_names
from PIL import Image
import glob

os.mkdir('images')

logo = Image.open('self.png').convert('RGBA')
signature = Image.open('signature.png').resize((200,200), Image.LANCZOS)
photos = glob.glob('photos/*.jpg')

for i in photos :
    path = i.split('\\')[-1]
    img = Image.open(i)
    img.paste(logo,(825,1000),logo)
    img.paste(signature,(1700,860),signature)
    img.save("images/%s" % path, "JPEG")

