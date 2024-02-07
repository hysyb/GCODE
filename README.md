# GCODE
Software to slice a 3d model file using PrusaSlicer(https://github.com/prusa3d/PrusaSlicer) and then parse the results with the goal of generating a customer cost to 3D print a particular model. <br> 
Test 3d model is the infamous 3DBenchy(https://www.3dbenchy.com/) <br>
<br>
main.py contains main function.<br>
slicing.py is where the model is sliced using PrusaSlicer's CLI. <br>
parser.py is where the GCODE is dissected and relevant sections returned <br>


Next steps is to integrate into a web app so that a 3d model file can be uploaded through a form and run through this software..
