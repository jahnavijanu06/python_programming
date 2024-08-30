
def is_valid_username(username):
    
    pattern = r'^[a-zA-Z0-9_@]{6,}$'
    if re.match(pattern, username):
        return True
    else:
        return False

username = input("Enter the username: ")


if is_valid_username(username):
    print("The username is valid.")
else:
    print("The username is invalid.")

test_usernames = ["Saveetha@789", "user_123", "abc", "username!", "Valid@123"]

for uname in test_usernames:
    validity = "valid" if is_valid_username(uname) else "invalid"
    print(f"Username: {uname} -> {validity}")
