#Its how we store our images

from collections import defaultdict

#Set up dicts in dicts
nested_dict = lambda: defaultdict(nested_dict)

class pixel:
    '''This class is for holding our pixel data '''
    red_value = 0
    green_value = 0
    blue_value = 0
    max_rgb = 255 #This is hardcoded for now TODO:add it as required input in the pixel constructor

    def set_red(self, value):
        self.red_value = value

    def set_green(self, value):
        self.green_value = value

    def set_blue(self, value):
        self.blue_value = value

    def get_red(self):
        return self.red_value

    def get_green(self):
        return self.green_value 

    def get_blue(self):
        return self.blue_value

    def get_pixel_raw(self):
        '''returns a pixel as a string '''
        return (str(self.red_value) + " " + str(self.green_value) + " " + str(self.blue_value) + " ")

    def print_pixle(self):
        print("Im a pixel and my rgb is: " + str(self.red_value) + " " + str(self.green_value) + " " + str(self.blue_value) + "\n")
    

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

    def get_spec(self):
       return self.ppm_spec

    def get_x(self):
        return int(self.dimension_x)

    def get_y(self):
        return int(self.dimension_y)

    def get_max_rgb(self):
        return self.max_rgb

    def add_to_map(self, x, y, pix):
        self.image_map[x][y] = pix

    def get_pixel(self, x, y):
        '''returns the pixel based on location'''
        return self.image_map[x][y]

    def get_pixel_raw(self, x, y):
        '''Returns the pixel as a string'''
        return self.image_map[x][y].get_pixel_raw()




