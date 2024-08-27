# iteratable objects
name = ['Jihad','Aya','Raneem','Khalid']
name_iter = iter(name)
while True:
    try:
        print(next(name_iter))
    except StopIteration:
        break




