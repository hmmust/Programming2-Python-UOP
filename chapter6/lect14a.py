#print_info() raise error because function
#               call before declaration
def print_info():
    print("Hi, my name is Hossam")
def print_info2(name):
    print(f"Hi, my name is {name}")
def enter_info():
    name= input("Enter name:")
    return name
def collect_info(no):
    names=[]
    for i in range(0,no):
        n = enter_info()
        names.append(n)
    return names
def generate_email(snames):
    if type(snames) in (list, tuple) and len(snames) > 0 :
        emails=[]
        for s in snames:
            emails.append(f"{s}@std.uop.edu.jo")
        return emails
    else:
        raise Exception("Function input error: not list or tuple")
"""print_info()
n = enter_info()
print_info2(n)"""
student_names = collect_info(4)
student_emails = generate_email(student_names)
print(student_emails)

