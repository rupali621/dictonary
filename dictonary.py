#introducing dictionary 
phoneDirectory = {}

choice=0
#concept of loops
while (choice!=5):
#entering given directories
    print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
    print("1. Add a record")
    print("2. Search a record")
    print("3. Update a record")
    print("4. Delete a record")
    print("5. Quit")
#entering inputs
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter your 10-digit phone number: ")
        
        print("Record added")
    elif choice == 2:
        name = input("Enter name: ")
        if name in phoneDirectory:
            print("Phone number:", phoneDirectory[name])
        else:
            print("Record not found")
    elif choice == 3:
        name = input("Enter name: ")
        if name in phoneDirectory:
            phone = input("Enter new phone number: ")
            
            print("Record updated")
        else:
            print("Record not found")
          
    elif choice == 4:
        name = input("Enter name: ")
        if name in phoneDirectory:
            
            print("Record deleted")
        else:
            print("Record not found")

    elif choice == 5:
        break

    else:
        print("Invalid choice")