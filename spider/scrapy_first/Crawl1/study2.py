from PIL import Image

img = r'K:\1.jpg'
WIDTH = 80
HEIGHT = 60
ascill_char = list(
    "ηθικλμʌəɔ:æεauəɔʒ。,ʃtrdrdzts$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:\"^`'. ")
# ascill_char1=list(" .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$")
ascill_char3 = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascill_char3)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 计算灰度
    unit = (256.0 + 1) / length
    return ascill_char3[int(gray / unit)]


if __name__ == '__main__':
    im = Image.open(img)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'
    print(txt)
    output = r'K:\字符画.txt'
    with open(output, 'w')as f:
        f.write(txt)
