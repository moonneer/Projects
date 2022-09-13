import numpy as np
from PIL import Image

def load_img(filename):
    img = Image.open(filename)
    pil_img = img.convert('RGB')
    arr = np.array(pil_img.getdata(), dtype=np.uint8).reshape(pil_img.height, pil_img.width, 3)
    img = [ [ (int(p[0]),int(p[1]),int(p[2])) for p in row ] for row in arr ]
    return img

def save_img(img, filename):
    arr = np.asarray(img, dtype=np.uint8)
    pil_img = Image.fromarray(arr)
    pil_img.save(filename, format='png')

def create_img(height, width, color):
    result = [None] * height
    for i in range(len(result)):
        result[i] = [color] * width
    return result

def height(img):
    return len(img)

def width(img):
    return len(img[0])

def img_str_to_file(img, filename):
    # Converting to integer pixel values
    img = np.asarray(img, dtype=np.uint8)

    # Calculating max length 
    max_length = len(str((255,255,255)))

    # Limiting the number of rows and columns to be printed
    r_limit = min(20, height(img))
    c_limit = min(20, width(img))
    
    with open(filename, 'w') as file:
        pix_str = ""
        for y in range(r_limit):
            for x in range(c_limit):
                # Creating the string representation
                temp_str = ("(" + str(img[y][x][0])
                           + "," + str(img[y][x][1])
                           + "," + str(img[y][x][2]) + ")")
                pix_str += temp_str
                # Added appropriate number of spaces to make it visually clear
                pix_str += " " * (max_length-len(temp_str))
            pix_str += "\n"
        file.write(pix_str)

    return pix_str