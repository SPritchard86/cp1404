

def main():

    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)


def get_result(score):

    if 0 <= score <= 100:
        if score >= 90:
            return "Excellent"
        elif score < 50:
            return "bad"
        else:
            return "pass"
    else:
        return "Invalid score"


main()
