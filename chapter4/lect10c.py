# Merge for list of student info(name,first,second)
# print average mark, and number of marks above 40

names = ["Saed","Jihad","Abdullah","Aya"]
first = [22,17,21,19]
second = [18,22,20,23]
marks_sum = []
for i in range(len(first)) :
    marks_sum.append( first[i] + second[i] )
nmarks = 0
smarks = 0
for mark in marks_sum:
    smarks += mark
    if mark > 40:
        nmarks += 1
print(smarks/len(marks_sum))
print("number of marks above 40:",nmarks)