# Part A — List Warmup

# 1. Create a list called fruits containing four fruits
fruits = ["apple", "banana", "mango", "orange"]

# 2. Print the first and the last item using indexes
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# 3. .append() a fifth fruit, then print the whole list
fruits.append("pineapple")
print(f"List after adding a fruit: {fruits}")

# 4. .remove() one fruit, then print the list again
fruits.remove("banana")
print(f"List after removing banana: {fruits}")

cat << 'EOF' > shopping_list.py
# Part B — Shopping List Manager

# Start with an empty list
shopping_list = []

while True:
    print("\n--- Shopping List Manager ---")
    action = input("Choose an action (add / remove / show / done): ").strip().lower()

    if action == "add":
        item = input("Enter item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"'{item}' added to the list.")
        else:
            print("Item cannot be empty.")

cat << 'EOF' > list_report.py
# Part C — List Report

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 1. Loop through the list and print each item numbered
print("--- Numbered Shopping Items ---")
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")

# 2. Count how many item names have more than 4 letters
long_name_count = 0
for item in items:
    if len(item) > 4:
        long_name_count += 1

print(f"\nNumber of items with more than 4 letters: {long_name_count}")

# 3. Find and print the longest item name using a loop comparison
longest_item = items[0]
for item in items:
    if len(item) > len(longest_item):
        longest_item = item

print(f"The longest item name is: {longest_item}")
