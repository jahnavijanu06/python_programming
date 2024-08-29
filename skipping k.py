def print_numbers_with_skip(M, N, K):
    current = M
    while current <= N:
        print(current, end=", " if current + K + 1 <= N else "")
        current += K + 1


M = int(input("Enter the starting number M: "))
N = int(input("Enter the ending number N: "))
K = int(input("Enter the number of skips K: "))

print_numbers_with_skip(M, N, K)
