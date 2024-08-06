# Dictionaries example - convert list to dictionary
dept_counts = [4, 2, 3, 2]
depts = ['DSAI', 'CS', 'SE', 'IS']

specs =  dict(zip(depts,dept_counts))
print(specs)