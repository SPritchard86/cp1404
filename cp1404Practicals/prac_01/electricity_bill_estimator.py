print("Electricity bill estimator.")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("""Please choose the number from the list of Tariffs below:
1. Tariff 11 ($0.244618 c per kWh)
2. Tariff 31 ($0.136928 c per kWh)""")

tariff_choice = int(input("1 or 2? "))
if tariff_choice == 1:
    cents_per_kWh = TARIFF_11
else:
    cents_per_kWh = TARIFF_31

daily_use_in_kWh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
bill_estimate = (cents_per_kWh / 100) * daily_use_in_kWh * number_of_billing_days
print("Estimated bill: $" + str(bill_estimate))
