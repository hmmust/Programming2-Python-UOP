# Sets - Syntax , unique, un-indexable
specs = { "CS","SE","IS", "DSAI","CS","IS",1,True,0, False }
print(specs)
print(type(specs))
specs.add("VR")
specs.remove(1)
specs.remove(0)
specs2 = set() # empty set - do not use {}
specs2.update(["BI","RB","CS"]) #specs.update({"BI","RB"})
print("unin",specs.union(specs2),specs | specs2)
print("intersection",specs.intersection(specs2),specs & specs2)
print("difference",specs.difference(specs2),specs - specs2)
