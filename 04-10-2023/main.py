#get percentage
marks = 275
total_marks = 300

percentage = (marks /total_marks) * 100
print(percentage)

#two variables together
first_name , last_name = 'ali' , 'raza'
print(first_name , last_name)

#updation of variable
a = 4
a = 5
print(a)

b = 'xyz'
b = 'abc'
print(b)

#list / array
details = ["sabeh" , "shaikh" , "bscs" , "2nd semester" , 19]
print(details)
#indexing & type
print(details[2])
print(type(details))

#add in list
details_one = ["sabeh" , "shaikh" , "bscs" , "2nd semester" , 19]
details_two = ["ali" , "raza" , "bscs" , "2nd semester" , 20]
details_three = [21 , 22 , 23]
print(details_one + details_two + details_three)

#append method --> add only at end
teams = ['pak' , 'eng' , 'aus']
teams.append('nz')
print(teams)