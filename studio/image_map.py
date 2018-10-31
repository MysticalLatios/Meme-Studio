#Its how we store our images

from collections import defaultdict

#Set up dicts in dicts
nested_dict = lambda: defaultdict(nested_dict)

class pixel:
    red_value = 0
    green_value = 0
    blue_value = 0
    max_rgb = 255; #This is hardcoded for now TODO:add it as required input in the pixel constructor

    def set_red(self, value):
        self.red_value = value

    def set_green(self, value):
        self.green_value = value

    def set_blue(self, value):
        self.blue_value = value


class ppm:
    ppm_spec = 0
    dimension_x = 0
    dimension_y = 0
    max_rgb = 0

    #Dictionary
    #First key is xpos
    #Second key is ypos
    #Second is a pixel
    image_map = nested_dict()


    def set_spec(self, spec):
        self.ppm_spec = spec

    def set_x(self, x):
        self.dimension_x = x

    def set_y(self, y):
        self.dimension_y = y

    def set_max_rgb(self, rgb):
        self.max_rgb = rgb

    def add_to_map(self, x, y, pix):
        self.image_map[x][y] = pix




