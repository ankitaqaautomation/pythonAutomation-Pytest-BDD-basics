# This file demonstrates creating a dictionary and Methods to interact with dictionaries in Python.

info = {
"name": "Dict_basics", 
"age": 35,
"city": "New York",
"occupation": "Engineer",
"is_employed": True,  # here is_employed is a boolean value
"skills": ["Python", "Data Analysis", "Machine Learning", "Test Automation"]  # here skills is a list of Strings

}

print(type(info))  # Output: <class 'dict'>

# Accessing values in the dictionary
print("Name:", info["name"])
print("Age:", info["age"])
print("City:", info["city"])
print("Skills:", info["skills"])

# Create an empty dictionary and adding key-value pairs in empty dict.
empty_dict = {}
empty_dict["new_key"] = "new_value"
empty_dict["firstName"] = "Sara"
empty_dict["lastName"] = "Deshmukh"
empty_dict["SaraAge"] = 9
print("Empty Dictionary after adding a key-value pair:", empty_dict)

# we can also use the get() method to access values in a dictionary.
print("Occupation:", info.get("occupation"))
print("Is Employed:", info.get("is_employed"))
print("First Skill:", info["skills"][0])  # Accessing the first skill from the skills list


# Modifying values in the dictionary
info["age"] = 46  # Updating age
info["city"] = "San Francisco"  # Updating city
print("Updated Age:", info["age"])
print("Updated City:", info["city"])
print("updated Dictionary:", info)

# Nested dictionaries
employee = {
    "emp_name": "John Doe",
    "emp_age": 28,
    "empdepartment": "IT",
    "emp_address": {
        "street": "123 Main St",
        "city": "Boston",
        "state": "MA"
    }
}


print("Employee Name:", employee["emp_name"])
print("Employee City:", employee["emp_address"]["city"])


print(employee["emp_address"])  # Output: {'street': '123 Main St', 'city': 'Boston', 'state': 'MA'}
print(employee["emp_address"]["street"])  # Output: 123 Main St


print(employee["emp_age"])  # Output: employee age value using direct key access.
print(employee.get("emp_age"))  # Output: employee age value using get() method.

# print(employee["emp_age2"])  #   Output would be an error since emp_age2 key does not exist in the dictionary.
# the above line would raise a KeyError.and the program would terminate abruptly. without executing the next lines of code.

print(employee.get("emp_age2"))  # Output would be None since emp_age2 key does not exist in the dictionary.

print(list(employee.keys()))  # Output: list of keys in the employee dictionary. we can use the keys() method to get a list of keys in the dictionary.
# we have done typecasting to list to display the keys as a list.

print(list(employee.values()))  # Output: list of values in the employee dictio nary. 
#we can use the values() method to get a list of values in the dictionary.

print(employee.items())  # Output: list of key-value pairs in the employee dictionary.
# we can also use the items() method to get a list of key-value pairs in the dictionary.
# we get the output as a list of tuples, where each tuple contains a key-value pair.

# Modifying values in the nested dictionary

print("Employee Name:", employee["emp_name"])
print("Employee City:", employee["emp_address"]["city"])


# # Removing Values from Dictionary

del employee["emp_address"]  # Removing a specific key-value pair using del method.
print("Dictionary after deleting emp_address:", employee)

# removing the last key-value pair added to the dictionary using popitem() method. from info dictionary
removed_item = info.popitem()  # Removes key and returns value
print("Removed Item:", removed_item)
print("Dictionary after popitem():", info)


# we can create a dictionary using the dict() constructor.
person = dict(name="Alice", age=30, city="Los Angeles")
print("Person Dictionary:", person)

# we can use the len() function to get the number of key-value pairs in the dictionary.
print("Number of key-value pairs in info dictionary:", len(info))

# Methods to interact with dictionaries

# we can also use the items() method to get a list of key-value pairs in the dictionary.
print("Key-Value Pairs:", info.items())
# we can use the keys() method to get a list of keys in the dictionary.
print("Keys:", info.keys())
# we can use the values() method to get a list of values in the dictionary.
print("Values:", info.values())

# we can remove a key-value pair from the dictionary using the del statement.
del info["occupation"]
print("Dictionary after deleting occupation:", info)


# deleting all key-value pairs/items from the dictionary using clear() method.
# info.clear()
# print("Dictionary after clear():", info)


# copying a dictionary
Dictionary_copy = info.copy()
print("Copied Dictionary:", Dictionary_copy)

# we can use the update() method to add key-value pairs from one dictionary to another.
other_details = {"hobby": "Photography", "married": False}
info.update(other_details)
print("Updated Dictionary with additional info:", info)


# we can use the pop() method to remove a specific key-value pair from the dictionary.
removed_value = info.pop("city")  # Removes key and returns value
print("Removed Value for 'city':", removed_value)
print("Dictionary after pop():", info)

# Looping through a dictionary
for key in info:
    print(f"{key}: {info[key]}")
for key, value in info.items():
    print(f"{key}: {value}")

    
# Output:
# Name: Dict_basics
# Age: 35
# City: New York
# Skills: ['Python', 'Data Analysis', 'Machine Learning', 'Test Automation']
# Empty Dictionary after adding a key-value pair: {'new_key': 'new_value'}

# Setting a default value if the key does not exist using setdefault() method.
default_value = info.setdefault("country", "USA")
print("Country (default value):", default_value)


#Note: 
# Dictionary can store various data types including strings, integers, boolean values and lists.
# a dictionary is a built-in data type used to store data in key–value pairs.
# a key can be any immutable data type such as strings, numbers or tuples.
# keys must be unique within a dictionary.
# tuples can be used as keys in a dictionary because tuples are immutable, 
# meaning their contents(keys) cannot be changed after they are created.
# Dictionaries are mutable, meaning that their contents (key-value pairs) can be changed after they are created.  
# It’s unordered, mutable, and does not allow duplicate keys.