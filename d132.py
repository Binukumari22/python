"""A local school wants to keep track of students' names in a file.
Ask the user how many student names they want to add.
Then, take that many names as input and store each name on a new line in a file called students.txt.
If the file already exists, first show all existing names, then add the new ones without removing the old ones.
After saving the new names, read and display the updated list of all student names."""

number = int(input("Enter how many student names you want to add: "))


print("\nExisting names:")
try:
    with open("students.txt", "r") as f:
        print(f.read())
   
except FileNotFoundError:
    print("No file found. A new one will be created.")

f = open("students.txt", "a")  
for i in range(number):
    name = input(f"Enter name {i+1}: ")
    f.write(name + "\n")
f.close()
print("\nUpdated list of names:")
f = open("students.txt", "r")
print(f.read())
f.close()