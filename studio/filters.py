#File for handling out filters
import random

from studio import image_map


#lets make it more blue
def more_blue(img_in: image_map.ppm):
    ''' Makes an image more blue '''

    x = img_in.get_x()
    y = img_in.get_y()

    for i in range(0, y):
        for j in range(0, x):
            pix = img_in.get_pixel(j,i)
            pix.set_blue(int(pix.get_blue()) + random.randint(-25, 25) % 255)
            pix.set_green(int(pix.get_green()) + random.randint(-25, 25) % 255)
            pix.set_red(int(pix.get_red()) + random.randint(-25, 25) % 255)
