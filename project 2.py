print("Welcome to Tip Calculator $ ")

total_bill=float(input("How much was the total bill $? \n"))
tip =int(input("How much tip would you like to give $? 10,12 or 15 \n"))
no_of_persons=int(input("How many people are going to split the bill?"))

final_tip =  tip/100 * total_bill + total_bill
print(final_tip)
