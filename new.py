def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")


def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")



# Write a find_integers function that returns a list of all the integers from my_tuple:
my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

# Iterate through each element in my_tuple
# Test to see if the element is an integer 
# If it is, colelct it in a collection 
# retrun the new collection 

def find_integers(my_tuple):
    new_list = []
    for element in my_tuple:
        if isinstance(element, int):
            new_list.append(element)
    return new_list

integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]



# Write a find_integers function that returns a list of all the integers from my_tuple:
my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

# Iterate through each element in my_tuple
# Test to see if the element is an integer 
# If it is, colelct it in a collection 
# retrun the new collection 

def find_integers(my_tuple):
    return [x for x in my_tuple if type(x) is int]
    # for element in my_tuple:
    #     if isinstance(element, int):
    #         new_list.append(element)
    # return new_list

integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]