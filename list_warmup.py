# Stage 1: List Operations Warmup

# Create an initial list
items = ["apples", "bread", "milk"]
print("Initial list:", items)

# Accessing items by index
print("First item:", items[0])
print("Last item:", items[-1])

# Growing the list using .append()
items.append("eggs")
items.append("cheese")
print("After appending eggs and cheese:", items)

# Shrinking the list using .remove() safely with 'in'
item_to_remove = "bread"
if item_to_remove in items:
    items.remove(item_to_remove)
    print(f"Removed '{item_to_remove}' successfully.")

print("Final list after warmup:", items)
