#This file is to read in and export images

import image_map

#Opens up a ppm and returns it as a ppm
def open_PPM(ppm_file_name):
    image = image_map.ppm()
    with open(ppm_file_name) as ppm_file:

        #We now have the lines
        lines = []
        for line in ppm_file:
            lines.append(line)

        for line in lines:
            print(line)


        #Read the first 3 lines
        line1 = lines.pop(0)
        #Check to see if file is a PPM
        if line1[0] == "P":
            image.set_spec(line1)
        else:
            #file is not a PPM
            raise Exception("The ppm_file that was expected to be a PPM, does not apear to follow the PPM file format")

        #Read the second line by type casting the line into a list
        line2 = lines.pop(0)
        list(line2)
        image.set_x(line2[0])
        image.set_y(line2[1])

        #Read the third line
        line3 = lines.pop(0)
        image.set_max_rgb(line3)

        x = 0
        y = 0

        for line in ppm_file:
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


def write_PPM(image):
    list_o_strings = list()

    #Append the PPM spec
    list_o_strings.append(image)

    #Append the PPM x size
    list_o_strings.append(image)

    #Append the PPM y size
    list_o_strings.append(image)

    #Append the max RGB value
    list_o_strings.append(image)


    #Make the image map into a list of strings

    #Then append that strings onto the list_o_strings

    #Then write this list_o_strings out as 

    #Make a list of strings then write them to the file
    file_out = open("output.ppm", 'w')


    





open_PPM("bunny.ppm")




