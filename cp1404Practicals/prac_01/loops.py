
STAR = "*"

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_stars = int(input("Enter the number of stars you would like: "))
for i in range(number_of_stars):
    print("*", end='')
print()

number_of_star_lines = int(input("Enter the number of star lines you would like: "))
for i in range(number_of_star_lines):

    print(STAR, end='')
    STAR += "*"
    print()

