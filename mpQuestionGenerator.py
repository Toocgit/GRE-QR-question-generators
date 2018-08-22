import random

print("This program generates multiplication principle questions for you to practice.")

decisions = random.randint(1, 10)

print("Let's say you have {} decisions to make.".format(decisions))

decisionOptions = []

# For each decision to be made...
for d in range(decisions):
    
    # Add the number of options for each decision to the list 'decisionOptions'
    decisionOptions.append(random.randint(1, 30))
    
    print("There are {} options to choose from for decision {}.".format(decisionOptions[d], (d + 1)))

expectedResult = 1

# For each set of options per decision...
for options in range(decisions):
    
    # Extend expected result calculation
    expectedResult = (expectedResult * decisionOptions[options])

print("How many different groups of decisions are possible?")

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