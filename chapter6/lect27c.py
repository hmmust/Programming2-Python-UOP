# generator expressions - list/dictionary comprehension

names = ['Jihad','Aya','Raneem','Khalid','','']
emails= [ f"{n.lower()}@std.uop.edu.jo" for n in names if n!= '']
emails_d= { n.lower():f"{n.lower()}@std.uop.edu.jo" for n in names if n!= ''}

print(emails)
print(emails_d)