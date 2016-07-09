#!/usr/bin/env python3

from PIL import Image
from os.path import isfile
import sys, getopt

def main(argv):
    
    path_to_image = ''
    path_to_matrix = ''
    imgmat = False
    
    try:
        opts, args = getopt.getopt(argv,"hi:m:",["imgmat"])
    except getopt.GetoptError:
        print("Type " + sys.argv[0] + " -h for help")
        return
    for opt, arg in opts:
        if opt == '-h':
            print("Usage: " + sys.argv[0] + " -m <matrix file/name> -i <image file/name> [--imgmat]")
            print("-m: location of matrix file")
            print("-i: name and path for image file")
            print("--imgmat: will cause " + sys.argv[0] + " to take the image file as input and produce an output at the specified matrix location")
            print('\n')
            print(sys.argv[0] + " will take as input a path to a text file with each line representing rows and each space separated number representing column elements. Numbers must be binary (0 or 1) with 0 representing a white pixel and 1 representing a black pixel. The matrix will be converted to an image file and saved to the specified location. If the --imgmat option is used, then " + sys.argv[0] + " will use the file at the specified image location and convert it to a binary matrix in plain text format.")
            return
        elif opt == '-i':
            path_to_image = arg
        elif opt == '-m':
            path_to_matrix = arg
        elif opt == '--imgmat':
            imgmat = True
    
    if path_to_matrix == '' or path_to_image == '':
        if path_to_matrix == '':
            print("Matrix argument missing")
        if path_to_image == '':
            print("Image argument missing")
        return
    
    if imgmat:
        image_to_matrix(path_to_matrix, path_to_image)
    else:
        matrix_to_image(path_to_matrix, path_to_image)
        

def matrix_to_image(matrix_path, image_path):
    
    if not (isfile(matrix_path)):
        print("Could not find " + matrix_path)
        return
    
    out_image_height = 0
    out_image_width = 0
    out_list = []
    
    try:
        with open(matrix_path) as in_text_matrix:
            for line in in_text_matrix:
                out_image_height += 1
                temp_list = line.split()
                out_image_width = len(temp_list)
                out_list += temp_list

    except IOError:
        print("Error opening file " + matrix_path)
        return
    


    out_list = [255 if x == '0' else 0 for x in out_list]
    
    out_image = Image.new('1', (out_image_width,out_image_height))
    out_image.putdata(out_list)
    out_image.convert('RGB')
    try:
        out_image.save(image_path, 'PNG')     
    except IOError:
        print("Error saving file " + image_path)
        
    out_image.close()
        
def image_to_matrix(matrix_path, image_path):
    
    if not (isfile(image_path)):
        print("Could not find " + image_path)
        return
    
    
    in_image = None
    try:
        in_image = Image.open(image_path)
    except IOError:
        print("Error opening file " + image_path)
        return
    
    in_image = in_image.convert('1')
    in_image_width = in_image.size[0]
    in_image_height = in_image.size[1]
    in_list = list(in_image.getdata())
    in_list = [1 if x == 0 else 0 for x in in_list]
    
    try:
        with open(matrix_path,'w') as out_text_matrix:
        
            out_string = ''
            
            
            for i in range(0,in_image_height):
                out_string = ' '.join(str(x) for x in in_list[i*in_image_width : (i + 1)*in_image_width])
                out_text_matrix.write("%s\n" % out_string)
                
    except IOError:
        print("Error saving file " + matrix_path)
        
def image_to_list(image_path):
    if not (isfile(image_path)):
        print("Could not find " + image_path)
        return
    
    
    in_image = None
    try:
        in_image = Image.open(image_path)
    except IOError:
        print("Error opening file " + image_path)
        return
    
    in_image = in_image.convert('1')
    in_image_width = in_image.size[0]
    in_image_height = in_image.size[1]
    in_list = list(in_image.getdata())
    in_list = [1 if x == 0 else 0 for x in in_list]
    
    return_list = []
    
    for i in range(0,in_image_height):
        new_list = []
        new_list.append([x for x in in_list[i*in_image_width : (i + 1)*in_image_width]])
        return_list.append(new_list)
        
    return return_list

        
if __name__ == '__main__':
    
    main(sys.argv[1:])
