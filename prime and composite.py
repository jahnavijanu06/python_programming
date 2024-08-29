def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_and_composites(numbers):
    prime_count = 0
    composite_count = 0
    
    for num in numbers:
        if num > 1:
            if is_prime(num):
                prime_count += 1
            else:
                composite_count += 1
    
    return prime_count, composite_count


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

prime_count, composite_count = count_primes_and_composites(numbers)
print(f"Prime numbers count: {prime_count}")
print(f"Composite numbers count: {composite_count}")
