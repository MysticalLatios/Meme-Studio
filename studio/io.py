#This file is to read in and export images

import image_map

#Opens up a ppm and returns it as a ppm
def open_PPM(file_name):
    image = image_map.ppm()
    with open(file_name) as file:

        #Read the first 3 lines
        line1 = file.readline()
        #Check to see if file is a PPM
        if line1[0] == "P":
            image.set_spec(line1)
        else:
            #File is not a PPM
            raise Exception("The file that was expected to be a PPM, does not apear to follow the PPM file format")

        #Read the second line by type casting the line into a list
        line2 = file.readline()
        list(line2)
        image.set_x(line2[0])
        image.set_y(line2[1])

        #Read the third line
        line3 = file.readline()
        image.set_max_rgb(line3)

        x = 0
        y = 0

        for line in file:
            x = 0
            raw_pixle_list = list(line)
            
            #While the list is not empty, get stuff from it
            while raw_pixle_list != []:
                pix = image_map.pixel()
                temp_raw = []
                for i in range(1,3):
                    #Get the first item
                    temp_raw.append(raw_pixle_list[0])
                    #Then remove the first item
                    raw_pixle_list.pop(0)

                pix.set_red(temp_raw[0])
                pix.set_red(temp_raw[1])
                pix.set_red(temp_raw[2])
                
                image.add_to_map(x, y, pix)

                x = x + 1

            #After the while ends, we are on our next line
            y = y + 1

                






