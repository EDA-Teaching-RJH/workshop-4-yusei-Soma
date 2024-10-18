camel_case=input("Enter a camel case valuable: ")
print("snake case: ", end="")
for c in  camel_case:
    if c.islower():
        print(c, end="")
    if c.isupper():
        print("_",c.lower(), end="")
print()


  


