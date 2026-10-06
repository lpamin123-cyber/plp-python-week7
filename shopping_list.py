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

python list_warmup.py
python shopping_list.py
python list_report.py
cat << 'EOF' > README.md
# Week 7 Assignment: Shopping List Manager

## Overview
This repository contains Python programs developed for the PLP Python Week 7 assignment, covering basic list operations, interactive input management, and procedural data analysis.

## Files Description
* `list_warmup.py`: Demonstrates basic list operations including index access, `.append()`, `.remove()`, and `len()`.
* `shopping_list.py`: An interactive CLI tool to manage a shopping list supporting addition, safe removal, and display functions.
* `list_report.py`: Analyzes a list of items to format a numbered output, count items based on string length, and identify the longest item name using a comparative loop.
* `screenshots/`: Contains execution output screenshots for each script.

## Safety Reflection: Checking Membership with `in`
It is safer to check `if item in list:` before calling `.remove()` because calling `.remove()` on an item that does not exist raises a `ValueError` in Python, which crashes the program. Checking membership beforehand guarantees safe handling of missing items and prevents execution errors, ensuring a smooth user experience.
