import re

value = []
items = [x for x in input('Password: ').split(',')]

for p in items:
    if len(p) < 1 or len(p) > 100:
        continue
    if not re.search("[a-z]", p):
        print("1")
        continue
    elif not re.search("[0-9]", p):
        print("2")
        continue
    elif not re.search("[A-Z]", p):
        print("3")
        continue
    elif not re.search("[$#@]", p):
        print("4")
        continue
    print(p)
    value.append(p)
print ("".join(value))