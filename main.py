import os

import parser
import slicing
import sys

#This file handles data validation of arguments and
# uses slicing.py to slice a model and then parser.py to parse the GCODE
def main():
    #Will need to change how filepath is specified as it will be coming from a form
    filepath_stl = '3DBenchy.stl'

    slicing.slice_model(filepath_stl) #slicing stl -> gcode
    filepath_gcode = get_gcode_filepath(filepath_stl) #get gcode filepath
    parser.get_printing_details_from_gcode(filepath_gcode) #parse gcode for costs


def get_gcode_filepath(filepath):
    """"PrusaSlicer by default calls resulting gcode the same name as the stl file just different extension.
    So this removes .stl from filepath_stl and replace with .gcode
    :param filepath: filepath to the 3d model file
    :return: filepath to the resulting gcode file"""
    filename_no_ext = filepath.split(".")
    filepath_gcode = filename_no_ext[0] + ".gcode"
    return filepath_gcode

if __name__ == '__main__':
    main()
