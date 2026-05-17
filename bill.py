purchase_amount = float(input("Enter your purchase amount:"))

if purchase_amount > 5000:
    membership = input("Is membership card present(Yes/No):").lower().strip()
    if membership == "yes":
        discount = purchase_amount * 0.30
        print(f"Total discount: Rs. {discount:.2f}")
        print(f"Total amount : Rs. {purchase_amount - discount:.2f}")
    else:
        print(f"Total: Rs. {purchase_amount:.2f}, Discount Rs. 0")
else:
    print(f"Total: Rs. {purchase_amount:.2f}, Discount Rs. 0")
