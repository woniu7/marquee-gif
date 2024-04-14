from PIL import Image, ImageDraw, ImageFont
#img = Image.open("/code/educative.jpeg")
img = Image.new('RGBA', (256, 250), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

#txt = "全世界无产者，联合起来！"
txt = "ab全世"
myfont = ImageFont.truetype('/home/d/.local/share/fonts/yugioh-diy/YGODIY-Chinese.ttf', 50)
draw.text((50, 50), txt, fill =(255, 0, 0), font=myfont)
img.save('graph.gif', 'GIF')
img.show()
