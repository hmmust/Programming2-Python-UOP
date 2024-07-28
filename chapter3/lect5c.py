k = int(input("Enter a number:"))
result = ""
while k != 0:
    r = k % 2
   # print(r,end="")
    result = str(r) + result
    k = k // 2
print(result)