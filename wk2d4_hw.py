# Build a shopping cart focusing on OOP


from os import remove


cart = []

def add_to_cart(category, food):
    cart_cat = {}
    cart_cat[category] = food
    cart.append(cart_cat)
    cart_cat = {}

def remove_from_cart(category, food):
    for i in cart:
        if category in i:
            i[category] = "NaN"

def go_shopping():
    lets_shop = "Y"
    shop_shop = input("Hi there. Would you like to go shopping? Y/N: ").upper()
    while lets_shop == "Y":
        if shop_shop == "N":
            lets_shop = "N"
            break
        which_aisle = input("Which aisle would you like to shop in? We have: \n 'Produce' \n 'Dairy' \n 'Deli' \n 'Snacks' \n 'Frozen' \n and 'Other' if you would like to walk around and look for something not listed.:  ").title()
        the_food = input(f"Awesome, we'll go shopping in the {which_aisle} area of the store. What would you like?: ").title()
        add_to_cart(which_aisle, the_food)
        print(f"Here's what your cart is looking like \n {cart}")
        keep_shopping = input("Would you like to keep shopping? Y/N: ").upper()
        print(f"Here is what is in your cart now. {cart}")
        if keep_shopping == "N":
            remove_stuff = input(f"Would you like to remove anything from your cart before leaving? Here is your cart \n {cart} \n Y/N: ").upper()
            if remove_stuff == "Y":
                what_category = input("What category would you like to remove from?: ").title()
                what_stuff = input("Which item would you like to remove?: ").title()
                remove_from_cart(what_category, what_stuff)
                lets_shop = 'N'
            lets_shop = "N"
go_shopping()

print(cart)




