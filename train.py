from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os




class Student:
        def __init__(self,root):
              self.root=root
              self.root.geometry("1530x790+0+0")
              self.root.title("Face Recognition System")

              title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",32,"bold"),fg="#00004d",bg="white",justify="center")
              title_lbl.place(x=0,y=0,width=1380,height=40)

              img_top=Image.open(r"E:\projecttt\Attendance_System\images\frame1.webp")
              img_top=img_top.resize((720,110),Image.LANCZOS)
              self.top_photoimg=ImageTk.PhotoImage(img_top)
              f_label=Label(self.root,image=self.top_photoimg)
              f_label.place(x=5,y=0,width=635,height=105)


            
if __name__ == "__main__":
    root =Tk()
    obj=Student(root)
    root.mainloop()