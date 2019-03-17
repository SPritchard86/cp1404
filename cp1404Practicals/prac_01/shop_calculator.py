
total_price = 0
discount_modifier = 0.9

number_of_items = int(input("Enter the number of items: "))
if number_of_items <= 0:
    print("Goodbye.")
else:
    for i in range(number_of_items):
        price_of_item = float(input("Enter the item price: $"))
        while price_of_item < 0:
            print("Invalid number of items!")
            price_of_item = float(input("Enter the item price: $"))
        total_price = total_price + price_of_item
    if total_price >= 100:
        total_price = total_price * discount_modifier
    print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))

