MIN_PASSWORD_LENGTH = 6
password = input("Enter a password: ")
while len(password) < MIN_PASSWORD_LENGTH:
    print("Invalid password! Must be {} or more characters!".format(MIN_PASSWORD_LENGTH))
    password = input("Enter a password:")
print("*" * len(password))