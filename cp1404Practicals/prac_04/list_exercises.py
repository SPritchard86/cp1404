def main():
    numbers = []
    for number in range(5):
        numbers.append(int(input("Enter a number: ")))

    print("The sum of the list is {}".format(sum(numbers)))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    username = input("Username: ")
    if username in usernames:
        print("Access Granted")
    else:
        print("Access denied")

main()
