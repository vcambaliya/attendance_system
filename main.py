from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os

class Face_Recognition_System:
        def __init__(self,root):
              self.root=root
              self.root.geometry("1530x790+0+0")
              self.root.title("Face Recognition System")

              img=Image.open(r"images\images.jpeg")
              img=img.resize((500,130),Image.LANCZOS)
              self.photoimg=ImageTk.PhotoImage(img)

              f_label=Label(self.root,image=self.photoimg)
              f_label.place(x=0,y=0,width=450,height=130)

              img1=Image.open(r"simages\centerimg.jpg")
              img1=img1.resize((500,130),Image.LANCZOS)
              self.photoimg1=ImageTk.PhotoImage(img1)

              f_label=Label(self.root,image=self.photoimg1)
              f_label.place(x=450,y=0,width=460,height=130)

              img2=Image.open(r"images\images.jpeg")
              img2=img2.resize((500,130),Image.LANCZOS)
              self.photoimg2=ImageTk.PhotoImage(img2)

              f_label=Label(self.root,image=self.photoimg2)
              f_label.place(x=910,y=0,width=450,height=130)
              
              img3=Image.open(r"images\facia.webp")
              img3=img3.resize((1530,710),Image.LANCZOS)
              self.photoimg3=ImageTk.PhotoImage(img3)
              bg_img=Label(self.root,image=self.photoimg3)
              bg_img.place(x=0,y=130,width=1530,height=710)
              title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",32,"bold"),fg="#00004d",bg="white",justify="center")
              title_lbl.place(x=0,y=0,width=1380,height=50)


              img4=Image.open(r"images\facia.webp")
              img4=img4.resize((220,220),Image.LANCZOS)
              self.photoimg4=ImageTk.PhotoImage(img4)
              b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
              b1.place(x=90,y=100,width=220,height=220)
              b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),fg="#00004d",bg="white",justify="center")
              b1_1.place(x=90,y=280,width=220,height=40)

              img5=Image.open(r"images\facia.webp")
              img5=img5.resize((220,220),Image.LANCZOS)
              self.photoimg5=ImageTk.PhotoImage(img5)
              b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
              b2.place(x=405,y=100,width=220,height=220)
              b1_2=Button(bg_img,text="Face Recognition",cursor="hand2",font=("times new roman",15,"bold"),fg="#00004d",bg="white",justify="center")
              b1_2.place(x=405,y=280,width=220,height=40)

              img6=Image.open(r"images\facia.webp")
              img6=img6.resize((220,220),Image.LANCZOS)
              self.photoimg6=ImageTk.PhotoImage(img6)
              b3=Button(bg_img,image=self.photoimg6,cursor="hand2")
              b3.place(x=725,y=100,width=220,height=220)
              b1_3=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),fg="#00004d",bg="white",justify="center")
              b1_3.place(x=725,y=280,width=220,height=40)


              img7=Image.open(r"images\facia.webp")
              img7=img7.resize((220,220),Image.LANCZOS)
              self.photoimg7=ImageTk.PhotoImage(img7)
              b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
              b4.place(x=1040,y=100,width=220,height=220)
              b1_4=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),fg="#00004d",bg="white",justify="center")
              b1_4.place(x=1040,y=280,width=220,height=40)


              img8=Image.open(r"images\facia.webp")
              img8=img8.resize((220,220),Image.LANCZOS)
              self.photoimg8=ImageTk.PhotoImage(img8)
              b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
              b5.place(x=90,y=340,width=220,height=220)
              b2_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),fg="#00004d",bg="white",justify="center")
              b2_1.place(x=90,y=520,width=220,height=40)

              img9=Image.open(r"images\facia.webp")
              img9=img9.resize((220,220),Image.LANCZOS)
              self.photoimg9=ImageTk.PhotoImage(img9)
              b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
              b6.place(x=405,y=340,width=220,height=220)
              b2_2=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",15,"bold"),fg="#00004d",bg="white",justify="center")
              b2_2.place(x=405,y=520,width=220,height=40)

              img10=Image.open(r"images\facia.webp")
              img10=img10.resize((220,220),Image.LANCZOS)
              self.photoimg10=ImageTk.PhotoImage(img10)
              b7=Button(bg_img,image=self.photoimg10,cursor="hand2")
              b7.place(x=725,y=340,width=220,height=220)
              b2_3=Button(bg_img,text="Developers",cursor="hand2",font=("times new roman",15,"bold"),fg="#00004d",bg="white",justify="center")
              b2_3.place(x=725,y=520,width=220,height=40)

              img11=Image.open(r"images\facia.webp")
              img11=img11.resize((220,220),Image.LANCZOS)
              self.photoimg11=ImageTk.PhotoImage(img11)
              b7=Button(bg_img,image=self.photoimg11,cursor="hand2")
              b7.place(x=1040,y=340,width=220,height=220)
              b2_4=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),fg="#00004d",bg="white",justify="center")
              b2_4.place(x=1040,y=520,width=220,height=40)

def open_img(self):
      os.startfiles("data")

def student_details(self):
      self.new_window=Toplevel(self.root)
      self.app=Student(self.new_window)





if __name__ == "__main__":
    root =Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()