## SMT Component Placer
## Superimposes live and frozen OpenCV camera images to aid component placement

## Supported modes for COLEMETER 50x - 500x Microscope are:
##
## 160,120
## 320,240
## 640,480
## 800,600
## 1024,768
## 1280,720
## 1280,960
## 1280,1024
## 1600,1200
## 1920,1080

import numpy as np
import cv2
import time
import Tkinter as tk
from PIL import Image, ImageTk

class Placer(object):

    def __init__(self):
        ''' Init Placer '''

        #Default values
        self.swap_red_blue = True
        self.camx = 640.
        self.camy = 480.
        self.crossx = int(self.camx/2)
        self.crossy = int(self.camy/2)
        
        #Open camera
        self.cam0 = cv2.VideoCapture(0) # Open camera 0
        time.sleep(2)
        self.cam0.set(cv2.CAP_PROP_FRAME_WIDTH, int(self.camx)) # Set resolution
        self.cam0.set(cv2.CAP_PROP_FRAME_HEIGHT, int(self.camy))
        time.sleep(2)
        _, self.frameL = self.cam0.read() # Read camera image
        if self.swap_red_blue: self.frameL = self.swap_rb_chans(self.frameL) # Swap red and blue
        self.frameL[self.crossy,:] = [255,255,255] # Add crosshair
        self.frameL[:,self.crossx] = [255,255,255]
        self.frameF = self.frameL # Store initial frozen image

        #Set up GUI
        self.window = tk.Tk() # Make main window
        self.window.wm_title("SMT Component Placer") # Add a title
        self.window.config(background="#FFFFFF") # Set background colour to white

        #Set up Frames
        self.toolFrame = tk.Frame(self.window, height=int(self.camy))
        self.toolFrame.pack(side=tk.LEFT)

        self.imageFrame = tk.Frame(self.window, width=int(self.camx), height=int(self.camy))
        self.imageFrame.pack(side=tk.RIGHT)

        #Slider (slider controls live vs frozen images)
        self.slider_txt = tk.Label(self.toolFrame, text = 'Live\nvs\nFrozen')
        self.slider_txt.grid(row=0, column=0)
        self.slider = tk.Scale(self.toolFrame, from_=1, to=0, resolution=0.01, orient=tk.VERTICAL)
        self.slider.set(1.)
        self.slider.grid(row=1, column=0)

        #Video frame
        image = Image.fromarray(self.frameL)
        photo = ImageTk.PhotoImage(image)
        self.image = photo # Prevent garbage collection
        self.label = tk.Label(self.imageFrame,image=photo)
        self.label.pack(fill=tk.BOTH)

        #Bind left mouse button click event - freeze image
        self.label.bind("<Button-1>",self.left_click)

        # Timer
        self.window.after(100,self.timer) # First timer event after 0.1 secs

        # Start GUI
        self.window.mainloop()

    def swap_rb_chans(self, frame):
        ''' Swap red and blue channels '''
        red = frame[:,:,0].copy()
        blue = frame[:,:,2].copy()
        frame[:,:,2] = red
        frame[:,:,0] = blue
        return frame

    def timer(self):
        ''' Update live image '''
        if(self.cam0.isOpened):
            _, self.frameL = self.cam0.read() # Read camera image
            if self.swap_red_blue: self.frameL = self.swap_rb_chans(self.frameL) # Swap red and blue
            self.frameL[self.crossy,:] = [255,255,255] # Add crosshair
            self.frameL[:,self.crossx] = [255,255,255]
            # Add live and frozen images
            added = cv2.addWeighted(self.frameF,(1.-self.slider.get()),self.frameL,self.slider.get(),0) # Add images
            # Update label using added image
            image = Image.fromarray(added)
            photo = ImageTk.PhotoImage(image)
            self.label.configure(image=photo)
            self.image = photo # Prevent garbage collection
        self.window.after(100, self.timer) 

    def left_click(self, event):
        ''' Left mouse click - update frozen image '''
        if(self.cam0.isOpened):
            _, self.frameF = self.cam0.read() # Read camera image
            if self.swap_red_blue: self.frameF = self.swap_rb_chans(self.frameF) # Swap red and blue
            self.frameF[self.crossy,:] = [255,255,255] # Add crosshair
            self.frameF[:,self.crossx] = [255,255,255]

    def close(self):
        time.sleep(2)
        try:
            self.cam0.release() # Close camera
        except:
            pass
        time.sleep(2)
        try:
            cv2.destroyAllWindows()
        except:
            pass

if __name__ == "__main__":
   try:
      placer = Placer()
   finally:
      try:
         placer.close()
      except:
         pass





