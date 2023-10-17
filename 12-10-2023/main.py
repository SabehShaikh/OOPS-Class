list = [1,11, 'anas' , 'khan' , 11]
list[2:3] = [12]
print(list)

#delete by value
list.remove('khan')
print(list)

#delete by index/item
list.pop(0)
print(list)

#length
print(len(list))

#sort ---> arrange in ascending order
numbers = [1,2,3,6,4,8,7,5,9,15,25,10]
numbers.sort()
print(numbers)

#sort in reverse ---> descending order
nums = [98,75,80,104,202,260,300,50,60]
nums.sort(reverse=True)
print(nums)

naams = ['anas' , 'babar' , 'cat' , 'zoo' , 'xyz' , 'pakistan']
naams.sort(reverse=True)
print(naams)

