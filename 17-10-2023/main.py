# Create a tuple containing four strings---> cannot be modified.
my_tuple = ("sabeh", "sabeh", "shaikh", "shaikh")

# Create a set containing four strings--> duplicates are not allowed.
my_set = {"sabeh", "pakistan", "babar", "rizwan"}

# Create a list containing three strings--> can be modified.
my_list = ["ali", "raza", "pak"]

# Print the type of the 'my_tuple' variable, which will be <class 'tuple'>
print(type(my_tuple))

# Print the type of the 'my_set' variable, which will be <class 'set'>
print(type(my_set))

# Print the type of the 'my_list' variable, which will be <class 'list'>
print(type(my_list))

# Print the contents of the 'my_tuple' variable, which will include all four elements
print(my_tuple)

# Print the contents of the 'my_set' variable, which may not preserve the order of elements
print(my_set)

# Print the contents of the 'my_list' variable, which will include all three elements
print(my_list)

# Conditional statements
# Define the scores for three subjects: English, Math, and PST.
english = 45
maths = 80
pst = 50

# Check if the score in English is greater than or equal to 40.
if english >= 40:
    print('You have passed in English')  # Print a message indicating the person passed in English.
else:
    print('You have failed in English')  # Print a message indicating the person failed in English.

# Check if the score in Math is greater than or equal to 40.
if maths >= 40:
    print('You have passed in Math')  # Print a message indicating the person passed in Math.
else:
    print('You have failed in Math')  # Print a message indicating the person failed in Math.

# Check if the score in PST is greater than or equal to 40.
if pst >= 40:
    print('You have passed in PST')  # Print a message indicating the person passed in PST.
else:
    print('You have failed in PST')  # Print a message indicating the person failed in PST.
