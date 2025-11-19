"""Create the Empty List:
    The program starts with an empty list inventory = [] to hold the names of pet supplies as strings, making it simple for beginners.
Add Items with add_item Function:
    The add_item(item) function takes one item name (a string) and adds it to the inventory list using append().
    In the main() function, it adds "dog food", "cat toy", "bird cage", and "fish tank" by calling add_item four times.
Count Items with count_items Function:
  The count_items(items) function uses recursion to count the number of items in the list.
Base Case: If the list is empty (not items), return 0.
Recursive Step: Count 1 for the current item and add the result of calling count_items on the rest of the list (items[1:]).
          This is called in main() to get the total number of items.
Display Items with Lambda Function:
     A lambda function show_item = lambda item: print(f"Item in Stock: {item}") formats each item with the prefix "Item in Stock: ".
      A for loop in main() iterates over the inventory list to display each item using the lambda function.
Main Function and Running the Program:
    The main() function puts all steps together:
    Adds the four items using add_item.
    Displays the items using the lambda function in a loop.
    Counts and displays the total number of items using count_items.
    The program ends with a direct main() call, keeping it simple for students."""
    
inventory = []

def add_item(x):
    inventory.append(x)

def count_items(items):
    if len(items) == 0:  
        return 0  
    else:
        return 1 + count_items(items[1:])  

show_item = lambda item: print(f"Item in Stock: {item}")

def main():

    add_item("Dog food")
    add_item("cat toy")
    add_item("bird cage")
    add_item("fish tank")

    print(inventory)

    for item in inventory:
        show_item(item)

    total = count_items(inventory)
    print(f"\nTotal number of items: {total}")   


main()
