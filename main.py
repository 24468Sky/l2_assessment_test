inventory = {"Mele": "Sword", "Shield": "Royal Shield", "Bow": "Lizal bow"}
def menu():
    print(" Menu\n", "'1'Show inventory\n", "'2'Drop an item\n", "'3'End\n")
def show_inventory():
    for item, value in inventory.items():
        print(f"{item}: {value}")
def drop_item():
    print("What item would you like to drop?")
    print(" '1'Mele\n", "'2'Shield\n", "'3'Bow")
    choice = input(">>> ")

    if choice == '1':
        inventory['Mele'] = 'Nothing'
    elif choice == '2':
        inventory['Shield'] = 'Royal Shield'
    elif choice == '3':
        inventory['Bow'] = ' Lizal bow'
# main routine
while True:
    menu()
    option = input(">>> ")

    if option == '1':
        show_inventory()
    elif option == '2':
        drop_item()
    elif option == '3':
        break
    else:
        print("Invalid option. Please choose again.")