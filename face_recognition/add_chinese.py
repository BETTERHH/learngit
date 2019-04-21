from PIL import Image, ImageDraw, ImageFont
import  cv2
import numpy as np

def  change_cv2_draw(image, strs, local, size, color):
    cv2img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pilimg = Image.fromarray(cv2img)
    draw = ImageDraw.Draw(pilimg)
    font = ImageFont.truetype("simhei.ttf", size, encoding="utf-8")
    draw.text(local, strs, color, font=font)
    image = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)

    return image
