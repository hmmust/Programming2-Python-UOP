from lect25 import Student,BSStudent

"""s1 = Student()
s1.id= 20201
s1.name = "Saed"
s1.spec = "IS"
print(s1.name)"""
s1 = Student(spec="IS", id= 20220, name="Saed")
#s2 = Student(spec="IS", id= 20220, name="Saed")
s2 = BSStudent(spec="DSAI", id= 20203, name="Jihad",gpa=3.5)
print(s1)

del s1
print(s2)

#print(s1 == s2)