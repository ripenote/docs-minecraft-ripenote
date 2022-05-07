# https://zenn.dev/makiart/articles/78d53694e70105
import os
import sys
from PIL import Image, ImageDraw, ImageFont

CONST_REQUEST_PATH = sys.argv[1]
CONST_CWD = str(os.getcwd() + '/')
ogp_base_img_path = CONST_CWD + 'base.png'
font_black_path = CONST_CWD + "NotoSansJP-Regular.otf"
font_medium_path = CONST_CWD + "NotoSansJP-Bold.otf"

def add_centered_text(base_img, text, font_path, font_size, font_color, height):
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(base_img)
    
    # 文字がベース画像からはみ出ないように処理
    if draw.textsize(text, font=font)[0] > base_img.size[0] - 10:
        while draw.textsize(text + '…', font=font)[0] > base_img.size[0] - 10:
            text = text[:-1]
        text = text + '…'

    draw.text(((base_img.size[0] - draw.textsize(text, font=font)[0]) / 2, height), text, font_color, font=font)

    return base_img

if __name__ == '__main__':
    base_img = Image.open(ogp_base_img_path).copy()
    base_img = add_centered_text(base_img, '/execute コマンド', font_black_path, 64, (64, 64, 64), 380)
    base_img = add_centered_text(base_img, 'Created by tamagoez', font_medium_path, 32, (120, 120, 120), 560)

    base_img.show()
    print(CONST_REQUEST_PATH)
    # https://note.nkmk.me/python-os-mkdir-makedirs/
    os.makedirs(os.path.dirname(CONST_REQUEST_PATH), exist_ok=True)
    # https://note.nkmk.me/python-os-basename-dirname-split-splitext/
    base_img.save(CONST_CWD + 'output/' + os.path.splitext(os.path.basename(CONST_REQUEST_PATH))[0] + '.png')
