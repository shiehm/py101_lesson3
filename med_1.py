# print('-> Question 1')
# string = '-The Flintstones Rock!'

# for i in range(11):
#     print(string)
#     string = '-' + string
    
# for prefix in range(1, 11):
#     print(f'{"-" * prefix}The Flintstones Rock!')
    
    
print('-> Question 2')
# Refactor to handle negative numbers

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result
    
print(factors(27))
print(factors(-1))


print('-> Question 4')
import math

print(0.3 + 0.6)
print(math.isclose(0.3 + 0.6, 0.9))


print('-> Question 5')
nan_value = float("nan")
print(math.isnan(nan_value))


print('-> Question 8')
def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"

# Should return paper
print(
    rps(
        rps(
            rps("rock", "paper"), # returns paper
            rps("rock", "scissors") # returns rock
        ), # returns paper
    "rock") # returns paper
    )