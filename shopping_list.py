# Stage 2: Shopping List Manager

shopping_list = []

def show_menu():
    print("\n--- SHOPPING LIST MANAGER ---")
    print("1. View List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ").strip()
    
    if choice == "1":
        if not shopping_list:
            print("\nYour shopping list is empty.")
        else:
            print("\nYour Current Shopping List:")
            for index, item in enumerate(shopping_list, start=1):
                print(f"{index}. {item}")
                
    elif choice == "2":
        new_item = input("\nEnter the item to add: ").strip()
        if new_item:
            shopping_list.append(new_item)
            print(f"'{new_item}' has been added.")
        else:
            print("Item name cannot be empty.")
            
    elif choice == "3":
        remove_item = input("\nEnter the item to remove: ").strip()
        # Checking membership before removing
        if remove_item in shopping_list:
            shopping_list.remove(remove_item)
            print(f"'{remove_item}' has been removed.")
        else:
            print(f"'{remove_item}' was not found in your list.")
            
    elif choice == "4":
        print("\nExiting Shopping List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
