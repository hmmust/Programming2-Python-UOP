"""Create Gui with a button to Read data1.txt, generate email,password, write in new file
 data1_users.csv"""
import random
import tkinter
from tkinter import Button,messagebox,filedialog
from tkinter import Button,messagebox,filedialog

filename= ""
def generate_accounts():
    char_pass= ["@",'$',"_",".","-"]

    fh = open(filename,"rt")
    f_result= []
    for l in fh:
        username = l.replace("\n","").split(",")[0].lower()
        username = f'{username}@std.uop.edu.jo'
        password = f'{username[0].upper()}{random.choice(char_pass)}{random.randint(100, 999)}'
        f_result.append(f'{username},{password}\n')
    fh.close()
    fh2 = open("data1_users.csv",'wt')
    fh2.writelines(f_result)
    fh2.close()
    messagebox.showinfo(message="File Generated")

def select_input_file():
    filename= filedialog.askopenfilename()

m = tkinter.Tk()
b_file = Button(m,text="Select File",width=50,pady=10,padx=10,command=select_input_file)
b_file.pack()
b_gen = Button(m,text="Generate Accounts",width=50,pady=10,padx=10,command=generate_accounts)
b_gen.pack()

m.mainloop()