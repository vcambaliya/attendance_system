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
              
              self.var_dep=StringVar()
              self.var_course=StringVar()
              self.var_year=StringVar()
              self.var_semester=StringVar()
              self.var_std_id=StringVar()
              self.var_std_name=StringVar()
              self.var_div=StringVar()
              self.var_roll=StringVar()
              self.var_gender=StringVar()
              self.var_dob=StringVar()
              self.var_email=StringVar()
              self.var_phone=StringVar()
              self.var_address=StringVar()
              self.var_faculty=StringVar()
              

              img=Image.open(r"E:\projecttt\Attendance_System\images\stud1.jpeg")
              img=img.resize((500,120),Image.LANCZOS)
              self.photoimg=ImageTk.PhotoImage(img)

              f_label=Label(self.root,image=self.photoimg)
              f_label.place(x=0,y=0,width=450,height=120)

              img1=Image.open(r"E:\projecttt\Attendance_System\images\stud2.jpeg")
              img1=img1.resize((500,120),Image.LANCZOS)
              self.photoimg1=ImageTk.PhotoImage(img1)

              f_label=Label(self.root,image=self.photoimg1)
              f_label.place(x=450,y=0,width=460,height=120)

              img2=Image.open(r"E:\projecttt\Attendance_System\images\stud3.jpeg")
              img2=img2.resize((500,120),Image.LANCZOS)
              self.photoimg2=ImageTk.PhotoImage(img2)
              f_label=Label(self.root,image=self.photoimg2)
              f_label.place(x=910,y=0,width=450,height=120)
              
              img3=Image.open(r"E:\projecttt\Attendance_System\images\facia.webp")
              img3=img3.resize((1530,710),Image.LANCZOS)
              self.photoimg3=ImageTk.PhotoImage(img3)
              bg_img=Label(self.root,image=self.photoimg3)
              bg_img.place(x=0,y=120,width=1530,height=690)
              title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",32,"bold"),fg="#00004d",bg="white",justify="center")
              title_lbl.place(x=0,y=0,width=1380,height=40)

              main_frame=Frame(bg_img,bd=2)
              main_frame.place(x=10,y=44,width=1330,height=530)

              left_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
              left_frame.place(x=10,y=0,width=650,height=535)
              
              left_img=Image.open(r"E:\projecttt\Attendance_System\images\frame1.webp")
              left_img=left_img.resize((720,110),Image.LANCZOS)
              self.photoimg_left=ImageTk.PhotoImage(left_img)
              f_label=Label(left_frame,image=self.photoimg_left)
              f_label.place(x=5,y=0,width=635,height=105)

              #current course
              current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new roman",12,"bold"))
              current_course_frame.place(x=5,y=103,width=635,height=100)

              dep_label=Label(current_course_frame,bg="white",text="Department : ",font=("times new roman",12,"bold"))
              dep_label.grid(row=0,column=0,padx=10)
              dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12),width=17,state="read only")
              dep_combo["values"]=("Select Department","Computer Application","B.Tech","Management","FoCA")
              dep_combo.current(0)
              dep_combo.grid(row=0,column=1,padx=2,pady=6,sticky=W)

              course_label=Label(current_course_frame,bg="white",text="Course : ",font=("times new roman",12,"bold"))
              course_label.grid(row=0,column=2,padx=10)
              course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12),width=17,state="read only")
              course_combo["values"]=("Select Course","MCA","BCA","B.Honr","Data Science")
              course_combo.current(0)
              course_combo.grid(row=0,column=3,padx=2,pady=6,sticky=W)

              year_label=Label(current_course_frame,bg="white",text="Year : ",font=("times new roman",12,"bold"))
              year_label.grid(row=1,column=0,padx=10)
              year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12),width=17,state="read only")
              year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
              year_combo.current(0)
              year_combo.grid(row=1,column=1,padx=2,pady=6,sticky=W)

              semester_label=Label(current_course_frame,bg="white",text="Semester : ",font=("times new roman",12,"bold"))
              semester_label.grid(row=1,column=2,padx=10)
              semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12),width=17,state="read only")
              semester_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6")
              semester_combo.current(0)
              semester_combo.grid(row=1,column=3,padx=2,pady=6,sticky=W)



              class_student_frame=LabelFrame(left_frame,bd=4,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
              class_student_frame.place(x=5,y=203,width=635,height=305)
              

              studentId_label=Label(class_student_frame,bd=4,bg="white",text="StudentID : ",font=("times new roman",12,"bold"))
              studentId_label.grid(row=0,column=0,padx=6,sticky=W)
              studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=16,font=("times new roman",12,"bold"))
              studentID_entry.grid(row=0,column=1,padx=6,sticky=W)
              
              studentName_label=Label(class_student_frame,bd=4,bg="white",text="Student Name : ",font=("times new roman",12,"bold"))
              studentName_label.grid(row=0,column=2,padx=6,sticky=W)
              studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=16,font=("times new roman",12,"bold"))
              studentName_entry.grid(row=0,column=3,padx=6,pady=5,sticky=W)

              studentdiv_label=Label(class_student_frame,bd=4,bg="white",text="Student Division : ",font=("times new roman",12,"bold"))
              studentdiv_label.grid(row=1,column=0,padx=6,sticky=W)
              #studentdiv_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=16,font=("times new roman",12,"bold"))
              #studentdiv_entry.grid(row=1,column=1,padx=6,pady=5,sticky=W)              
              
              division_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12),width=14,state="read only")
              division_combo["values"]=("A","B","C")
              division_combo.current(0)
              division_combo.grid(row=1,column=1,padx=2,pady=6,sticky=W)



              studentroll_label=Label(class_student_frame,bd=4,bg="white",text="Roll No. : ",font=("times new roman",12,"bold"))
              studentroll_label.grid(row=1,column=2,padx=6,sticky=W)
              studentroll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=16,font=("times new roman",12,"bold"))
              studentroll_entry.grid(row=1,column=3,padx=6,pady=5,sticky=W)

              studentgender_label=Label(class_student_frame,bd=4,bg="white",text="Gender : ",font=("times new roman",12,"bold"))
              studentgender_label.grid(row=2,column=0,padx=6,sticky=W)
              gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12),width=14,state="read only")
              gender_combo["values"]=("Male","Female","Other")
              gender_combo.current(0)
              gender_combo.grid(row=2,column=1,padx=2,pady=6,sticky=W)


              studentdob_label=Label(class_student_frame,bd=4,bg="white",text="DOB : ",font=("times new roman",12,"bold"))
              studentdob_label.grid(row=2,column=2,padx=6,sticky=W)
              studentdob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=16,font=("times new roman",12,"bold"))
              studentdob_entry.grid(row=2,column=3,padx=6,pady=5,sticky=W)

              studentemail_label=Label(class_student_frame,bd=4,bg="white",text="Email : ",font=("times new roman",12,"bold"))
              studentemail_label.grid(row=3,column=0,padx=6,sticky=W)
              studentemail_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=16,font=("times new roman",12,"bold"))
              studentemail_entry.grid(row=3,column=1,padx=6,pady=5,sticky=W)

              studentphn_label=Label(class_student_frame,bd=4,bg="white",text="Phone No. : ",font=("times new roman",12,"bold"))
              studentphn_label.grid(row=3,column=2,padx=6,sticky=W)
              studentphn_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=16,font=("times new roman",12,"bold"))
              studentphn_entry.grid(row=3,column=3,padx=6,pady=5,sticky=W)

              studentadd_label=Label(class_student_frame,bd=4,bg="white",text="Address : ",font=("times new roman",12,"bold"))
              studentadd_label.grid(row=4,column=0,padx=6,sticky=W)
              studentadd_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=16,font=("times new roman",12,"bold"))
              studentadd_entry.grid(row=4,column=1,padx=6,pady=5,sticky=W)

              studenttech_label=Label(class_student_frame,bd=4,bg="white",text="Faculty Name : ",font=("times new roman",12,"bold"))
              studenttech_label.grid(row=4,column=2,padx=6,sticky=W)
              studenttech_entry=ttk.Entry(class_student_frame,textvariable=self.var_faculty,width=16,font=("times new roman",12,"bold"))
              studenttech_entry.grid(row=4,column=3,padx=6,pady=5,sticky=W)

              self.var_radio1=StringVar()
              radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo Sample",value="Yes")
              radiobtn1.grid(row=6,column=0)

             
              radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
              radiobtn2.grid(row=6,column=1)

              btn_frame=Frame(class_student_frame,bg="white",bd=2,relief=RIDGE)
              btn_frame.place(x=5,y=198,width=623,height=35)

              save_bt=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",12,"bold"),bg="#00004d",fg="white")
              save_bt.grid(row=0,column=0)

              update_bt=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",12,"bold"),bg="#00004d",fg="white")
              update_bt.grid(row=0,column=1)
            
              delete_bt=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",12,"bold"),bg="#00004d",fg="white")
              delete_bt.grid(row=0,column=2)

              reset_bt=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="#00004d",fg="white")
              reset_bt.grid(row=0,column=3)

              btn_frame1=Frame(class_student_frame,bg="white",bd=2,relief=RIDGE)
              btn_frame1.place(x=5,y=233,width=623,height=35)

              take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,width=34,font=("times new roman",12,"bold"),bg="#00004d",fg="white")
              take_photo_btn.grid(row=0,column=0)

              update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=34,font=("times new roman",12,"bold"),bg="#00004d",fg="white")
              update_photo_btn.grid(row=0,column=1)

              
              right_frame=LabelFrame(main_frame,bd=4,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
              right_frame.place(x=670,y=0,width=650,height=535)

              right_img=Image.open(r"E:\projecttt\Attendance_System\images\right.jpeg")
              right_img=right_img.resize((720,110),Image.LANCZOS)
              self.photoimg_right=ImageTk.PhotoImage(right_img)
              f_label1=Label(right_frame,image=self.photoimg_right)
              f_label1.place(x=5,y=0,width=635,height=105)


              Search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
              Search_frame.place(x=5,y=103,width=635,height=60)

              search_label=Label(Search_frame,bg="red",fg="white",text="Search By. : ",font=("times new roman",12,"bold"))
              search_label.grid(row=0,column=0,padx=2,pady=3,sticky=W)

              search_combo=ttk.Combobox(Search_frame,font=("times new roman",12),width=14,state="read only")
              search_combo["values"]=("Select","Roll_No","Phone_No")
              search_combo.current(0)
              search_combo.grid(row=0,column=1,padx=2,pady=3,sticky=W)

              search_entry=ttk.Entry(Search_frame,width=14,font=("times new roman",12,"bold"))
              search_entry.grid(row=0,column=2,padx=2,pady=3,sticky=W)

              search_btn=Button(Search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="#00004d",fg="white")
              search_btn.grid(row=0,column=3)

              show_btn=Button(Search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="#00004d",fg="white")
              show_btn.grid(row=0,column=4)

              table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
              table_frame.place(x=5,y=170,width=630,height=330)

              scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
              scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

              self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","faculty","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
              scroll_x.pack(side=BOTTOM,fill=X)
              scroll_y.pack(side=RIGHT,fill=Y)

              scroll_x.config(command=self.student_table.xview)
              scroll_y.config(command=self.student_table.yview)

              self.student_table.heading("dep",text="Department",)
              self.student_table.heading("course",text="Course")
              self.student_table.heading("year",text="Year")
              self.student_table.heading("sem",text="Semester")
              self.student_table.heading("id",text="StudentId")
              self.student_table.heading("name",text="Name")
              self.student_table.heading("div",text="Division")
              self.student_table.heading("roll",text="Roll No.")
              self.student_table.heading("gender",text="Gender")
              self.student_table.heading("dob",text="DOB")
              self.student_table.heading("email",text="Email")
              self.student_table.heading("phone",text="Phone")
              self.student_table.heading("address",text="Address")
              self.student_table.heading("faculty",text="Faculty")
              self.student_table.heading("photo",text="PhotoSampleStatus")
              self.student_table["show"]="headings"
              self.student_table.column("dep",width=100)
              self.student_table.column("course",width=100)
              self.student_table.column("year",width=100)
              self.student_table.column("sem",width=100)
              self.student_table.column("id",width=100)
              self.student_table.column("name",width=100)
              self.student_table.column("roll",width=100)
              self.student_table.column("gender",width=100)
              self.student_table.column("div",width=100)
              self.student_table.column("dob",width=100)
              self.student_table.column("email",width=100)
              self.student_table.column("phone",width=100)
              self.student_table.column("address",width=100)
              self.student_table.column("faculty",width=100)
              self.student_table.column("photo",width=150)
              self.student_table.pack(fill=BOTH,expand=1)
              self.student_table.bind("<ButtonRelease>",self.get_cursor)
              self.fetch_data()
        def add_data(self):
              if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                  messagebox.showerror("Error","All Fields are required")
              else:
                  try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Vidhi@2022",database='student_attendence')
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),
                                                                                                          self.var_course.get(),
                                                                                                          self.var_year.get(),
                                                                                                          self.var_semester.get(),
                                                                                                          self.var_std_id.get(),
                                                                                                          self.var_std_name.get(),
                                                                                                          self.var_div.get(),
                                                                                                          self.var_roll.get(),
                                                                                                          self.var_gender.get(),
                                                                                                          self.var_dob.get(),
                                                                                                          self.var_email.get(),
                                                                                                          self.var_phone.get(),
                                                                                                          self.var_address.get(),
                                                                                                          self.var_faculty.get(),
                                                                                                          self.var_radio1.get()
                                                                                                          ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
                  except Exception as es:
                        messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)
              
        def fetch_data(self):
              conn=mysql.connector.connect(host="localhost",username="root",password="Vidhi@2022",database='student_attendence')
              my_cursor=conn.cursor()
              my_cursor.execute("select * from student")
              data=my_cursor.fetchall()

              if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                          self.student_table.insert("",END,values=i)
                    conn.commit()
              conn.close()


        def get_cursor(self,event=""):
              cursor_focus=self.student_table.focus()
              content=self.student_table.item(cursor_focus)
              data=content["values"]

              self.var_dep.set(data[0]),
              self.var_course.set(data[1]),
              self.var_year.set(data[2]),
              self.var_semester.set(data[3]),
              self.var_std_id.set(data[4]),           
              self.var_std_name.set(data[5]),
              self.var_div.set(data[6]),
              self.var_roll.set(data[7]),
              self.var_gender.set(data[8]),
              self.var_dob.set(data[9]),
              self.var_email.set(data[10]),
              self.var_phone.set(data[11]),
              self.var_address.set(data[12]),
              self.var_faculty.set(data[13]),
              self.var_radio1.set(data[14])

        def update_data(self):
              if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                  messagebox.showerror("Error","All Fields are required")
              else:
                  try:
                        Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                        if Update>0:
                              conn=mysql.connector.connect(host="localhost",username="root",password="Vidhi@2022",database='student_attendence')
                              my_cursor=conn.cursor()
                              my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,faculty=%s,photosample=%s where student_id=%s",(
                                                                                                          self.var_dep.get(),
                                                                                                          self.var_course.get(),  
                                                                                                          self.var_year.get(),
                                                                                                          self.var_semester.get(),
                                                                                                          self.var_std_name.get(),
                                                                                                          self.var_div.get(),
                                                                                                          self.var_roll.get(),
                                                                                                          self.var_gender.get(),
                                                                                                          self.var_dob.get(),
                                                                                                          self.var_email.get(),
                                                                                                          self.var_phone.get(),
                                                                                                          self.var_address.get(),
                                                                                                          self.var_faculty.get(),
                                                                                                          self.var_radio1.get(),
                                                                                                          self.var_std_id.get()
                              ))
                        else:
                              if not Update:
                                    return
                        messagebox.showinfo("Sucess","Student details Updated sucessfully",parent=self.root)
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                  except Exception as es:
                        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        def delete_data(self):
              if self.var_std_id.get()=="":
                    messagebox.showerror("Error","Student id must be required",paremt=self.root)
              else:
                    try:
                          delete=messagebox.askyesno("Delete","Do you want to delete this student record",parent=self.root)
                          if delete>0:
                              conn=mysql.connector.connect(host="localhost",username="root",password="Vidhi@2022",database='student_attendence')
                              my_cursor=conn.cursor()
                              sql="delete from student where student_id=%s"
                              val=(self.var_std_id.get(),)
                              my_cursor.execute(sql,val)
                          else:
                                if not delete:
                                      return
                          conn.commit()
                          self.fetch_data()
                          conn.close()
                          messagebox.showinfo("Delete","Successfully Deleted Student Data",parent=self.root)

                    except Exception as es:
                          messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        def reset_data(self):
                  self.var_dep.set("Select Department")
                  self.var_course.set("Select Course")
                  self.var_year.set("Select Year")
                  self.var_semester.set("Select Semester")
                  self.var_std_id.set("")
                  self.var_std_name.set("")
                  self.var_div.set("Select Division")
                  self.var_roll.set("")
                  self.var_gender.set("")
                  self.var_dob.set("")
                  self.var_email.set("")
                  self.var_phone.set("")
                  self.var_address.set("")
                  self.var_faculty.set("")
                  self.var_radio1.set("")
                                    
