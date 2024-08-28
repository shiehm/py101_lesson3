print('-> Question 1')

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return { # if it starts on the same line as return it'll work, otherwise None
        'prop1': "hi there",
    }

print(first())
print(second())


print('-> Question 2')
dictionary = {'first': [1]}
num_list = dictionary['first'] # [1]
num_list.append(2) # [1, 2]

print(num_list)
print(dictionary) # {'first': [1, 2]} because it is mutating a collection in a shallow copy, same object in memory location

# These return new lists (different objects in memory)
dictionary = {"first": [1]}
num_list = dictionary["first"].copy() # Copies the list only, which has 1 immutable element, not a collection within a collection 
num_list.append(2)

dictionary = {"first": [1]}
num_list = dictionary["first"][:] # Slicing returns a new list 
num_list.append(2)


print('-> Question 4')
def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False
    
def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    
    if len(dot_separated_words) != 4:
        return False
        
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True
    
print(is_dot_separated_ip_address('10.4.5.11'))
print(is_dot_separated_ip_address('10.4.5.11.1'))
print(is_dot_separated_ip_address('10.4.5'))
print(is_dot_separated_ip_address('10.4.5.1111'))