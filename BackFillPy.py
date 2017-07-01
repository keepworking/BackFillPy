from PIL import Image , ImageFilter, ImageDraw

img = Image.open("target.jpg")

img = img.filter(ImageFilter.GaussianBlur(radius=30))

img = img.rotate(-90,expand=True)

draw = ImageDraw.Draw(img)

draw.line((0,0)+ img.size)

img.save("export.jpg")
