for i in range (1,6): # outer loop (rows)
    for j in range(1,i+1): # inner loop (columns)
        print("*", end="")
    print("")
"""
* (i=1, 1->2)
** (i=2, 1->3)
***(i=3, 1->4)
****(i=4, 1->5)
*****(i=5, 1->6)
"""
print("-------------------------")

for i in range (5,0,-1): # outer loop (rows)
    for j in range(1,i+1): # inner loop (columns)
        print("*", end="")
    print("")

print("-------------------------")

for i in range (1,6): # outer loop (rows)
    for j in range(1,5-i+1): # inner loop 1 (spaces)
        print(" ", end="")
    for j in range(1,i+1): # inner loop 2 (stars)
        print("*", end="")
    print("")

