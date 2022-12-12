def dispense(item):
  print(f"Dispensing {item}...")

def select_item():
    print("Please select an item:")

    print("1. Crisps")
    print("2. Sweete")
    print("3. Drink")

    selection = int(input("Enter the number of the item you want to dispense: "))

    if selection == 1:
        dispense("chips")
    elif selection == 2:
        dispense("sweets")
    elif selection == 3:
        dispense("drink")
    else:
        print("Invalid selection. Please try again.")
select_item()
