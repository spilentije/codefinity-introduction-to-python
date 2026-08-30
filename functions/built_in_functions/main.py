# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []

for product_name, values in products.items():
    # Unpack strings
    price_str, quantity_str = values
    # Convert and calculate
    price = float(price_str)
    quantity = int(quantity_str)
    total_sales = price * quantity
    # Print and collect
    print(f"Total sales for {product_name}: ${total_sales}")
    total_sales_list.append(total_sales)

# Summary statistics
total_sum = sum(total_sales_list)
min_sales = min(total_sales_list)
max_sales = max(total_sales_list)

print(f"\nTotal sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")


