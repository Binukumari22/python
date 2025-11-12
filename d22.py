x = '''  Python is a high level interpreted programming language
Python is opensource 
It is easy to learn  '''
b = len(x)
print(b)
print("The first letter is ",x[2])
print("The last letter is ",x[-3])
print(x[0:50])
newx = x.replace("Python","PYTHON")
print(newx)
print(x.lower())
c = x.strip()
print(c)
print(c.split(" "))
a = len(c.split(" "))
print(a)
print("course" in x)
y = f"The course description is {b} characters long and has {a} words."
print(y)
