# Set Example

student_specs1 = ['DSAI', 'CS', 'SE', 'IS','CS', \
                 'SE', 'IS','DSAI', 'CS', 'SE']
student_specs2 = ['CS', 'SE', 'IS','ART',"DNT",'ENG', \
                 'SE','CS','MGM']
"""student_specs1 = set(student_specs1)
student_specs2 = set(student_specs2)
student_specs= student_specs1 | student_specs2
#student_specs1.update(student_specs2)"""
student_specs_all = student_specs1 +student_specs2
student_specs = list(set( student_specs_all))
counts = [0] * len(student_specs)
specs = dict(zip(student_specs,counts))
student_count = 0
for s in student_specs_all:
    if s in specs and s != 'OTHER':
        specs[s] += 1
        student_count +=1
    else:
        specs['OTHER'] += 1
print(specs)
print('Number of students in FIT',student_count)