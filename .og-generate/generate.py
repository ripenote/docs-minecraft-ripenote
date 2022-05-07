# https://zenn.dev/makiart/articles/78d53694e70105

from PIL import Image, ImageFont

ogp_base_img_path = 'base.png'
font_black_path = "NotoSansJP-Regular.otf"
font_medium_path = "NotoSansJP-Bold.otf"

def add_centered_text(base_img, text, font_path, font_size, font_color, height):
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(base_img)
    
    # 文字がベース画像からはみ出ないように処理
    if draw.textsize(text, font=font)[0] > base_img.size[0] - 170:
        while draw.textsize(text + '…', font=font)[0] > base_img.size[0] - 170:
            text = text[:-1]
        text = text + '…'

    draw.text(((base_img.size[0] - draw.textsize(text, font=font)[0]) / 2, height), text, font_color, font=font)

    return base_img

if __name__ == '__main__':
    base_img = Image.open(ogp_base_img_path).copy()
    base_img = add_centered_text(base_img, '/execute コマンド', font_black_path, 64, (64, 64, 64), 380)
    base_img = add_centered_text(base_img, 'Created by tamagoez', font_medium_path, 32, (120, 120, 120), 560)

    base_img.show()
    base_img.save('output.png')
