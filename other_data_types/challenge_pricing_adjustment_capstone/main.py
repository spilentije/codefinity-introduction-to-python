grocery_inventory = {"Milk": ("Dairy", 3.50, 8), "Eggs": ("Dairy", 5.50, 30), "Bread": ("Bakery", 2.99, 15), "Apples": ("Produce", 1.5, 50)}
# Task 4: Manage Milk stock
milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (
        grocery_inventory["Milk"][0],
        grocery_inventory["Milk"][1],
        milk_stock + 20,
    )
else:
    print("Milk has sufficient stock.")
print("Updated inventory:", grocery_inventory)
eggs_price = grocery_inventory.get("Eggs")[1]
if eggs_price > 5:
    grocery_inventory["Eggs"] = (
    grocery_inventory["Eggs"][0],
    eggs_price - 1,
    grocery_inventory["Eggs"][2],
    )
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of Eggs is reasonable")
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory)

                      