from cp1404Practicals.prac_06.guitar import Guitar


def main():

    i = 0
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print("{Guitar.name} ({Guitar.year}) : ${Guitar.cost:10,.2f} added".format(Guitar=guitars[i]))
        i += 1
        name = input("Name: ")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars):
        if guitars[i].is_vintage():
            vintage_string = "(Vintage)"
        else:
            vintage_string = ""

        print("Guitar {position}: {Guitar.name:>20} ({Guitar.year}), worth ${Guitar.cost:10,.2f} {vintage}".format(position = i + 1, Guitar = guitars[i], vintage=vintage_string))


main()