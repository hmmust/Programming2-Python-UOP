nums = [2,3,4,5]
name= "Zain"
gpa = 3.855
age = 6
salary = 4544544.544
print(f"nums = {len(nums)}")
print(f"nums = {nums*2}")
print(f"name = {name[0]}")
print(f"gpa = {gpa:0.2f}")
print(f"age = {age:03}")
print(f"salary = {salary:,.2f}$")

print(f"age = {age:#^30}")
print(f"name = {name:#^30}")
print(f"salary = {salary:#^30}")

print("age = %i" % age)
print("age = %i and name = %s " % (age,name))

s1 = "age = {a} and name = {b}"
print(s1.format(a=age,b=name.upper()))
print(s1.format(a=age,b=name.lower()))