# -*- coding: utf-8 -*-

from PIL import Image , ImageDraw , ImageFilter
import Tkinter as tk
import math

#화면 사이즈 구하기
root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

del root

#배경 이미지와 타겟이미지 선언
wallpaper = Image.new(size = (width,height), color="white",mode="RGB")

img = Image.open("target.jpg")

#비율 기준으로 가로맞춤 및 세로마춤 판단
x, y = img.size

if float(height)/float(width) >= float(y)/float(x) :
    zoomf = float(width)/float(x)
    zoomb = float(height)/float(y)
else:
    zoomf = float(height)/float(y)
    zoomb = float(width)/float(x)

#앞뒤로 배치될 이미지 생성
front = img.resize((int(x*zoomf),int(y*zoomf)), Image.ANTIALIAS)
back = img.resize((int(x*zoomb),int(y*zoomb)), Image.ANTIALIAS)

del img

#뒤에 배치될 이미지는 아웃 포커싱을 위해 블러처리
back = back.filter(ImageFilter.GaussianBlur(10))

#각 이미지 배치및 저장
wallpaper.paste(back,(width/2-back.size[0]/2,height/2-back.size[1]/2))
wallpaper.paste(front,(width/2-front.size[0]/2,height/2-front.size[1]/2))

wallpaper.save("export.png","PNG")
