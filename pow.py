
def calculate(x, n, choice):
    if choice == 1:  
        result = 1
        for _ in range(n):
            result *= x
        return result
    elif choice == 2:  
        return x + n
    elif choice == 3:  
        return x - n
    elif choice == 4:
        return x * n
    elif choice == 5:  
        return x / n if n != 0 else "Division by zero error!"
    else:
        return "Invalid Choice!"


x = int(input("Enter X: "))
n = int(input("Enter N: "))
print("Choose Operation: 1. Pow(X, N)  2. Add(X, N)  3. Sub(X, N)  4. Mul(X, N)  5. Div(X, N)")
choice = int(input("Enter your choice (1-5): "))


result = calculate(x, n, choice)
print("Result:", result)


test_cases = [(0, 4, 2), (5, 0, 1), (-3, 3, 4), (0, 0, 5), (123, 123, 3)]

for x, n, choice in test_cases:
    result = calculate(x, n, choice)
    print(f"X: {x}, N: {n}, Choice: {choice} -> Result: {result}")
