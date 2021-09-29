print("Welcome to the Tip Calculator.")

bill = input("What was the total bill? ")
people = input("How many people to split the bill? ")
tip = input("What percentage tip woul you like to give? 10, 12, or 15? ")

total_tip = (float(bill) * float(tip) / 100)
total_bill = (total_tip + float(bill))
each_person_should_pay = (total_bill / float(people))
each_person_should_pay_last = round(each_person_should_pay, 2)

print(f"Each person should pay {each_person_should_pay_last}" )