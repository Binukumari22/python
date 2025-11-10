import random
rice = 45
sugar = 40
oil = 130
rice_kg = 3
sugar_kg = 2.5
oil_kg = 1.8
Total_price = (rice * rice_kg) + (sugar * sugar_kg) + (oil * oil_kg)
print(Total_price)
x = int(Total_price)
print(x , type(x))
y = str(Total_price)
print(y,type(y))
newsugar_kg = int(sugar_kg)
newoil_kg = int(oil_kg)
z = random.randrange(5,10)
final_bill = (rice * rice_kg) + (sugar * newsugar_kg) + (oil * newoil_kg) + z
print(final_bill)