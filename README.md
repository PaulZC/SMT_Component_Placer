# SMT Component Placer

A simple Python TK GUI which allows you to superimpose two OpenCV camera images (live and frozen) to aid surface mount component placement.

Works best under Linux (e.g. on Raspberry Pi) as OpenCV does not work correctly with some Windows drivers.

Hook up a USB microscope and then run [SMT_Component_Placer.py](https://github.com/PaulZC/SMT_Component_Placer/blob/master/SMT_Component_Placer.py)

Clicking anywhere in the image box will store the frozen image. The slider can then be used to superimpose the frozen and live images.

Freezing an image of the pads on your circuit board and then superimposing a live image of the component as you place it
allows you to line up the component legs with the circuit board pads more easily.

![USB_Microscope.JPG](https://github.com/PaulZC/SMT_Component_Placer/blob/master/img/USB_Microscope.JPG)

![GUI_1.JPG](https://github.com/PaulZC/SMT_Component_Placer/blob/master/img/GUI_1.JPG)

This project is distributed under a Creative Commons Attribution + Share-alike (BY-SA) licence.
Please refer to section 5 of the licence for the "Disclaimer of Warranties and Limitation of Liability".

Enjoy!

**_Paul_**