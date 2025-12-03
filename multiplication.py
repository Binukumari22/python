# Write a program to enter a number and print its multiplication tsble till 10 rows

num = int(input("enter a number"))
for i in range(1,11):
    print(f" Multiple of {i} * {num} is = ",i * num)