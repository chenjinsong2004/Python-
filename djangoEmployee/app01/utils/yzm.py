from PIL import Image, ImageDraw, ImageFont
import random

# 随机验证码文本（数字+大小写字母）
def generate_random_captcha(length=4):
    chars = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmnpqrstuvwxyz23456789"
    return ''.join(random.choices(chars, k=length))

# 生成高难度干扰验证码图片
def generate_complex_captcha(code):
    # 画布大小
    width, height = 220, 80
    # 随机浅色背景
    bg_color = (random.randint(230, 255), random.randint(230, 255), random.randint(230, 255))
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # ✅ Windows专属字体 永远不报错
    try:
        # 调用Windows自带原生字体，效果最好
        font = ImageFont.truetype("arial.ttf", 45)
    except:
        # 找不到就自动降级兜底
        font = ImageFont.load_default(size=45)

    # 1. 画随机干扰背景噪点
    for _ in range(800):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill=(random.randint(0, 180), random.randint(0, 180), random.randint(0, 180)))

    # 2. 画干扰斜线条
    for _ in range(8):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line([(x1,y1), (x2,y2)], fill=(random.randint(50,150),random.randint(50,150),random.randint(50,150)), width=2)

    # 3. 逐个画字符：随机颜色、随机旋转、随机偏移
    offset = 30
    for char in code:
        # 随机深色文字
        text_color = (random.randint(10, 80), random.randint(10, 80), random.randint(10, 80))
        # 随机上下偏移
        y_offset = random.randint(-8, 8)
        # 随机倾斜位置
        draw.text((offset, 12 + y_offset), char, font=font, fill=text_color)
        offset += 48

    # 4. 增加随机曲线干扰
    import math
    for i in range(width):
        y = int(35 + 12 * math.sin(i * 0.04))
        draw.point((i, y), fill=(100,100,100))

    return img