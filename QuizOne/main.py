#create a program that asks the user to input a number and then prints the square of that number.

number = int(input('enter your number'))
square = number * number

print(square)

#create a program to ask the user to enter two numbers, multiply them together and print

num_one = int(input('enter number one'))
num_two = int(input('enter number two'))

mult = num_one * num_two
print(mult)

#ask the user to enter the fave food and colour and print the response using both answers:

fave_food = input('enter your fave food')
fave_colour = input('enter your fave colour')

print('Fave food is' , fave_food )
print('fave colour is' , fave_colour)

#create a very simple spanish translation program, let the user enter a number between one to four then print the spanish word for that number

num = int(input('Enter a number between 1 and 4: '))

if num == 1:
    print('uno')
elif num == 2:
    print('dos')
elif num == 3:
    print('tres')
elif num == 4:
    print('cuatro')
else:
    print("I only know numbers between 1 and 4.")

#choose a category like planets, people in your class or months in the year secretly chose three of them, ask the user to a word in your category, if they enter one of three you chosed, they lose

months = ['january', 'february', 'march']

user_months = input('Enter a month: ')

if user_months in months:
    print('You are correct.')
else:
    print('You lose.')
