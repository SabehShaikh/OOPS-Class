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