def calculate_averages():
    positive_sum = 0
    positive_count = 0
    negative_sum = 0
    negative_count = 0
    
    while True:
        num = int(input("Enter the number: "))
        if num == -1:
            break
        elif num > 0:
            positive_sum += num
            positive_count += 1
        elif num < 0:
            negative_sum += num
            negative_count += 1

    
    if positive_count > 0:
        positive_avg = positive_sum / positive_count
    else:
        positive_avg = 0  # No positive numbers entered
    
    if negative_count > 0:
        negative_avg = negative_sum / negative_count
    else:
        negative_avg = 0  # No negative numbers entered
    
    print(f"The average of negative numbers is: {negative_avg}")
    print(f"The average of positive numbers is: {positive_avg}")


calculate_averages()
def remove_duplicates_entirely(arr):
    
    arr.sort()

    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    
    result = [num for num in arr if frequency[num] == 1]

    return result
