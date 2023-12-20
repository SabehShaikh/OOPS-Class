total = 0 # Initialize a variable to store the total sum of numbers entered by the user



# While Loop
while True:
    choice = input('You have 3 choices: 1 to enter a number, 2 to show the total, 3 to exit: ')

    if choice == '1':
        num = int(input('Enter the number: '))
        total = total + num
        continue

    elif choice == '2':
        print("The total value is:", total)
        continue

    elif choice == '3':
        print("Program finished.")
        break

# Note: The 'continue' statement is not necessary after the 'break' statement.
