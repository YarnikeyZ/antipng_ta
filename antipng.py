from PIL import Image
from subprocess import getoutput as gout
from sys import argv as args

tclr = gout('clear')
sscale = ['.', "'", ',', ':', '^', '"', ';', '*', '!', '²', '¤', '/', 'r', '(', '?', '+', '?', 'c', 'L', 'ª', '7', 't', '1', 'f', 'J', 'C', 'Ý', 'y', '¢', 'z', 'F', '3', '±', '%', '2', 'k', 'ñ', '5', 'A', 'Z', 'X', 'G', '$', 'À', '0', 'Ã', 'm', '&', 'Q', '8', '#', 'R', 'Ô', 'ß', 'Ê', 'N', 'B', 'å', 'M', 'Æ', 'Ø', '@', '¶']
cscale  = [0, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 15]

def do_art(y, path_to_image):
    try:
        x = y*2
        img = Image.open(path_to_image).convert('L').resize((x, y), Image.Resampling.LANCZOS)
        obj = img.load()
        pic = ''
        for y_pix in range(0, img.size[1]):
            line = ''
            for x_pix in range(0, img.size[0]):
                cbright = obj[x_pix, y_pix]//9-1
                sbright = obj[x_pix, y_pix]//4
                if sbright == 0:
                    sbright =+ 1
                if cbright > 25:
                    cbright = 25
                elif cbright < 1:
                    cbright = 0
                line += f'\033[38;5;{cscale[cbright]}m{sscale[sbright-1]}\033[0;0m'
            pic += f'{line}\n'
        print(f"{tclr}{pic}")
    except KeyboardInterrupt:
        exit()

try:
    path_to_image = args[1]
    do_art(int(args[2]), path_to_image)
except IndexError:
    try:
        path_to_image = args[1]
        do_art(int(input("Y:")), path_to_image)
    except IndexError:
        exit()
