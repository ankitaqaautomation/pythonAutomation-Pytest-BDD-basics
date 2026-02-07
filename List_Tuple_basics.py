# this module demonstrates basic functions and operations in Python including string, list, and tuple manipulations.
# It includes functions to read user input, perform string operations, list manipulations, and tuple operations.


def get_and_display_input():
    """Read a string from the user and display it."""
    user_input = input("Enter a string: ")
    print("You entered:", user_input)


def basic_string_operations():
    
    # Strings in Python are sequences of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """).
    # They are immutable, meaning once created, their content cannot be changed.
  
    # Basic string functions in Python
    str1 = "i am learning Python"
    print(str1.endswith("as"))  # output is in true or false
    print("The string before capitalise is :" , str1)
    str2 = str1.capitalize()
    print("The string after capitalise is :" , str2)

    # capitalize 1st word of string. 
    # It creates a new string and original string remains unchanged
    print(str1.replace("Python" , "AI"))

    # replace method replaces a substring with another substring
    print(str1.lower())  # converts string to lowercase
    print(str1.upper())  # converts string to uppercase
    print(str1.count("a"))  # counts occurrences of a substring

    #find() method returns the lowest index of the substring if found in given string. If not found, it returns -1
    print(str1.find("learning"))  # finds the index/ position of a substring
    print(str1.find("Automation"))  # returns -1 if substring not found
    print(str1.find("a" , 1))  # finds the position of "a" starting from index 1

    #index() method returns the lowest index of the substring if found in given string. If not found, it raises a ValueError
    print(str1.index("learning"))  # finds the index/ position of a substring
    print(str1.index("Automation"))  # returns ValueError if substring not found
    print(str1.index("a" , 1))  # finds the position of "a" starting from index 1

    # split() method splits a string into a list of substrings based on a delimiter
    print(str1.split(" "))  # splits the string into a list of substrings


def list_operations():
    
    # list in python is a collection which is ordered and changeable. Allows duplicate members.
    # A list is created using square brackets []. I can have different data types in a list
    # list in python is mutable i.e. we can change the elements of list
    # Example - [14, "Hello", 3.14, True, "Karan", "Delhi", 85]
    # List operations
    my_list = [10, 20, 30, 40, 50, 30, 75, 20]
    print("Original List:", my_list)
    print("Element at index 2:", my_list[2])  # accessing 3rd element by index
    print("Length of list:", len(my_list))  # length of the list
    print(type(my_list))  # type of the list  is always a class <list>
    print("Slicing list from index 1 to 3:", my_list[1:4])  # slicing the list from index 1 to 3

    my_list.extend([60,80,100])  #Takes one iterable (like a list, tuple, set, string, etc.) and adds multiple elements
    # to the end of the list. and Modifies the original list in place, Returns None
    print("After extend:", my_list)

    my_list.append(60)  # adds an element at the end
    print("After append:", my_list)

    my_list.insert(2, 25)  # inserting 25 element at index 2
    print("After insert:", my_list)

    my_list.remove(30)  # removes the first occurrence of the element 30
    print("After remove:", my_list)

    popped_element = my_list.pop(2)  # removes and returns the element at index 2
    print("Popped element:", popped_element)
    print("After pop:", my_list)

    my_list.reverse()  # reverses the list
    print("After reverse:", my_list)

    my_list.sort()  # sorts the list in ascending order
    print("After sort:", my_list)
    print("Sorted list without modifying original:", sorted(my_list))  # returns a new sorted list without modifying the original list

    sorted_list = sorted(my_list, reverse=True)  # returns a new sorted list in descending order without modifying the original list
    print("Sorted list in descending order without modifying original:", sorted_list)

    print("Count of element 20:", my_list.count(20))  # counts occurrences of element 20
    print("Sum of elements in the list:", sum(my_list))  # calculates sum of elements
    print("Maximum element in the list:", max(my_list))  # finds maximum element
    print("Minimum element in the list:", min(my_list))  # finds minimum element


    print("Index of element 40:", my_list.index(40))  # finds index of element 40
    print("Count of element 20:", my_list.count(20))  # counts occurrences of element 20
    print("Length of list after operations:", len(my_list))  # length of the list after operations


    # if we try to access an index which is not present in the list, it will raise an IndexError
    print("Accessing out of range index will raise an error:")
    try:
        print(my_list[10])  # accessing out of range index
    except IndexError as e:
        print("Error:", e)
        print("IndexError: list index out of range")
        print("Our list contains only", len(my_list), "elements.")



