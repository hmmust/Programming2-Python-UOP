"""mark = float( input("Enter Mark:") )
#if mark >= 90 and mark <=100:
if 90<=mark<=100:
    print('A')
#elif mark >= 80 and mark <90:
elif 80 <=mark< 90:
    print('B')
#elif mark >= 70 and mark <80:
elif 70 <= mark < 80:
    print('C')
#elif mark >= 60 and mark <70:
elif 60 <= mark < 70:
    print('D')
#elif mark < 60 and mark >=0:
elif 0 <= mark < 60:
    print("F")
else:
    pass
    #print('Invalid')"""

mark,gpa = 90,3.5
"""if mark is not 90:
    print("Good")
else:
    print("Outstanding")"""
if mark in (90,89,91):
    print("Outstanding")
else:
    print("Good")


