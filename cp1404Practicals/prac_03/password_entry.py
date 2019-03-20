def main():

    MIN_PASSWORD_LENGTH = 6
    password = get_password(MIN_PASSWORD_LENGTH)
    print(convert_password_to_stars(password))


def get_password(min_password_length):
    """Get password, check for length."""
    password = input('Enter a password: ')
    while len(password) < min_password_length:
        print("Invalid password! Must be {} or more characters!".format(min_password_length))
        password = input("Enter a password:")
    return password


def convert_password_to_stars(password):
    return "*" * len(password)


main()
