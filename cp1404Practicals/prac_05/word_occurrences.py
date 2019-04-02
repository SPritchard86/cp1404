
def main():
    """Get a string input and print out a formatted list of the occurrence number of words."""
    string = input("Enter your string: ")
    split_string = string.split(" ")
    split_string.sort()

    string_dictionary = create_dictionary(split_string)
    longest_word_length = find_longest_word(split_string)

    for word in string_dictionary:
        print("{:{}s} : {}".format(word, longest_word_length, string_dictionary[word]))


def create_dictionary(split_string):
    """Count occurrence of words and return dictionary."""
    string_dictionary = {}
    for word in split_string:
        if word in string_dictionary:
            string_dictionary[word] += 1
        else:
            string_dictionary[word] = 1
    return string_dictionary


def find_longest_word(split_string):
    """from a list, find the longest string and return its length."""
    longest_word_length = 0
    for word in split_string:
        if len(word) > longest_word_length:
            longest_word_length = len(word)
    return longest_word_length


main()
