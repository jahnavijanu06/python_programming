def find_mth_max_nth_min(arr, M, N):
    sorted_arr = sorted(arr)
    if M > len(arr) or M <= 0 or N > len(arr) or N <= 0:
        return None, None, None, None
    nth_min = sorted_arr[N-1]
    mth_max = sorted_arr[-M]
    sum_result = nth_min + mth_max
    difference_result = mth_max - nth_min
    return mth_max, nth_min, sum_result, difference_result# Sample Input
array = [14, 16, 87, 36, 25, 89, 34]
M = 1
N = 3

mth_max, nth_min, sum_result, difference_result = find_mth_max_nth_min(array, M, N)
print(f"{M}st Maximum Number = {mth_max}")
print(f"{N}rd Minimum Number = {nth_min}")
print(f"Sum = {sum_result}")
print(f"Difference = {difference_result}")
test_cases = [
    ([16, 16, 16, 16, 16], 0, 1),  
    ([0, 0, 0, 0], 1, 2),          
    ([-12, -78, -35, -42, -85], 3, 3),  
    ([15, 19, 34, 56, 12], 6, 3),   
    ([85, 45, 65, 75, 95], 5, 7)   for i, (arr, M, N) in enumerate(test_cases):
    mth_max, nth_min, sum_result, difference_result = find_mth_max_nth_min(arr, M, N)
    print(f"Test Case {i+1}: M={M}, N={N}")
    if mth_max is not None and nth_min is not None:
        print(f"Mth Maximum: {mth_max}, Nth Minimum: {nth_min}, Sum: {sum_result}, Difference: {difference_result}\n")
    else:
        print("Invalid M or N\n")
