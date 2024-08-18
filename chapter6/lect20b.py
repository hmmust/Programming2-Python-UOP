# Enter 5 students name, firstexam, second exam marks,
# then find the max/largest total mark using function
def get_total(line):
    line = line.split(",")
    line[0] = line[0].strip()
    line[1] = int(line[1].strip())
    line[2] = int(line[2].strip())
    total = line[1] + line[2]
    return total

total_marks = []
for _ in range(3):
    input_string = input("Enter name,first, second:")
    total_mark = get_total(input_string)
    total_marks.append(total_mark)

print(max(total_marks))


