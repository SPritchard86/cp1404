from cp1404Practicals.prac_06.guitar import Guitar


def main():

    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2015, 440)

    print("{} get age: expected 97. got {}".format(gibson.name, gibson.get_age()))
    print("{} get age: expected 4. got {}".format(another_guitar.name, another_guitar.get_age()))
    print("{} is vintage: expected Yes. got {}".format(gibson.name, gibson.is_vintage()))
    print("{} is vintage: expected Yes. got {}".format(another_guitar.name, another_guitar.is_vintage()))


main()
