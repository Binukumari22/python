"""You are helping a small stationery shop owner manage a simple list of items.
First, ask the user to enter the name of a new item.
If the file items.txt does not exist, create it and write the item into it.
If the file exists, open it in append mode and add the new item.
After writing, display the full list of items from the file to the user"""


try:
    with open("items.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Creating a new file")
item = input("Enter your item: ")
with open("items.txt", "a") as f:
    f.write(item + "\n")
with open("items.txt", "r") as f:
    print(f.read())



