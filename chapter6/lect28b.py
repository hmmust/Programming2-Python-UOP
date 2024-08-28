# lambda function (anonymous functions)
students = ['Saed Abdhaleem','Jihad Karam',"Abdullah Ismail"]

sum_numbers= lambda a,b:a+b
f_name = lambda s:s.split(" ")[0]
s_name = lambda s:s.split(" ")[1].lower()
students.sort(key=s_name)

print(students)

students_info = [['Saed',21,4],['Jihad',20,3.4],["Abdullah",19,3.5]]
c_student = lambda a:a[2]
students_info.sort(key=c_student)
students_info.reverse()
print(students_info)
"""print(type(sum_numbers))
print(sum_numbers(1,2))
print(f_name('Saed Abdhaleem'))"""