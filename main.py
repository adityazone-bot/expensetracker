import libs

def print_menu():
    print("1. Add expense")
    print("2. View expenses")
    print("3. Track budget")
    print("4. Save expenses")
    print("5. Exit")


tracker = libs.Tracker()


while True:
    print("")
    print_menu()
    option = int(input("Enter option: "))
    print("")

    if option == 1:
        tracker.input_expense()
    elif option == 2:
        tracker.view_expenses()
    elif option == 3:
        tracker.track_budget()
    elif option == 4:
        tracker.save_expenses()
    elif option == 5:
        break
    else:
        print("Invalid option selected! Try again!")
