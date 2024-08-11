# function arguments
def print_info(name,age=20):
    print(f"Hi, my name is {name}, age is {age} ")
def generate_email(*snames): # sname = ('ahmad','samar')
    print(type(snames))
    emails=[]
    for s in snames:
        emails.append(f"{s}@std.uop.edu.jo")
    return emails
#p = print_info() # returns None
#print(p)
emails= generate_email('ahmad','samar')
names = ['ahmad','samar','zaid']
emails= generate_email(*names)
print(emails)
#print_info("Hossam",45)
#print_info("Hossam")
print_info(age = 40,name = "Hossam")