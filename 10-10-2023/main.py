list = [12 , 'babar' , 'azam' , 'osama']

#slicing
print(list[0:3])
print(list[:3])
print(list[2:])

#change value
list[2] = 'rizwan'
print(list)

#more than one value
list[2:2] = ['azam']
print(list)

#insert function
list.insert(1, 13)
print(list)

#extend function
list2 = [7,2]
list.extend(list2)
print(list)
