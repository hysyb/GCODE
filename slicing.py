# This module slices a provided 3d model and a GCODE file is created.
import subprocess


def slice_model(model_file):
    """Slices a 3d model using PrusaSlicer CLI
    :param model_file: a path to a 3d model file to be sliced. Acceptable filetypes: ..."""
    subprocess.run(['./PrusaSlicer-2.7.1+linux-x64-GTK3-202312121425.AppImage', '--export-gcode',  model_file])

