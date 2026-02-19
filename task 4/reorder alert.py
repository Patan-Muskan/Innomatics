products = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 2,
    "Monitor": 30
}
# check stock
def check_stock(product):
    if stock < 15:
        return "Reorder alert"
    else:
        return "Stock OK"
# loop through dictionary
for product, quantity in products.items():
    stock = quantity
    print(product, ":", check_stock(quantity))

   