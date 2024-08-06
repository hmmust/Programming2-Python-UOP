# Dictionaries example - count specs in list of student specs
# Print all specs count of student in each department

student_specs = ['DSAI', 'CS', 'SE', 'IS','CS', \
                 'SE', 'IS','DSAI', 'CS', 'SE', \
                 'CS', 'SE', 'IS']
specs = dict() # {}
for s in student_specs:
    if s in specs:
        specs[s] += 1
    else:
        specs[s] = 1
print(specs)