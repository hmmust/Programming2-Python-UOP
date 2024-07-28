n = int( input("Enter No of Integers:") )
i=0
sum = 0
while i <n:
    mark = None
    try:
        mark = int( input("Enter mark:") )
    except:
        mark = -1
    if 0<=mark<=100:
        sum += mark
        i+=1
    else:
        print("Invalid No")
print('Average = ',sum/n)