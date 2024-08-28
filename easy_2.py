print('-> Question 1')
numbers = [1, 2, 3, 4, 5]

print(numbers[-1::-1])
print(sorted(numbers, reverse=True))
print(list(reversed(numbers)))


print('-> Question 2')
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

print(number1 in numbers)
print(number2 in numbers)


print('-> Question 3')
def btwn_10_100(num):
    return num in range(10,101,1)
    
print(btwn_10_100(42))
print(btwn_10_100(100))
print(btwn_10_100(101))


print('-> Question 4')
list_num = [1, 2, 3, 4, 5]
list_num.pop(2)
# or 
# del numbers[2]
print(list_num)


print('-> Question 5')
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
print(numbers is list)
print(table is list)


print('-> Question 6')
title = "Flintstone Family Members"
print(title.center(40,'-'))


print('-> Question 7')
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

print(statement1.count('t'))
print(statement2.count('t'))


print('-> Question 8')
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
print(ages.get('Spot'))
print('Spot' in ages)


print('-> Question 9')
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}

ages.update(additional_ages)

# or add with 
# ages['Marilyn'] = 22
# ages['Spot'] = 237

print(ages)