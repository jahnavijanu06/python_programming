import math

def is_palindrome_string(s):
    return s == s[::-1]

def is_palindrome_number(n):
    s = str(n)
    return s == s[::-1]

def compute_lcm_gcd(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a * b) // gcd
    return lcm, gcd

def main():
    print("Choose an option:")
    print("1. Check if a string or number is a palindrome")
    print("2. Find LCM and GCD of two numbers")
    
    choice = int(input("Enter choice (1 or 2): "))
    
    if choice == 1:
        case = int(input("Case (1 for string, 2 for number): "))
        
        if case == 1:
            s = input("Enter the string: ")
            if is_palindrome_string(s):
                print("Palindrome")
            else:
                print("Not Palindrome")
                
        elif case == 2:
            n = int(input("Enter the number: "))
            if is_palindrome_number(n):
                print("Palindrome")
            else:
                print("Not Palindrome")
                
        else:
            print("Invalid case")
            
    elif choice == 2:
        n1 = int(input("Number 1: "))
        n2 = int(input("Number 2: "))
        lcm, gcd = compute_lcm_gcd(n1, n2)
        print(f"LCM = {lcm}")
        print(f"GCD = {gcd}")
        
    else:
        print("Invalid choice")

if _name_ == "_main_":
    main()
