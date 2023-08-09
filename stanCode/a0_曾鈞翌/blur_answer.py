"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    new_w = img.width
    new_h = img.height
    new_image = SimpleImage.blank(new_w, new_h)
    
    for y in range(new_h):
        for x in range(new_w):
            pixel = img.get_pixel(x, y)
            point = 0
            red_sum = green_sum = blue_sum = 0

            for i in range(y - 1, y + 2):
                if i < 0 or i >= new_h:
                    continue
                for j in range(x - 1, x + 2):
                    if j < 0 or j >= new_w:
                        continue
                    point += 1
                    pixel1 = img.get_pixel(j, i)
                    red_sum += pixel1.red
                    green_sum += pixel1.green
                    blue_sum += pixel1.blue

            new_pixel = SimpleImage.blank(1, 1).get_pixel(0, 0)
            new_pixel.red = red_sum // point
            new_pixel.green = green_sum // point
            new_pixel.blue = blue_sum // point
            new_image.set_pixel(x, y, new_pixel)

    return new_image


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
