n = int(input("Enter No of Integers:"))
sum = 0
for i in range(1,n+1):
    while True:
        mark = None
        try:
            mark = int( input("Enter mark:") )
        except:
            mark = -1
        if 0<=mark<=100:
            sum += mark
            break
        else:
            print("Invalid No")
print('Average = ',sum/n)