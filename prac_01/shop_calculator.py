def main():
    total_price = 0
    number_items = int(input('Number of items:'))
    if number_items < 0:
        print(f'Invalid number of items!')
        return

    for item in range(number_items):
        price_items = float(input(f'Price of item{item+1} is:'))
        if price_items < 0:
            print(f'Sorry, try again.')
            return

        total_price += price_items

    if total_price > 100:
        total_price *= 0.9

    print(f"Total price for {number_items} items is ${total_price:.2f}")

main()

