import tensorflow as tf
from keras_preprocessing.image import ImageDataGenerator
from keras_preprocessing import image

import numpy as np
import easygui
from keras.models import load_model
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
my_w = tk.Tk()
# width = my_w.winfo_width()
# height = my_w.winfo_height()
# print(width,height)
# my_w.geometry("%dx%d"%(width,height))  
my_w.state("zoomed")
my_w.wm_title("Alzheimer Disease Prediction")
my_font1=(18)

bg = ImageTk.PhotoImage(file='alzheimer/bg.png')
bgLabel = Label(my_w, image=bg)
bgLabel.place(x=0, y=0 ,relwidth=1,relheight=1)



# l1 = tk.Label(my_w,text='Upload Files & get results',width=30,font=my_font1,bg='#124178',
#                    fg='white',)  
# l1.place(x=550 , y=190,relwidth=0.2,relheight=0.1)
b1 = tk.Button(my_w, text='Upload Images', 
   width=20,command = lambda:result(), activebackground='#000080',font=my_font1, bg='#124178',fg='white')
b1.place(relx=0.42,rely=0.4, relwidth=0.15,relheight=0.07)

print(tf.__version__)

def close():
   my_w.destroy()


titleLabel = Label(my_w, text=' ALIZHEIMER DISEASE PREDICTION', font=('italic', 22, 'bold '), bg='#0C516A',
                   fg='white')
titleLabel.place(x=0, y=0,relwidth=1,relheight=0.1)

endbtn=Button(my_w,text="Exit",font='italic 14 bold',bg='#0C516A',fg='white',command=close)
endbtn.place(relx=0.45,rely=0.8,relwidth=0.1,relheight=0.05)


classifierLoad = tf.keras.models.load_model('alzheimer\MODEL\model264.keras')


def result():
    
   filename =upload_file()
   test_image2 = image.load_img(filename, target_size = (224,224))
   test_image2 = image.img_to_array(test_image2)
   test_image2 = np.expand_dims(test_image2, axis = 0)   
   # cnn prediction on the test image
   result = classifierLoad.predict(test_image2)
   b1.place_forget()
   if result[0][1] == 1:
       prediction2="NonDemented"
   elif result[0][0] == 1:
       prediction2="MildDemented"
   elif result[0][2] == 1:
       prediction2="VeryMildDementedd"
   elif result[0][3] == 1:
       prediction2="ModerateDemented"
   
      
   #print(prediction2)
   prediction=prediction2
   l2 = tk.Label(my_w,text="Result :  "+prediction,font=my_font1,bg='#AC9005',fg='white',)  
   l2.place(relx=0.4, rely=0.65, relwidth=0.2, relheight=0.05)
   return filename 
       
def upload_file():   
    filename =  easygui.fileopenbox()
    img=Image.open(filename) # read the image file
    img=img.resize((200,140)) # new width & height
    img=ImageTk.PhotoImage(img)
    e1 =tk.Label(my_w)
    e1.place(relx=0.43, rely=0.4, relwidth=0.15, relheight=0.2)
    e1.image = img
    e1['image']=img
    return filename

my_w.mainloop()




