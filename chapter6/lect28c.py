# lambda function (anonymous functions) - filter
students = ['Saed Abdhaleem','Jihad Karam',"Abdullah Ismail"]
students_info = [['Saed',21,4],['Jihad',20,3.4],["Abdullah",19,3.5]]
filter_gpa = lambda s: s[2] >=3.5

print([*filter(filter_gpa,students_info)])
print([*filter(lambda s: s[1] %2 ==0,students_info)])

generate_email = lambda s: f'{s.split(' ')[0].lower()}@uop.edu.jo'
emails = list(map(generate_email,students))
print(emails)