import tkinter
from tkinter import *
from tkinter import messagebox

class Student:
    def __init__(self,id,name,age,email):
        self.id=id
        self.name = name
        self.age=age
        self.email=email
    def __str__(self):
        return f'{self.id},{self.name},{self.age},{self.email}'
    def check_info(self):
        if len(self.name.split(" ")) != 3:
            return False
        else:
            return True

def save_information():
    id = id_e.get()
    name = name_e.get()
    age = age_e.get()
    email = email_e.get()
    s1 = Student(id,name,age,email)

    if s1.check_info():
        fh = open("student_info.txt","at")
        fh.write(f'{s1}\n')
        fh.close()
    else:
        messagebox.showerror("Error","Some student information is Invalid")

main = tkinter.Tk()
main.title("Student Information")
id_l= Label(main,text="ID:")
id_l.pack()
id_e= Entry(main)
id_e.pack()

name_l= Label(main,text="Name:")
name_l.pack()
name_e= Entry(main)
name_e.pack()

age_l= Label(main,text="Age:")
age_l.pack()
age_e= Entry(main)
age_e.pack()

email_l= Label(main,text="Email:")
email_l.pack()
email_e= Entry(main)
email_e.pack()

ok_b= Button(main,text="Save",command=save_information)
ok_b.pack()

main.mainloop()
