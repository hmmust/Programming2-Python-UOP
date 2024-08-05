# Dictionary syntax
names = { 569:"Aya",237:"Rania",256:"Raneem",5:"Fawzi"}
print(names[569])
names[174] = "khalid" # New key
names[569] = "Aya H." # Existing Key (change value)
del names[256]
print(names)

specs = {"DS":1,"CS":2,"SE":3,"IS":2}
specs["DS"] += 3
print("VR" not in specs)
print(specs)
for k in specs:
    print(k,specs[k])