#===================generate data set or take photo=====================

        def generate_dataset(self):
              if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                  messagebox.showerror("Error","All Fields are required")
              else:
                  try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="Vidhi@2022",database="student_attendence")
                        my_cursor=conn.cursor()
                        my_cursor.execute("select * from student")
                        myresult=my_cursor.fetchall()
                        id=0
                        for x in myresult:
                              id+=1
                        my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,faculty=%s,photosample=%s where student_id=%s",(
                                                                                                          self.var_dep.get(),
                                                                                                          self.var_course.get(),  
                                                                                                          self.var_year.get(),
                                                                                                          self.var_semester.get(),
                                                                                                          self.var_std_name.get(),
                                                                                                          self.var_div.get(),
                                                                                                          self.var_roll.get(),
                                                                                                          self.var_gender.get(),
                                                                                                          self.var_dob.get(),
                                                                                                          self.var_email.get(),
                                                                                                          self.var_phone.get(),
                                                                                                          self.var_address.get(),
                                                                                                          self.var_faculty.get(),
                                                                                                          self.var_radio1.get(),
                                                                                                          self.var_std_id.get()==id+1
                              ))
                        conn.commit()
                        self.fetch_data()
                        self.reset_data()
                        conn.close()
                  
#========================Load predefine data on face frontals froom opencv
                        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                        def face_cropped(img):
                              gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                              faces=face_classifier.detectMultiScale(gray,1.3,5)

                              for(x,y,w,h) in faces:
                                    cropped_face=img[y:y+h,x:x+w]
                                    return cropped_face
                        
                        cap=cv2.VideoCapture(0)
                        img_id=0
                        while True:
                              ret,faceframe=cap.read()
                              if face_cropped(faceframe) is not None:
                                    img_id+=1
                                    face=cv2.resize(face_cropped(faceframe),(450,450))
                                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                    file_name_path=f"face_data/user.{str(id)}.{str(img_id)}.jpg"
                                    cv2.imwrite(file_name_path,face)
                                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                    cv2.imshow("Cropped Face",face)

                              if cv2.waitKey(1)==13 or int(img_id)==100:
                                    break
                        cap.release()
                        cv2.destroyAllWindows()
                        messagebox.showinfo("Result","Successfully Dataset Generated")
                  except Exception as es:
                       messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


if __name__ == "__main__":
    root =Tk()
    obj=Student(root)
    root.mainloop()