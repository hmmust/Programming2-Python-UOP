# Dictionaries examples based on items,value, keys
specs = {"DSAI":4,"CS":2,"SE":3,"IS":2}
"""for k in specs:
    print(k,specs[k])"""
"""for v in specs.values():
    print(v)
for k in specs.keys():
    print(k)"""
for k,v in specs.items():
    print(k,v)

dept_counts= list(specs.values())
print(dept_counts)
depts= list(specs.keys())
print(depts)