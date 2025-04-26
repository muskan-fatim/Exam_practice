print("Shopping Cart")
print("1. Add item to cart" ,"2. Remove item from cart" ,"3. View cart"  , "5. Exit")
print("Enter number not of task that you want to performe")
cart = []
while True:
    choice = input("Enter your choice:")
    if choice == "1":
        add = input("Enter your item to cart")
        cart.append(add)
    elif choice == "2":
        remove = input("Enter your item to remove from cart")
        if remove in cart:
            cart.remove(f"succesfully {remove}")
        else:
            print("Item not found in cart")
    elif choice == "3":
        print("Your cart contains:" + str(cart))
    elif choice == "4":
        print("Exiting the program")
        break
