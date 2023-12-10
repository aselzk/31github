#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#How the math works in order to calculate this:
#12% = 12/100 = 0.12
#12% of 150 -> 150 * 0.12 = 18.0
#150+18=168
#168/5=33.6 for each person

#My version
total_bill = 150
tip_in_percentage = 12
amount_of_people = 5
each_person = (150.00 / 5) * 1.12
print(round(each_person, 2))
print(f"Each person should pay {each_person}")

#Angelas version
print("Welcome to the tip calculator!")
total_bill = float(input("What is the total bill?"))
tip_in_percentage = int(
    input("How much percentage would like to give? 10, 12, 15? "))
amount_of_people = int(input("How many people to split the bill?"))
bill_with_tip = tip_in_percentage / 100 * total_bill + total_bill
print(bill_with_tip)
bill_per_person = total_bill / amount_of_people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount} dollars")

