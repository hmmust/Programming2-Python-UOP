"""
    Write a program that enters number of students (n)
    and enter their names and marks, store them in a
    list, find the maximum mark (print student name)
    and find the average of these marks
"""
n = int( input("Enter number of students:") )
max,avg,sum = 0,0,0
max_student = ""
marks = []
names = []
for i in range(0,n):
    name = input("Enter name:")
    mark = int( input("Enter mark:") )
    marks.append(mark)
    names.append(name)
    sum += mark
    if mark >= max:
        max = mark
        max_student = name
avg = sum /n
print(marks,names)
print(avg,max)

