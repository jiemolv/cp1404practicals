# Program to calculate and display a user's bonus based on sales.
# If sales are under $1,000, the user gets a 10% bonus.
# If sales are $1,000 or over, the bonus is 15%.

# while True:
#     sales = float(input("Enter sales: $"))
#     if sales < 0:
#         break
#     if sales < 1000:
#         print(f'You get a {sales*0.1}')
#     else:
#         print(f'The bonus is {sales*0.15}')

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        sales = sales * 0.1
    else:
        sales = sales * 0.15
    print(f"The bonus is: ${sales}")
    sales = float(input("Enter sales: S"))