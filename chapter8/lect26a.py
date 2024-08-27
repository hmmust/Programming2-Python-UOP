from lect25 import BSStudent
import os


if os.path.exists("data1.txt"):
    fh=open("data1.txt",'rt')
    students= []
    for line in fh:
        line= line.replace("\n","").split(",")
        s1 =  BSStudent(int(line[0]),line[1],line[2], float(line[3]))
        s1.generate_email()
        s1.generate_password()
        students.append(s1)
    fh.close()
    if os.path.exists("data1_new.txt"):
        os.remove("data1_new.txt")

    fh=open("data1_new.txt",'at') # mode wt
    for s in students:
       fh.write(f'{s}\n')
    fh.close()
else:
    print("file not exist")