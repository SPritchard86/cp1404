"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    LOW_SALES_MODIFIER = 0.1
    HIGH_SALES_MODIFIER = 0.15

    sales = float(input("Enter your sales: $"))
    while sales < 0:
        print("invalid input. Please enter a positive value.")
        sales = float(input("Enter your sales: $"))

    bonus = sales_bonus(sales, LOW_SALES_MODIFIER, HIGH_SALES_MODIFIER)
    print("Your sales bonus is ${:.2f}".format(bonus))


def sales_bonus(sales, low_sales_modifier, high_sales_modifier):
    if sales >= 1000:
        bonus = sales * high_sales_modifier
    else:
        bonus = sales * low_sales_modifier
    return bonus

main()
