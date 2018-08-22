import random

print("This program will ask you a permutations related question.")

items = random.randint(6, 20)

print("There is a group of {} items.".format(items))

selections = random.randint(1, items)

print("How many ways are there to select, and order, {} items ".format(selections))
print("from the group of {} items?".format(items))

expectedResult = 1

# For each selection to make...
for s in range(selections):
    
    # Update expected result calculation
    expectedResult = (expectedResult * (items - s))

# Until the user gives the correct answer...
while True:
    
    try:
        # Get user's answer and convert it to integer data type
        userAnswer = int(input())
    except:
        # If user did not provide their answer as an integer...
        print("Please provide your answer as an integer.")
        continue
    
    # If user's answer is correct, exit while loop
    if userAnswer == expectedResult:
        break
    else:
        print("The answer {} is incorrect. Please try again.".format(userAnswer))

print("Perfect, you got it.")