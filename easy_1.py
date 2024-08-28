# Question 2

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

def exclamation_end(string):
    if string[-1] == '!':
        print(True)
    else:
        print(False)

print(str1.endswith('!'))
print(str2.endswith('!'))
        
exclamation_end(str1)
exclamation_end(str2)


# Question 3
famous_words = "seven years ago..."

new_words1 = "Four score and " + famous_words
new_words2 = f'Four score and {famous_words}'

print(new_words1)
print(new_words2)


# Question 4, 5
munsters_description = "the Munsters are CREEPY and Spooky."
print(munsters_description.capitalize())
print(munsters_description.swapcase())


# Question 6
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
print('Dino' in str1)
print('Dino' in str2)
print(str1.find('Dino') > -1)
print(str2.find('Dino') > -1)


# Question 8
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(["Dino", "Hoppy"])
print(flintstones)


# Question 9
advice = "Few things in life are as important as house training your pet dinosaur."
house = advice.find('house')
print(advice[:house])
print(advice.split('house')[0])


# Question 10
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace('important', 'urgent'))