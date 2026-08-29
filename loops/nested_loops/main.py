produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries = [produce, dairy]
for section in range(len(produce)):
    print(f"{produce[section]}")
    for item in range(len(dairy)):
        print(f"Item name: {dairy[item]}")
