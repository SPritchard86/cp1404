"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":

        if choice == "C":
            temperature = int(input("Enter temperature for conversion: "))
            converted_temperature_type = "Farenheit"
            converted_temperature = celsius_to_farenheit(temperature)
        elif choice == "F":
            temperature = int(input("Enter temperature for conversion: "))
            converted_temperature_type = "Celsius"
            converted_temperature = farenheit_to_celsius(temperature)
        else:
            print("Invalid option")
            return
        print("Result: {:.2f} {}".format(converted_temperature, converted_temperature_type))
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


def celsius_to_farenheit(temperature_input):
    return temperature_input * 9.0 / 5 + 32


def farenheit_to_celsius(temperature_input):
    return 5 / 9 * (temperature_input - 32)


main()
