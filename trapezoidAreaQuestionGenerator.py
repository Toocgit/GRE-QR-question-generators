import random

baseOne = random.randint(50, 500)
baseTwo = random.randint(5, (baseOne - 10))
height = random.randint(12, 96)

# calculate trapezoid area
expectedResult = (((baseOne + baseTwo) * height) / 2)

print("What is the area of a trapezoid with a height of {}, ".format(height))
print("a base of length {} and another base of length {}?".format(baseOne, baseTwo))

# Until the user gives the correct answer...
while True:
    
    try:
        # Get user's answer and convert it to float data type
        userAnswer = float(input())
    except:
        # If user did not provide their answer as an integer / float
        print("Answer should be integer or float.")
        continue
    
    # If user's answer is correct, exit while loop
    if userAnswer == expectedResult:
        break
    else:
        print("The answer {} is incorrect. Please try again.".format(userAnswer))

print("Perfect.")
# done