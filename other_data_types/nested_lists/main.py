vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
if vegetables.count("carrots") == 0: 
    vegetables.append("carrots")
if vegetables.count("cucumbers") == 0: 
    vegetables.append("cucumbers")
vegetables.sort()
print(f"Updated Vegetable Inventory:, {vegetables}")
if vegetables.count("carrots") > 0: 
    print("Carrots are allready in the list.")
