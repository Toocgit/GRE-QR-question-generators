import random

quantities = random.randint(2, 9)
percentChanges = []
expectedResult = 1

# for every quantity...
for quantity in range(quantities):
    
    # quantity 1 is the whole i.e. 1
    if quantity == 0:
        percentChanges.append(1)
    # each other quantity will be an integer-percent change of the previous quantity
    else:
        percentChanges.append(round(random.random(), 2))

# for every quantity...
for quan in range(quantities):
    
    # for the first quantity...
    if quan == 0:
        print("Quantity {} is the whole i.e. {} (100%).".format((quan + 1), percentChanges[quan]))
        continue
    # for all other quantities...
    else:
        
        # roll a die...
        dice = random.randint(1, 6)
        
        # If you rolled an even number, percent decrease...
        if (dice % 2) == 0:
            expectedResult = (expectedResult * percentChanges[quan])
            print("Quantity {} is {} % of quantity {}.".format((quan + 1), (percentChanges[quan] * 100), quan))
        # If you rolled an odd number, percent increase...
        else:
            expectedResult = (expectedResult * (1 + percentChanges[quan]))
            print("Quantity {} is {} % of quantity {}.".format((quan + 1), ((percentChanges[quan] + 1) * 100), quan))

# express expected result as a %
expectedResult = round((expectedResult * 100), 2)

print("What is the final quantity as a % of the first quantity?")
print("Your answer should NOT include a % symbol.")
print("Your answer should be rounded to two decimal places.")

# Until the user gives the correct answer...
while True:
    
    try:
        # Get user's answer and convert it to float data type
        userAnswer = float(input())
    except:
        # If user did not provide their answer as an integer / float
        print("Answer should be integer or float rounded to two decimal places.")
        continue
    
    # If user's answer is correct, exit while loop
    if userAnswer == expectedResult:
        break
    else:
        print("The answer {} is incorrect. Please try again.".format(userAnswer))

print("Perfect.")
# done