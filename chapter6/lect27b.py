# generator function
names = ['Jihad','Aya','Raneem','Khalid']

def generate_f():
    yield "Dana"
    yield "Fawzi"
    yield "khalid"

def generate_emails(list_names):
    for n in list_names:
       yield f"{n.lower()}@uop.edu.jo"

def squares(*nos):
    for n in nos:
        yield n**2

for i in squares(10,15,30):
    print(i)

for e in generate_emails(names):
    print(e)

print(list(generate_emails(names)))
print([*generate_emails(names)])
print([*range(1,11)])
print(list(range(1,11)))
print([*enumerate(names)])


"""n_iter= iter(generate_f())
print(next(n_iter))
print(next(n_iter))
print(next(n_iter))"""

"""for i in generate_f():
    print(i)
"""



