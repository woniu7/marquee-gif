from PIL import Image, ImageDraw, ImageFont

def get_text_dimensions(text_string, font):
    # https://stackoverflow.com/a/46220683/9263761
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return (text_width, text_height)


def frange(start, stop=None, step=None):
    start = float(start)
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            yield stop
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1


def addText(x, y, text, font):
    img = Image.new('RGBA', (516, 160), (0, 0, 0, 0))
#    img = Image.new('RGBA', (256, 80), 'white')
    d = ImageDraw.Draw(img)
    d.text((x, y), text, font=font, fill=(255, 0, 0))

    return img


font = ImageFont.truetype('/home/d/.local/share/fonts/TrueType/wqy/wqy-microhei.ttc', 120)
text = "全世界无产者，联合起来！"
#text = "hello world"
text_size = get_text_dimensions(text, font)
images = []
n = text_size[0]
#n = 120
step = float(n) // 50.0
for i in frange(-30, (n-516+30), step):
    images.append(addText(-i, 0, text, font))
for i in frange(-30, (n-516+30), step):
    images.append(addText(-(n-516+30)+i, 0, text, font))
    
images[0].save("enterexit.gif", save_all=True, append_images=images[1:],
               optimize=False, duration=128, loop=0, disposal=2)
