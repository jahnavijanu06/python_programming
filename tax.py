def calculate_tax(income):
    if income <= 150000:
        tax = 0
    elif income <= 300000:
        tax = (income - 150000) * 0.10
    elif income <= 500000:
        tax = (income - 300000) * 0.20 + 15000  # 15000 is 10% of 150000
    else:
        tax = (income - 500000) * 0.30 + 15000 + 40000  # 40000 is 20% of 200000, 15000 is 10% of 150000
    
    return tax


taxable_income = float(input("Enter your taxable income: "))
tax = calculate_tax(taxable_income)
print(f"The tax on an income of {taxable_income} is {tax:.2f}")
