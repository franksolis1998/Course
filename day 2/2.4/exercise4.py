#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator")
bill = float(input("what was the total bill? $ "))
tip = int(input("What Percentage would you like to tip? 5, 10, 15, 20, 25? "))
people = int(input("How many people are splitting the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people 
final_amount = round(bill_per_person, 2)
print(f"Each person should pay ${final_amount}")