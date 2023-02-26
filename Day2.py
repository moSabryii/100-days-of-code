print("Hello and welcome to the tip calculator")
totalBill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
peopleNum = int(input("How many people to split the bill? "))

toPay = (totalBill + (totalBill*(tip/100))) / peopleNum
print("Each person should pay: " + str(round(toPay, 2)) + '$')
