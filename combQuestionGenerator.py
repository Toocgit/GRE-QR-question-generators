import random

objects = random.randint(6, 20)
selections = random.randint(1, objects)
expectedResult = 1
selOrders = 1

# for each selection to make...
for sel in range(selections):

    # if it is the final selection
    if sel == (selections - 1):

        # update expected result
        expectedResult = (expectedResult * (objects - sel))

        # get final expected result
        expectedResult = (expectedResult / selOrders)

    # for all other selections
    else:

        # update expected result
        expectedResult = (expectedResult * (objects - sel))

        # update possible orders of selections
        selOrders = (selOrders * (selections - sel))

print("How many ways are there to select {} objects from the group of {} objects".format(selections, objects))
print("when the order of the selections doesn't matter?")

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