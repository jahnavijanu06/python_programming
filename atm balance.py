def calculate_atm_balance(denominations, notes):
    total_balance = 0
    for denom, count in zip(denominations, notes):
        total_balance += denom * count
    return total_balance
denominations = []
notes = []
for i in range(1, 5):
    denom = int(input(f"Enter the {i}st/nd/rd/th Denomination: "))
    count = int(input(f"Enter the {i}st/nd/rd/th Denomination number of notes: "))
    denominations.append(denom)
    notes.append(count)
total_balance = calculate_atm_balance(denominations, notes)
print(f"Total Available Balance in ATM: {total_balance}")
