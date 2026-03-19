print("Welcome to tip calculator!")
total = float(input("what was the total bill?: "))
tip = int(input("How much tip you would like to give? 10, 12 or 15?: "))
people = int(input("How many people to split?: "))

bill_with_tip = tip / 100 * total + total 

print("Each person needs to pay" + int(input(bill_with_tip)))
