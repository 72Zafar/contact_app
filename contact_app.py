contact = { }

while True:
    print("\n Contact book app")
    print("1. create contact")
    print("2. view contact")
    print("3. updata contact")
    print("4. delete contact")
    print("5. search contact")
    print("6. count contact")
    print("7. exit")

    choice = int(input("enter your choice: "))
    if choice == 1:
        name = input("enter your name: ")
        if name in contact:
            print(f"contact name is {name} already exists")

        else:
            age = input("enter age: ")
            email = input("enter email: ")
            mobile = input("enter the mobile number: ") 
            contact[name] = {'age':int(age),'email':email,'mobile':mobile}  
            print(f"contact name {name} has been create successfully")  

    elif choice == 2:
        name = input("enter contact name to view: ")
        if name in contact:
            all_contact = contact[name]
            print(f"name:{name},Age:{age},email:{email},mobile:{mobile}") 

        else:
            print("name is not a found")           

    elif choice == 3:
        name = input("enter name to update contact: ")
        if name in contact:
             age = input("enter update age: ")
             email = input("enter update email: ")
             mobile = input("enter update mobile number: ") 
             contact[name] = {'age':int(age),'email':email,'mobile':mobile}  
        else:
            print(f"contact not found")     

    elif choice == 4:
        name = input("enter name to dalete contact: ")
        if name in contact:
            del contact[name]
            print(f"contact name {name} has been deleted successfully") 

        else:
            print("contact not found")           

    elif choice == 5:
        search_name = input("enter contact name to search: ")
        found = False
        for name ,all_contact in contact.items():
            if search_name.lower() in name.lower():
                print(f"found name {name}, age:{age}, mobile number:{mobile}, email:{email}")
                found  = True
        if not found:
            print("np contact found with that name") 

    elif choice == 6:
        print(f"total contact in your book: {len(contact)}")

    elif choice == 7:
        print("good buy .. closing the program")
        break

    else:
        print("invalid input")                   
        

