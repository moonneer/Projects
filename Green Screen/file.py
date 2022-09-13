from image import *

# Green screen function:
def green_screen(img1, img2):
    for row in range(height(img1)):
        for column in range(width(img1)):
            temp_1 = img1[row][column]
            temp_2 = img2[row][column]
            if img1[row][column] == (0, 255, 0):
                img1[row][column] = (temp_2[0], temp_2[1], temp_2[2])
    return img1
