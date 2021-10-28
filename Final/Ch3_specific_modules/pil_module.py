# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image  # pip3 install Pillow
import os


for f in os.listdir("./images"):
    if f.endswith(".png"):
        img = Image.open(f"./images/{f}")
        try:
            img.save(f"./images/jpg/{f[:-4]}.jpg")
        except Exception as e:
            print(e)


img1 = Image.open("images/astronaut.png")
img1.thumbnail((128, 128))
img1.save("./images/a.ico")


