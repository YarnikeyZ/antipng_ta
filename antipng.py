from PIL import Image
from subprocess import getoutput as gout
from sys import argv as args

tclr = "\033[0;0m\033[H\033[2J\033[3J"
sscale = ['.', "'", ',', ':', '^', '"', ';', '*', '!', '²', '¤', '/', 'r', '(', '?', '+', '?', 'c', 'L', 'ª', '7', 't', '1', 'f', 'J', 'C', 'Ý', 'y', '¢', 'z', 'F', '3', '±', '%', '2', 'k', 'ñ', '5', 'A', 'Z', 'X', 'G', '$', 'À', '0', 'Ã', 'm', '&', 'Q', '8', '#', 'R', 'Ô', 'ß', 'Ê', 'N', 'B', 'å', 'M', 'Æ', 'Ø', '@', '¶']
cscale  = [0, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 15]

def do_art(path_to_image: str, y: int, symbols: bool, colors: bool):
    try:
        img = Image.open(path_to_image).convert('L')
        if y == 0:
            y = img.size[1]
        x = y*2
        img = img.resize((x, y), Image.Resampling.LANCZOS)
        obj = img.load()
        pic = ''
        for y_pix in range(0, img.size[1]):
            for x_pix in range(0, img.size[0]):
                pixel = ''
                symbol = '#'
                if symbols:
                    sbright = obj[x_pix, y_pix]//4
                    if sbright == 0:
                        sbright =+ 1
                    symbol = sscale[sbright-1]
                    
                pixel = symbol
                
                color = ''
                if colors:
                    cbright = obj[x_pix, y_pix]//9
                    if cbright > 25:
                        cbright = 25
                    elif cbright < 1:
                        cbright = 0
                    color = cscale[cbright]
                    pixel = f'\033[38;5;{color}m{pixel}\033[0;0m'

                pic += pixel
            pic += '\n'
        return pic
    except KeyboardInterrupt:
        exit()

try:
    print(do_art(args[1], int(args[2]), True if args[3] == 'True' else False, True if args[4] == 'True' else False))
except IndexError:
    try:
        print(do_art(input("Img path: "), int(input("Y: ")), int(input("Colors (True/False): ")), int(input("Symbols (True/False): "))))
    except IndexError:
        exit()
