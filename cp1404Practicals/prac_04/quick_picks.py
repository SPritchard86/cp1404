import random


def main():
    """generate random unique numbers in sets of 6"""

    number_of_picks = int(input("Enter number of quick picks to generate: "))
    for line in range(number_of_picks):
        random_numbers = []

        for number in range(6):
            number = random.randint(0, 45)

            while number in random_numbers:
                number = random.randint(0, 45)
            random_numbers.append(number)
        random_numbers.sort()

        print(" ".join("{:2}".format(number) for number in random_numbers))


        #[random.randint(0, 45) for number in random_numbers if not in random_numbers]







main()