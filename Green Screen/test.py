from image import *
from file import *

# Writing Test Cases:
def test_image_1():
   img1 = load_img("images/cat_green_screen.jpg")
   img2 = load_img("images/cat_background.jpg")
   result = green_screen(img1, img2)
   save_img(result, "images/new_image_1.jpg")

def test_image_2():
   img1 = load_img("images/owl_green_screen.jpg")
   img2 = load_img("images/owl_background.jpg")
   result = green_screen(img1, img2)
   save_img(result, "images/new_image_2.jpg")
# Write your test function here
def test_green_screen_1():
   img1 = [[(120, 30, 60), (0, 255, 0)]]
   img2 = [[(90, 50, 20), (40, 20, 100)]]
   observed = green_screen(img1, img2)
   assert observed == [[(120, 30, 60), (40, 20, 100)]], f'Expected: [[(120, 30, 60), (40, 20, 100)]], but got {observed}'

def test_green_screen_2():
   img1 = [[(120, 30, 60), (0, 0, 0)]]
   img2 = [[(90, 50, 20), (40, 20, 100)]]
   observed = green_screen(img1, img2)
   assert observed == [[(120, 30, 60), (0, 0, 0)]], f'Expected: [[(120, 30, 60), (0, 0, 0)]], but got {observed}'

def test_green_screen_3():
   img1 = [[(90, 120, 50), (20, 80, 50)], [(0, 255, 0), (30, 20, 40)]]
   img2 = [[(40, 20, 70), (10, 0, 90)], [(90, 55, 10), (130, 220, 90)]]
   observed = green_screen(img1, img2)
   assert observed == [[(90, 120, 50), (20, 80, 50)], [(90, 55, 10), (30, 20, 40)]], f'Expected: [[(90, 120, 50), (20, 80, 50)], [(90, 55, 10), (30, 20, 40)]], but got {observed}'

def test_green_screen_4():
   img1 = [[(255, 255, 255), (0, 255, 0)]]
   img2 = [[(255, 255, 255), (255, 255, 255)]]
   observed = green_screen(img1, img2)
   assert observed == [[(255, 255, 255), (255, 255, 255)]], f'Expected: [[(255, 255, 255), (255, 255, 255)]], but got {observed}'

# Calling Functions:
test_image_1()
test_image_2()

test_green_screen_1()
test_green_screen_2()
test_green_screen_3()
test_green_screen_4()