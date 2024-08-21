"""Read data1,txt, compute the average of the total
 marks of students"""

# open file and store in file handler
fh = open("data1.txt","rt") # arg1:file, arg2:mode (r,w,a),type (b/t)
"""for l in fh: #iteration on each line
    print(l.replace("\n","")) # replace "\n" with nothing
"""
"""f_content = fh.read()
print(type(f_content))
print(f_content.split("\n"))"""

f_content = fh.readlines()
f_content_output = []
fh.close()
total = 0
for l in f_content:
    line = l.replace("\n","").split(",")
    line[1] = int(line[1] )
    line[2] = int(line[2])
    line.append(line[1]+line[2]) # optional
    f_content_output.append(f'{line[0]},{line[1]},{line[2]},{line[3]}\n')
    total+= line[3] # total += line[1]+line[2]
    #print(line)
print("Average Mark=",total/len(f_content))
fh=open("data1_t.txt","wt")
fh.writelines(f_content_output)
fh.close()
#print(f_content_output)