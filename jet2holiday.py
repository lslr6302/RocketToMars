#Created by Carol, Sam, Sophia, Vaishali
#unfinished, still some logic bugs

def purchaseTech():
    print("""Category: Tech Materials
    1. oxygen filtration system  --  $10,000
    2. water filtration system  --  $20,000
    3. Martian Tech: shelters/4 people  --  $50,000
    4. Martian Tech: irrigation system (adds 1 meal per day)  --  $100,000
    """)

    numOfTechPurchase = []
    numOfItems = 4
    for i in range(numOfItems):
        numOfTechPurchase.append(int(input(f"Amount want to purchase for item {i+1} >>> ")))

    # print(numOfTechPurchase)
    return numOfTechPurchase

def purchaseFood():
    print("""Category: Food Resources
    1. Seeds/meal  --  $5
    2. Soil Bags  --  $500
    3. Water Containers  --  $1,000
    """)

    numOfFoodPurchase = []
    numOfItems = 3
    for i in range(numOfItems):
        numOfFoodPurchase.append(int(input(f"Amount want to purchase for item {i+1} >>> ")))

    # print(numOfFoodPurchase)
    return numOfFoodPurchase


def purchasePeople():
    print("""Category: Professionals
    1. Herbologists  --  $160,000
    2. Mechanics  --  $100,000
    Note: You are only allowed 6 people on the space ship
    """)

    while True:
        numOfPassengers = []
        numOfPassengerTypes = 2
        totalNumPassengers = 0
        for i in range(numOfPassengerTypes):
            numOfPassengers.append(int(input(f"Amount person type {i + 1} >>> ")))
            totalNumPassengers += int(numOfPassengers[i])
        if (totalNumPassengers > 6):
            print("You have selected too many passengers! Please pick 6 or less people.")
        else:
            break

    # print(numOfPassengers)
    return numOfPassengers

def budgetting():
    amountSpend = 0

    for i in range(len(numOfTotalPurchase)):
        for j in range(len(numOfTotalPurchase[i])):
            amountSpend += numOfTotalPurchase[i][j]*prices[i][j]

    amountLeft = budget - amountSpend

    return amountLeft


#main
budget = 750000
numOfTotalPurchase = []
prices = [
    [10000, 20000, 50000, 100000],  # tech
    [5, 500, 1000],  # food
    [160000, 100000]  # people
]

print("Hello traveler, welcome to Jet2 Airlanes. You thought you were going on a relaxing vacation to Hawaii but SUPRISE! \nYou’ve actually been selected as captain of an elite mission to Mars. We’ve provided you with a budget of $750,000 \nand it is now up to you to decide how you would like to spend this money to ensure your survival on your Jet2 Holiday to Mars. \nThe categories of what you can purchase will be listed next...Good luck 😊\n\n")

print("""List of all Things to Purchase:
Category: Tech Materials
    1. oxygen filtration system  --  $10,000
    2. water filtration system  --  $20,000
    3. Martian Tech: shelters/4 people  --  $50,000
    4. Martian Tech: irrigation system (adds 1 meal per day)  --  $100,000
Category: Food Resources
    1. Seeds/meal  --  $5
    2. Soil Bags  --  $500
    3. Water Containers  --  $1,000
Category: Professionals
    1. Herbologists  --  $160,000
    2. Mechanics  --  $100,000
    Note: You are only allowed 6 people on the space ship
""")

print("Now entering the purchasing phase!")
if (input("Want to purchase tech materials? (Y/N) >>> ") == "Y"):
    numOfTotalPurchase.append(purchaseTech())
for i in range(len(numOfTotalPurchase[0])):
    budget -= numOfTotalPurchase[0][i]*prices[0][i]
print(f"Here is your current budget: {budget}")

if (input("Want to purchase food resources? (Y/N) >>> ") == "Y"):
    numOfTotalPurchase.append(purchaseFood())
for i in range(len(numOfTotalPurchase[1])):
    budget -= numOfTotalPurchase[1][i]*prices[1][i]
print(f"Here is your current budget: {budget}")

if (input("Want to hire professionals? (Y/N) >>> ") == "Y"):
    numOfTotalPurchase.append(purchasePeople())
for i in range(len(numOfTotalPurchase[2])):
    budget -= numOfTotalPurchase[2][i]*prices[2][i]
print(f"Here is your current budget: {budget}")

total_food = numOfTotalPurchase[1][0]
food_consumed = (numOfTotalPurchase[2][0]+numOfTotalPurchase[2][1])*3
days = 0
food_made = numOfTotalPurchase[2][0]*4
tech_decay = 100
decay = 99.5
repairs = numOfTotalPurchase[2][1]*0.25
while (total_food > 0 and tech_decay > 0) :
    # food_consumed is the number of people multiplied by 4 on mars
    total_food -= food_consumed
    # food made is the number of herbologists multiplied by 5 on mars
    total_food += food_made
    # decay is .9 on mars and repairs is (mechanics * 0.025)
    tech_decay = (tech_decay * (decay + repairs))

    if tech_decay == 1 :
        tech_decay = 0

    # makes sure cant go over 100%
    if tech_decay > 100 :
        tech_decay = 100

    print(f"After Day, {days} on Mars you have, {total_food} food left and your tech has decayed {100 - tech_decay}%")
    days += 10

print(f"Drats, you died. But you survived a whole {days} days! thats {days - 365} days on Mars!")
if tech_decay <= 0 :
    print("You Died because all your tech decayed in to nothing and the elements killed you. happens to the best of us")
else :
    print("you Died because you didnt have enough food and your whole crew starved. Nobodys perfect.")
