#Tip claculator
print("Welcome to the tip calculator.")
#Ask the user for the total bill
bill = float(input("What was the total bill? $"))
#Ask the user for the percentage tip
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
#Ask the user for the number of people
people = int(input("How many people to split the bill? "))
#Calculate the tip
Total_bill = bill + (bill * tip / 100)
#Calculate the bill per person
Each_person = Total_bill / people
print(f"Each person should pay: ${round(Each_person, 2)}")