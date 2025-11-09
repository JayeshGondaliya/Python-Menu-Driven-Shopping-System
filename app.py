def main_menu():
    print("[1] Admin ")
    print("[2] User")


def Admin_menu():
    print("[1] Add Product ")
    print("[2] Display Product")
    print("[3] Delete Product")
    print("[4] Update Product")
    print("[5] Exit")


def User_menu():
    print("[1] Add To Cart")
    print("[2] Display Cart")
    print("[3] Delete To Cart")
    print("[4] Update To Cart")
    print("[5] Exit")


product_list = []


def add_product():
    p_id = int(input("Enter Product Id:->"))
    for p in product_list:
        if p[0] == p_id:
            print("❌ Product is already exists")
            return
    p_name = input("Enter Product Name:->")
    p_price = float(input("Enter Product Price:->"))

    new_product = [p_id, p_name, p_price]
    product_list.append(new_product)
    print("✅SuccessFully Item Added By Admin")


def display_product():
    if not product_list:
        print("\n⚠️ No Products Available!")
        print()
        return

    print("\n" + "="*45)
    print("🛍️ AVAILABLE PRODUCTS")
    print("="*45)
    print(f"{'Product ID':<12}{'Product Name':<20}{'Price (₹)':<10}")
    print("-"*45)

    for p in product_list:
        print(f"{p[0]:<12}{p[1]:<20}{p[2]:<10.2f}")

    print("="*45)


def delete_product():
    if not product_list:
        print("\n⚠️ No Products Available!")
        print()
        return
    found = False
    new_p_id = int(input("Enter Pid to be delete:------------>"))
    for p in product_list:
        if p[0] == new_p_id:
            delete_list = [p[0], p[1], p[2]]
            product_list.remove(delete_list)
            found = True
            print("✅Product Delete SuccessFully")
        print()
    if found != True:
        print("❌ Product Not Found")


def update_product():
    if not product_list:
        print("\n⚠️ No Products Available!")
        print()
        return
    found = False
    p_id = int(input("Enter Product Id:------------>"))
    for p in product_list:
        if p[0] == p_id:

            print("---------------:Enter New Data :----------")
            new_p_name = input("Enter Product Name:---------->")
            new_p_price = float(input("Enter Prodcut Price:-------->"))
            p[1] = new_p_name
            p[2] = new_p_price
            found = True
            print("✅Update SuccessFully")

    if found != True:
        print(" Product Not Found")


cart_item_list = []


def add_to_cart():
    display_product()
    print()
    print("Enter the product to the cart")

    pid = int(input("Enter pid:-------->"))
    pquantity = int(input("Enter Quantity:--->"))

    for p in product_list:
        if p[0] == pid:

            # check if product is in already cart
            for c in cart_item_list:
                if c[0] == pid:
                    c[3] += pquantity
                    print("✅ Quantity updated in cart.")
                    return
            # if not in cart item so then add into cart
            new_cart_list = [pid, p[1], p[2], pquantity]
            cart_item_list.append(new_cart_list)
            print("✅ Product Added Into Cart.")
            return
    print("❌ Invalid Product ID — please try again.")


print()


def display_cart_total(list):
    if not list:
        print("not any item into cart")
        return
    sum = 0
    for a in list:
        sum += a[2]*a[3]

    return sum


def display_cart():
    if not cart_item_list:
        print("\n⚠️ No Products Available in Cart!")
        print()
        return

    total = display_cart_total(cart_item_list)

    print("\n" + "=" * 60)
    print("🛒 CART ITEMS")
    print("=" * 60)
    print(f"{'Product ID':<12}{'Product Name':<20}{'Price (₹)':<10}{'Quantity':<10}{'Subtotal(₹)':<10}")
    print("-" * 60)

    # Each item + subtotal
    for c in cart_item_list:
        subtotal = c[2] * c[3]
        print(f"{c[0]:<12}{c[1]:<20}{c[2]:<10.2f}{c[3]:<10}{subtotal:<10.2f}")

    print("-" * 60)
    print(f"{'TOTAL AMOUNT (₹)':<52}{total:<10.2f}")
    print("=" * 60)


def delete_from_cart():
    if not cart_item_list:
        print("❌ No Records Available")
        return

    pid = int(input("Enter Pid for item delete:----->"))
    found = False
    for p in cart_item_list:
        if p[0] == pid:
            delete_list = [pid, p[1], p[2], p[3]]
            cart_item_list.remove(delete_list)
            print("✅ Item delete successfully")
            found = True

    if found != True:
        print("❌ Not Found ! please enter valid Product Id")


def update_from_cart():
    if not cart_item_list:
        print("❌ No Records Available")
        return
    pid = int(input("Enter Pid for item Update:----->"))
    found = False
    for c in cart_item_list:
        if c[0] == pid:
            pquantity = int(input("Enter new quantity"))
            c[3] = pquantity
            found = True
            print("✅ Cart Item Updated Successfully")

    if found != True:
        print("❌ Not Found ! please enter valid Product Id")
# ----------- MAIN FUNCTION ------------


def main_funtion():
    while True:
        main_menu()
        choice = int(input("Enter Your Choice -----> "))
        match choice:
            case 1:  # Admin Panel
                while True:
                    Admin_menu()
                    Admin_choice = int(input("Enter Admin Choice -----> "))
                    match Admin_choice:
                        case 1:
                            add_product()
                        case 2:
                            display_product()
                        case 3:
                            delete_product()
                        case 4:
                            update_product()
                        case 5:
                            print("🔙 Returning to Main Menu...")
                            break
                        case _:
                            print("❌ Invalid Choice!")
            case 2:  # User Panel
                while True:
                    User_menu()
                    user_choice = int(input("Enter User Choice -----> "))
                    match user_choice:
                        case 1:
                            add_to_cart()
                        case 2:
                            display_cart()
                        case 3:
                            delete_from_cart()
                        case 4:
                            update_from_cart()
                        case 5:
                            print("🔙 Returning to Main Menu...")
                            break
                        case _:
                            print("❌ Invalid Choice!")
            case 0:
                print("👋 Thank You! Exiting the Program...")
                exit()
            case _:
                print("❌ Invalid Choice! Try Again.")


# Run Program
main_funtion()
