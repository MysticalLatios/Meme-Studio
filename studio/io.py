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

        #Split the line up
        line2 = line2.split()

        image.set_x(line2[0])
        image.set_y(line2[1])

        #Read the third line
        line3 = lines.pop(0)
        image.set_max_rgb(line3)

        x = 0
        y = 0


        #Make a big boy list for all the pixel data
        big_list = []
        for line in lines:
            pixle_list = line.split()
            for item in pixle_list:
                big_list.append(item)

        #print(big_list)

        #Iterate though or giant list
        for i in range(0, len(big_list), 3):
            pix = image_map.pixel()

            pix.set_red(big_list[i])
            pix.set_green(big_list[i+1])
            pix.set_blue(big_list[i+2])

            image.add_to_map(x,y,pix)

            #pix.print_pixle()

            x = x + 1

            if x == image.get_x():
                x = 0
                y = y + 1



        '''
        for line in lines:
            raw_pixle_list = line.split()
            #While the list is not empty, get stuff from it
            while raw_pixle_list != []:
                pix = image_map.pixel()
                temp_raw = []

                for i in range(0,3):
                    #Get the first item
                    temp_raw.append(raw_pixle_list[0])
                    #Then remove the first item
                    raw_pixle_list.pop(0)

                pix.set_red(temp_raw[0])
                pix.set_green(temp_raw[1])
                pix.set_blue(temp_raw[2])
                
                pix.print_pixle()
                image.add_to_map(x, y, pix)

                x = x + 1

            #After the while ends, we are on our next line
            y = y + 1
        '''
        return image

def write_PPM(img_export: image_map.ppm):
    list_o_strings = list()

    #Append the PPM spec
    list_o_strings.append(img_export.get_spec())

    #Append the PPM x size
    list_o_strings.append( str(img_export.get_x()) + " ")

    #Append the PPM y size
    list_o_strings.append( str(img_export.get_y()) + "\n")

    #Append the max RGB value
    list_o_strings.append(img_export.get_max_rgb() + "\n")


    #Set the row of pixels up and append them to 
    x = img_export.get_x()
    y = img_export.get_y()

    for i in range(0, y):
        row = []
        for j in range(0, x):
            row.append(img_export.get_pixel_raw(j,i))
        list_o_strings.append("".join(row))

    #Then write this list_o_strings out as 

    #Make a list of strings then write them to the file
    file_out = open("output.ppm", 'w')

    for line in list_o_strings:
        print(line)

    #Write out
    for line in list_o_strings:
        file_out.write(line)


    





berg = open_PPM("bunny.ppm")

write_PPM(berg)






