"""Module to parse GCODE and return a price for 3D printing based on print time and material cost
GCODE shouldve been sliced by our program using CLI slic3r, prusaslicer, or cura
therefore, no data validation is performed on the GCODE file, assumed legitimate"""

import sys

#Constants for cost calculations
MY_COST_PER_KG_PLASTIC = 30
MATERIAL_MARKUP = 10
COST_PRINT_TIME_DOLLARS_PER_HOUR = 5
COST_MATERIAL_DOLLARS_PER_GRAM = MY_COST_PER_KG_PLASTIC / 1000 * MATERIAL_MARKUP

def get_printing_details_from_gcode(filepath):
    """Read GCODE file and get printing time, filament cost, print time cost, and total cost.
    Costs use constants as multipliers to give a customer cost. Not my cost.
    :param filepath: GCODE file path
    :return: filament cost, print time cost, and total cost"""
    f = open(filepath, "r")
    filestring = f.read()
    filestring_lines = filestring.split(";")
    print_time_in_hours = 0.0
    total_cost = 0.00
    for line in filestring_lines:
        if "estimated printing time" in line:
            estimated_printing_time_line = line
            estimated_printing_time_line_split = estimated_printing_time_line.split("=")
            estimated_printing_time_line_split_hours = estimated_printing_time_line_split[1].split("h")
            print_time_in_hours += float(estimated_printing_time_line_split_hours[0])
            estimated_printing_time_line_split_minutes = estimated_printing_time_line_split_hours[1].split("m")
            print_time_in_hours += float(estimated_printing_time_line_split_minutes[0])/60
            print_time_cost = float(print_time_in_hours) * COST_PRINT_TIME_DOLLARS_PER_HOUR
            total_cost += print_time_cost

        if "total filament used [g]" in line:
            total_filament_used_line = line
            total_filament_used_line_split = total_filament_used_line.split("=")
            filament_cost = float(total_filament_used_line_split[1]) * COST_MATERIAL_DOLLARS_PER_GRAM
            total_cost += filament_cost

    print(f"Print Time:          {estimated_printing_time_line_split[1]}"
          f"Total filament cost:  ${filament_cost:.2f}\n"
          f"Print time cost:      ${print_time_cost:.2f}\n"
          f"Total cost:           ${total_cost:.2f}")
    return filament_cost, print_time_cost, total_cost
