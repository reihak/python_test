import re


zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!
"""
m = re.findall("^is",zen,re.MULTILINE)
#print(m)

s = "Two too"
m =re.findall("t[wo]o",s,re.IGNORECASE)
print(m)

l = "123 hi 34 hello"
v = re.findall("\d",l, re.IGNORECASE)
print(v)

t  = "__one__ __two__ __three__"
found=re.findall("__.*?__",t)
for match in found:
    print(match)
