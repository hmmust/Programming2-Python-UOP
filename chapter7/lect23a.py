"""Read data1.txt, generate email,password, write in new file
 data1_users.csv"""
import random
char_pass= ["@",'$',"_",".","-"]

fh = open("data1.txt","rt")
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
