from PIL import Image


def jpg2ascii():
    symbols = ["@", "#", "£", "=", "+", "|", ":", ".", " "]
    img = Image.open("man.jpg")
    pix = img.load()
    data = []

    data = ""
    symbol_count = len(symbols)

    for y in range(img.size[1]):
        if y > 0 :
            data = data + "\n"
        for x in range(img.size[0]):
            grayScale = toGray(pix[x, y])
            data = data + symbols[int((grayScale / 255.0) * symbol_count)]

    text_file = open("man.txt", "w")
    text_file.write(data)


def luminance(c):
    red = c[0]
    green = c[1]
    blue = c[2]
    return (.299 * red) + (.587 * green) + (.114 * blue)


def toGray(c):
    y = int(round(luminance(c)))
    return y

if __name__ == "__main__":
    jpg2ascii()
