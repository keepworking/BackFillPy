from PIL import Image , ImageDraw , ImageFilter
import Tkinter as tk
import math

root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

del root

wallpaper = Image.new(size = (width,height), color="white",mode="RGB")

img = Image.open("target.jpg")

x, y = img.size


if float(height)/float(width) >= float(y)/float(x) :
    zoomf = float(width)/float(x)
    zoomb = float(height)/float(y)
else:
    zoomf = float(height)/float(y)
    zoomb = float(width)/float(x)

front = img.resize((int(x*zoomf),int(y*zoomf)), Image.ANTIALIAS)
back = img.resize((int(x*zoomb),int(y*zoomb)), Image.ANTIALIAS)

back = back.filter(ImageFilter.GaussianBlur(10))

wallpaper.paste(back,(width/2-back.size[0]/2,height/2-back.size[1]/2))
wallpaper.paste(front,(width/2-front.size[0]/2,height/2-front.size[1]/2))

#wallpaper.show()

wallpaper.save("export.png","PNG")

#front = img.resize()
