#list declaration
name = []
names = list()
marks = [25,30,40,15,True,"Rand",[["A","B"],2]]
print(marks)
for i in marks:
    print(i)
print(type(marks))
#list indexing
print(marks[0])
#print(marks[50]) #valid
print(len(marks))
print( marks[len(marks)-1] ) # marks[6]
print(marks[6][0][0])
#merging
marks = [25,30,40,15]
marks2= [17,24]
marks_all = marks + marks2
marks_all.sort()
marks_all.reverse()
#marks_all= sorted(marks_all)
print(marks_all)
marks_all.append(99)
marks_all.insert(0,100)
print(marks_all)


