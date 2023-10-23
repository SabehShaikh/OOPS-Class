#calculator by input

num_one = int(input('Enter first value: '))
num_two = int(input('Enter second value: '))
sum_result = num_one + num_two
sub = num_one - num_two
mul = num_one * num_two

# Check for division by zero
if num_two != 0:
    div = num_one / num_two
else:
    div = "Division by zero is not allowed"

operator = input('Enter operator + , - , * , /')

if operator == '+':
    print(sum_result)
elif operator == '-':
    print(sub)
elif operator == '*':
    print(mul)
elif operator == '/':
    print(div)
else:
    print('Invalid operator')

# Create a dictionary named thisdict with three key-value pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Print the value associated with the "brand" key using the get() method
print(thisdict.get("brand"))

# Print the entire dictionary
print(thisdict)

# Access and print the value associated with the "brand" key directly
print(thisdict["brand"])

# Print the type of the variable thisdict (which is a dictionary)
print(type(thisdict))

# Print the keys of the dictionary using the keys() method
print(thisdict.keys())

# Print the values of the dictionary using the values() method
print(thisdict.values())

# Create a dictionary named dict with three key-value pairs
dict = dict(name="John", age=36, country="Norway")

# Print the entire dictionary
print(dict)

# Create a dictionary named car with three key-value pairs
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Get a view of the keys in the car dictionary
x = car.keys()

# Print the keys view before making changes to the dictionary
print(x)  # before the change

# Add a new key-value pair ("color": "white") to the car dictionary
car["color"] = "white"

# Print the keys view after making changes to the dictionary
print(x)  # after the change
