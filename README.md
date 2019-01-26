# SMT Component Placer

A simple Python TK GUI which allows you to superimpose two OpenCV camera images (live and frozen) to aid surface mount component placement.

![USB_Microscope.JPG](https://github.com/PaulZC/SMT_Component_Placer/blob/master/img/USB_Microscope.JPG)

![GUI_1.JPG](https://github.com/PaulZC/SMT_Component_Placer/blob/master/img/GUI_1.JPG)

Works best under Linux as some Windows drivers do not work correctly with OpenCV. See below for the installation instructions.

Connect a USB microscope and then run [SMT_Component_Placer.py](https://github.com/PaulZC/SMT_Component_Placer/blob/master/SMT_Component_Placer.py)

Left-clicking anywhere in the image box will store the frozen image. The slider can then be used to superimpose the frozen and live images.

Freezing an image of the pads on your circuit board and then superimposing a live image of the component as you place it
allows you to line up the component legs with the circuit board pads more easily.

Right-clicking anywhere in the image box will save the displayed image in .png format.

![Placer_1.JPG](https://github.com/PaulZC/SMT_Component_Placer/blob/master/img/Placer_1.JPG)
![Placer_2.JPG](https://github.com/PaulZC/SMT_Component_Placer/blob/master/img/Placer_2.JPG)
![Placer_3.JPG](https://github.com/PaulZC/SMT_Component_Placer/blob/master/img/Placer_3.JPG)

![Placer_4.JPG](https://github.com/PaulZC/SMT_Component_Placer/blob/master/img/Placer_4.JPG)
![Placer_5.JPG](https://github.com/PaulZC/SMT_Component_Placer/blob/master/img/Placer_5.JPG)
![Placer_6.JPG](https://github.com/PaulZC/SMT_Component_Placer/blob/master/img/Placer_6.JPG)

## Installation

Assuming you already have git installed, you can download a copy of this repo using:

- git clone https://github.com/PaulZC/SMT_Component_Placer

Or, you can download the Python code on its own using:

- wget https://github.com/PaulZC/SMT_Component_Placer/blob/master/SMT_Component_Placer.py

Run the code in Python:

- python SMT_Component_Placer.py

To let the code run successfully you will need to install the following Python libraries:

### Numpy

- pip install numpy

### OpenCV

- pip install opencv-python

### Pillow

- pip install Pillow

### PIL ImageTk

- sudo apt-get install python-pil.imagetk

## Licence

This project is distributed under a Creative Commons Attribution + Share-alike (BY-SA) licence.
Please refer to section 5 of the licence for the "Disclaimer of Warranties and Limitation of Liability".

Enjoy!

**_Paul_**