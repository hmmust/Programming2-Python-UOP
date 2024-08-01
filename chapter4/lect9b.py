# tuple application with lists
marks = [15,18,25,20]
names = ["Saed","Jihad","Abdullah","Aya"]
all_students = zip(names,marks)
for name,mark in all_students:
    print(name,mark)