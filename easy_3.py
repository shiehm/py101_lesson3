print('-> Question 1')
numbers = [1, 2, 3, 4]
numbers.clear()

# while numbers:
#     numbers.pop()

print(numbers)


# print('-> Question 2')
# str1 = "hello there" 
# str2 = str1 # str2 has the same pointer as str2 to same memory location
# str2 = "goodbye!" # this REASSIGNS str2 to "goodbye!" in new memory location, not affecting str1 in any way
# print(str1)

# If I change str1 instead
# str1 = "hello there" 
# str2 = str1
# str1 = 'GOODBYE' # This REASSIGNS str1 to 'GOODBYE' in new memory location, BUT str2 still has the original pointer
# print(str2) # still pointing to "hello there" in the original memory location str1 was pointing to 
# print(str1)


# Note: review this one, the pointers and shallow vs. deep copy and collections
# Remember deep copy means completely separate
# Shallow copy which is always done when copy.deepcopy() isn't used the collections in a collection are still the same pointer
print('-> Question 4')
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list1[0]['first'] = 42
print(my_list2)


print('-> Question 5')
def is_color_valid1(color):
    return (color == "blue" or color == "green")
        
def is_color_valid2(color):
    return color in ['blue', 'green']

print(is_color_valid1('blue'))
print(is_color_valid1('green'))

print(is_color_valid2('blue'))
print(is_color_valid2('green'))