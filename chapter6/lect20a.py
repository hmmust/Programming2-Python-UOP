str1 = "  Ahmad is a student in UOP  "
s1 = "is" in str1
#print(type(s1))
print(s1)
print(str1.lower())
print(str1.upper())
print(str1)
#print(str1.capitalize())
#print(str1)
print(f"##{str1.lstrip()}##")
print(f"##{str1.rstrip()}##")
print(f"##{str1.strip()}##")

print(str1.find("is"))
print(str1.strip().lower().find("is"))
print(str1.strip().lower().startswith("ahmad"))
print(str1.strip().lower().endswith("uop"))
print(str1.find("is",9))
# extra searching in regular expressions  re
print(str1.isnumeric())
print("1".isnumeric())
print("1.5".isnumeric())

print(str1.strip().split(" "))



