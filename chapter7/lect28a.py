# using list comprehesion

"""Read data1,txt, generate email, password
 and store in other file data1_n.txt"""
import random

# open file and store in file handler
fh = open("data1.txt","rt") # arg1:file, arg2:mode (r,w,a),type (b/t)
students = fh.readlines()
students= [s.replace("\n","").split(",") for s in students]
students_accounts= [[f"{s[0].lower()}@uop.edu.jo",f"{s[0][0].lower()}_{random.randint(100,999)}"] for s in students]
#students_accounts_dict= { f"{s[0].lower()}@uop.edu.jo": f"{s[0][0].lower()}_{random.randint(100,999)}" for s in students}
fh=open("data1_n.txt","wt")
fh.writelines([f'{s[0]},{s[1]}\n'for s in students_accounts])
fh.close()

#print(f_content_output)