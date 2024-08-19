# GUI -tkinter
import tkinter
from tkinter import Button,Label,Entry,messagebox,filedialog

def btn_click():
    try:
        no1 = int(e_no1.get())
        no2 = int(e_no2.get())
        r = no1+no2
        l_result['text'] = r
        # messagebox.showwarning("Project",f"{no1} + {no2}= {r}")
    except:
        messagebox.showerror("Error","Enter valid numbers")

# 1 create main window object
m = tkinter.Tk()
m.config(width=500,height=500, bg="#faefd2")
m.title("First Project")
# 2 add controls
l1= Label(text="Number 1",padx=5,pady=5)
l1.pack()
e_no1 = Entry(width=30)
e_no1.pack()
l2= Label(text="Number 2",padx=5,pady=5)
l2.pack()
e_no2 = Entry(width=30)
e_no2.pack()
l_result= Label(text="result",padx=5,pady=5)
l_result.pack()
b_calc = Button(text="Calculate",padx=5,pady=5, command=btn_click)
b_calc.pack()






# 3 show window
m.mainloop()