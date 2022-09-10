#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 11:57:54 2022

@author: bridgetmoynihan
"""

## taken and adapted from source code found on "https://techvidvan.com/tutorials/extract-text-from-image-with-python-opencv/"

# import modules
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/5.2.0/bin/tesseract.exe'

# setting up Tkinter
root = Tk()
root.title('Text from Image Project')

newline = Label(root)
uploadedImg = Label(root)
scroll = Scrollbar(root)
scroll.pack(side = RIGHT, fill = Y) #setting location for scroll bar

# extract text from the image
def extract(path):
    Actual_image = cv2.imread(path)
    img = cv2.resize(Actual_image, (400, 350))
    height, width, thickness = img.shape
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #convert to a different color space
    texts = pytesseract.image_to_data(img)
    mytext = ""
    prevy = 0
    
    for count, text in enumerate(texts.splitlines()):
        if count==0:
            continue
        
        text = text.split()
        
        if len(text) == 12: # ?
            x,y,w,h = int(text[6]),int(text[7]),int(text[8]),int(text[9])
            
            if(len(mytext)==0):
                prevy=y
          
            if(prevy-y>=10 or y-prevy>=10):
                print(mytext)
                Label(root,text=mytext,font=('Times',15,'bold')).pack()
                mytext=""
            mytext = mytext + text[11]+" "
            prevy=y
    Label(root,text=mytext,font=('Times',15,'bold')).pack()
    
# create button to extract text
def show_button(path):
    extractBtn = Button(root, text="Extract Text", 
                        command = lambda: extract(path), 
                        bg="#2f2f77",fg="gray",pady=15,
                        padx=15,font=('Times',15,'bold'))
    extractBtn.pack()

# upload image 
def upload():    
    try:
        path = filedialog.askopenfilename()
        image = Image.open(path)
        img = ImageTk.PhotoImage(image)
        uploadedImg.configure(image=img)
        uploadedImg.image=img
        show_button(path)
    except:
        pass

uploadbtn = Button(root,text="Upload an image",command=upload,background="purple",foreground="purple",height=2,width=20,font=('Times',15,'bold')).pack()
newline.configure(text='\n')
newline.pack()
uploadedImg.pack()
root.mainloop()
    
    
    
