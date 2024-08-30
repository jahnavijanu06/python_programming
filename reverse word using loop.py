 
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


input_string = "TEMPLE"
print("Original String:", input_string)
print("Reversed String:", reverse_string(input_string))


test_cases = ["SIGN UP", "AT-LEAST", "1245", "!@#$%", "145*999=144855"]

for test in test_cases:
    print(f"Original String: {test} -> Reversed String: {reverse_string(test)}")