def tuple_operations():
    """Demonstrate tuple operations."""
    # tuple in python is a collection which is ordered and unchangeable. Allows duplicate members
    # Tuples are immutable i.e. we cannot add, remove or change the elements of tuple
    # So the functions like append(), remove(), sort() extend() insert()which modify the list are not available for tuple
    # A tuple is created using parentheses (). I can have different data types in a tuple
    # Example - (14, "Welcome", 3, True, "Priya", "Pune", 85.56)

     # Tuple operations
    my_tuple = (100, 200, 300, 400, 500, 300, 700, 200, 800, 900)
    print("Original Tuple:", my_tuple)
    print("Index of element 300:", my_tuple.index(300))

    print("Element at index 2:", my_tuple[2])  # accessing element by index

    # Tuples are immutable, so we cannot add or remove elements
    # However, we can concatenate tuples
    new_tuple = my_tuple + (600, 700)
    print("After concatenation:", new_tuple)

    print("Length of tuple:", len(my_tuple))  # length of the tuple
    print(type(my_tuple))  # type of the tuple is always a class <tuple>
    print("Slicing tuple from index 1 to 3:", my_tuple[1:4])  # slicing the tuple from index 1 to 3
    print("Count of element 500:", my_tuple.count(500))  # counts occurrences of element 500
    print("Index of element 400:", my_tuple.index(400))  # finds index of element 400
    print(max(my_tuple))  # finds maximum element
    print(min(my_tuple))  # finds minimum element
    print(sum(my_tuple))  # calculates sum of elements
    print(sorted(my_tuple))  # returns a new sorted list from the tuple elements
    print(sorted(my_tuple, reverse=True))  # returns a new sorted list in descending order from the tuple elements
    print(list(enumerate(my_tuple)))  # returns a list of tuples containing index and element
    print(tuple(reversed(my_tuple)))  # returns a new tuple with elements in reverse order
    print("Length of tuple after operations:", len(my_tuple))  # length of the tuple after operations
    print("Original Tuple remains unchanged:", my_tuple)
    print(list(my_tuple))  # convert tuple to list

    # Trying to modify a tuple will raise a TypeError
    print("Trying to modify a tuple will raise an error:")
    try:
        my_tuple[1] = 250  # trying to modify an element
    except TypeError as e:
        print("Error:", e)
        print("TypeError: 'tuple' object does not support item assignment")

    # Tuples are immutable, so to modify them we convert the tuple into a list using list(),
    # make changes, and convert it back into a tuple using tuple()
    temp_list = list(my_tuple)  # convert tuple to list
    temp_list.append(600)  # modify the list

    # convert back to tuple
    my_tuple = tuple(temp_list)  # convert list back to tuple
    print("After modification:", my_tuple)

    print("tuple 1: ", my_tuple)  # Tuple 1
    tuple2 = (700, 800, 900, 1000, 4343, 7474)  # Tuple 2
    print("tuple 2: ", tuple2)
    # Concatenating tuples
    tuple3 = my_tuple + tuple2
    print("Concatenated tuple: ", tuple3)

    print("Iterating through the tuple:")
    for item in tuple3:
        print(item)
        



if __name__ == "__main__":
   # get_and_display_input()
   # basic_string_operations()
   # list_operations()
    tuple_operations()
