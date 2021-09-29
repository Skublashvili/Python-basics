age = input("What is your current age? ")

new_age = (90 - int(age))

new_age_days = (new_age * 365)
new_age_weeks = (new_age * 52)
new_age_months = (new_age * 12)

print(f"You have {new_age_days} days, {new_age_weeks} weeks, and {new_age_months} months left.")