import re
line = "Arzona 479, 501, 870. california 209,213,650."
m = re.findall("\d",line,re.IGNORECASE)
for i in m:
    print(i)
#print(m)
line2 = "the ghost that says boo haunts the loo"
m2 = re.findall(".oo",line2, re.IGNORECASE)
print(m2)
