# Stage 3: Smart Report Generator

# Sample list of items with prices (represented as tuples or parallel lists)
shopping_items = ["Apples", "Milk", "Bread", "Eggs", "Cheese"]
prices = [2.50, 1.20, 2.00, 3.10, 4.50]

print("=" * 30)
print("     SHOPPING LIST REPORT     ")
print("=" * 30)

total_cost = 0

# Looping through lists to summarize content
for i in range(len(shopping_items)):
    item = shopping_items[i]
    price = prices[i]
    total_cost += price
    print(f"- {item}: ${price:.2f}")

print("-" * 30)
print(f"Total Items : {len(shopping_items)}")
print(f"Total Cost  : ${total_cost:.2f}")

if shopping_items:
    average_cost = total_cost / len(shopping_items)
    print(f"Average Price: ${average_cost:.2f}")
print("=" * 30)
