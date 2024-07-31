"""
    Write a program that enters number of students (n)
    and enter their names and marks, store them in a
    list, find the maximum mark (print all student names)
"""
n = int( input("Enter number of students:") )
max = 0
max_students = []  #string atomic , list multivalue
marks = []
names = []
for i in range(0,n):
    name = input("Enter name:")
    mark = int( input("Enter mark:") )
    marks.append(mark)
    names.append(name)
    if mark > max:
        max = mark
        max_students.clear()
        max_students.append(name)
    elif mark == max:
        max_students.append(name)
print(marks,names)
print(max)
print(max_students)

