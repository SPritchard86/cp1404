name = input("Enter name: ")
print("""(H)ello
(G)oodbye
(Q)uit""")
print()
menu_choice = input(">>> ")

while menu_choice != 'Q':
    if menu_choice == 'H':
        print("Hello " + name)
    elif menu_choice == 'G':
        print("Goodbye " + name)
    else:
        print("Invalid input")
    print("""(H)ello
(G)oodbye
(Q)uit""")
    print()
    menu_choice = input(">>> ")
print("Finished.")

