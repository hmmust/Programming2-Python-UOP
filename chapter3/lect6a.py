names = ['Ahmad','Khalid','Mira']
print(names)

"""c = 0
while c<3:
    print(names[c])
    c+=1"""

for n in names: #n=Mira
    print(n)

student_name = "Saed Ahmad"
for i in student_name:
    print(i,"_",end="")

"""for i in [1,2,3,4,5]:
    print(i)"""
print("##############")

for i in range(1,6): #=> [1,2,3,4,5]
    print(i)
print("##############")
for i in range(1,6,2): #=> [1,3,5]
    print(i)
print("##############")
for i in range(5,0,-1):
    print(i)
print("##############")
for i in range(5,0): #=> []
    print(i)