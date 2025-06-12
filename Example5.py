while True:
    print("Menu:")
    print("1. Say Hello")
    print("2. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
