def check_voting_eligibility(age):
    if age < 0:
        print("Invalid age entered.")
    elif age >= 18:
        print("You are eligible to vote.")
    else:
        years_left = 18 - age
        print(f"You are allowed to vote after {years_left} years.")
        age = input("Enter your age: ")
try:
    age = float(age)
    if age.is_integer():
        age = int(age)
    check_voting_eligibility(age)
except ValueError:
    print("Invalid input. Please enter a valid number.")
