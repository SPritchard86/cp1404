

NAME_FILE = "name.txt"
NUMBERS_FILE = "numbers.txt"

out_file = open(NAME_FILE, 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

in_file = open(NAME_FILE, 'r')
print("Your name is {}".format(in_file.read()))
in_file.close()

in_file = open(NUMBERS_FILE, 'r')
sum_of_numbers = int(in_file.readline()) + int(in_file.readline())
print(sum_of_numbers)
in_file.close()

# Print sum of all numbers in file
sum_of_numbers = 0
in_file = open(NUMBERS_FILE, 'r')
for line_str in in_file:
    sum_of_numbers += int(line_str)
print(sum_of_numbers)
in_file.close()
