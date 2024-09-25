def calculate_discount(purchase_amount):
    if purchase_amount > 5000:
        discount = purchase_amount * 0.10
    else:
        discount = purchase_amount * 0.05
    final_price = purchase_amount - discount
    return discount, final_price


while True:
    purchase_amount = float(input("Enter the total purchase amount: "))
    discount, final_price = calculate_discount(purchase_amount)

    print(f"Initial Purchase Amount: {purchase_amount:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Final Price: {final_price:.2f}")

    try_again = input("Do you want to try again? (yes/no): ")
    if try_again != "yes":
        print("Thank you!")
        break
