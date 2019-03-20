"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

LOW_SALES_MODIFIER = 0.1
HIGH_SALES_MODIFIER = 0.15

sales = float(input("Enter your sales: $"))
while sales >= 0:
    if sales >= 1000:
        bonus = sales * HIGH_SALES_MODIFIER
    else:
        bonus = sales * LOW_SALES_MODIFIER
    print("Your sales bonus is $" + str(bonus))
    sales = float(input("Enter your sales: $"))
