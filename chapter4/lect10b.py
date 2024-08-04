# Merge for list of student info(name,first,second)
# print all student with sum of mark >= 40

names = ["Saed","Jihad","Abdullah","Aya"]
first = [22,17,21,19]
second = [18,22,20,23]
marks_sum = []
for i in range(len(first)) :
    marks_sum.append( first[i] + second[i] )

students = list(zip(names,first,second,marks_sum))
result_index = []
for i in range(len(students)) :
    if students[i][3] >= 40:
        result_index.append((i))

print(result_index)