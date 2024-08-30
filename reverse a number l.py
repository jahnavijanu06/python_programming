def reverse_number(num):
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + digit  
        num = num // 10  
    return reversed_num
number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print(f"Reverse Number: {reversed_number}")
