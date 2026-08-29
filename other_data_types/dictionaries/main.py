grocery_inventory = {"Milk": (113, "Dairy"), "Eggs": (116, "Dairy"), "Bread": (117, "Bakery"), "Apples": (141, "Produce")}
bread_details = grocery_inventory.get("Bread")
grocery_inventory.update({"Cookies": (143, "Bakery")})
# or with: grocery_inventory["Cookies"] = (143, "Bakery")
print("Details of Bread:", bread_details)
print("Inventory after adding Cookies:", grocery_inventory)
grocery_inventory.pop("Eggs")
# print("Inventory after removing Eggs:", grocery_inventory)
print("Inventory after removing Eggs:", grocery_inventory)
print("Bread", grocery_inventory["Bread"], bread_details)

