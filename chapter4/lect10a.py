# tuple application with lists + range
# Merge for list of student info(name,first,second)
# compute the sum of first and second and append to list

names = ["Saed","Jihad","Abdullah","Aya"]
#del names[0] # names.pop(0)
first = [22,17,21,19]
second = [18,22,20,23]
marks_sum = []
"""for f,s in zip(first,second):
    marks_sum.append(f+s) # [22+18, 17+22 ... ]"""
"""for i,f in enumerate(first):
    marks_sum.append(f + second[i])"""
for i in range(len(first)) :
    marks_sum.append( first[i] + second[i] )

students = list(zip(names,first,second,marks_sum))
max_sum = -1
max_index = -1
for i in range(len(students)) :
    if max_sum < students[i][3]:
        max_sum = students[i][3]
        max_index = i

print(max_index,max_sum)