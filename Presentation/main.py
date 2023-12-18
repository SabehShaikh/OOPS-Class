def greet(name, age):
  if age < 18:
    print("Hello, " + name + "! You are a minor.")
  elif age < 65:
    print("Hello, " + name + "! You are an adult.")
  else:
    print("Hello, " + name + "! You are a senior citizen.")

greet("Sabeh", 17)
greet("Ronaldo", 38)
greet("Charlie", 75)


#
# #
#
# # Functional Subroutine (Lambda Function)
# addition = lambda a,b,c: a + b + c
#
# # Using the functional subroutine
# result = addition(4, 6 , 5)
# print(result)
#
#

def add(x, y):
  return x + y
result = add(5, 3)
print(result)

def sub(a,b):
  return a - b
ans = sub(12,8)
print(ans)



