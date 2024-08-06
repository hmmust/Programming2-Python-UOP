# Dictionaries example - count specs in list of student specs
# Print all specs count of student in each department in the faculty
# other spec will be as others

student_specs = ['DSAI', 'CS', 'SE', 'IS','CS', \
                 'SE', 'IS','DSAI', 'CS', 'SE', \
                 'CS', 'SE', 'IS','ART',"DNT",'ENG', \
                 'SE','CS','MGM','OTHER']
specs = {'DSAI':0,'CS':0,'SE':0, 'IS':0,'OTHER':0}
student_count = 0
for s in student_specs:
    if s in specs and s != 'OTHER':
        specs[s] += 1
        student_count +=1
    else:
        specs['OTHER'] += 1
print(specs)
print('Number of students in FIT',student_count)