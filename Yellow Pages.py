dictPages = {
    "PT Cahaya Abadi": {
        "no_telp": 6262818912919,
        "address":"Jl. Raya Kapal Mangapura, Kapal, Mengwi, Badung"
    },
    "PT Kasih Sayang": {
        "no_telp": 6289624942032,
        "address":"Jl. Petitenget, Kerobokan Kelod, Kuta Utara, Badung"
    },
    "PT Jaya Selamanya": {
        "no_telp": 6287863399212,
        "address":"Jl. Gatot Subroto Timur, Denpasar Utara, Denpasar"
    }
}

def menu():
    print("==========================================================================================================")
    print("\t\t\t\t Welcome to Yellow Pages Apps")
    print("\t\t\t\t Created by William | JCDSOL-019")
    print("==========================================================================================================")
    print("1. Contact List")
    print("2. Create Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Add Column to Yellow Pages")
    print("7. Exit")

def listPages():
    print("----------------------------------------------------------------------------------------------------------")
    header = "| No | Contact Name\t\t| Number\t | Address \t\t\t\t\t\t |"
    
    # Check if any contact has additional columns to create header
    additional_columns = set()
    for contact_details in dictPages.values():
        additional_columns.update(contact_details.keys() - {"no_telp", "address"})

    for col in additional_columns:
        header += f" {col}\t |"
        
    print(header)
    print("----------------------------------------------------------------------------------------------------------")

    count = 1

    for key, contact_details in dictPages.items():
        row = f"| {count:<3}| {key:<24} | {contact_details['no_telp']:<14} | {contact_details['address']:<53} |"
        
        for col in additional_columns:
            row += f" {contact_details.get(col, ''):<10}\t |"
        
        print(row)
        print("----------------------------------------------------------------------------------------------------------")
        count += 1


def checkInput(input_user):
    while True:
        checking = input(input_user)

        if checking:
            return checking
        
        print("Your Input Cannot be Empty")
    
def createNewPages():
    input_contact_name = checkInput("Please input your Contact Name : ")

    input_phone_number = checkInput("Please input your Phone Number : ")

    input_address = checkInput("Please input your Address : ")
        
    dictPages[input_contact_name] = {
        "no_telp" : input_phone_number,
        "address" : input_address
    }

def editMenuPages():
    print("What do you want to change?")
    print("1. Contact Name")
    print("2. Contact Number")
    print("3. Address")
    print("4. Cancel")

    return checkInput("Please input your choice : ")

def editPages():
    listPages()
    print("Which contact you want to edit? ")

    while True:
        check_availibity_index = len(dictPages)

        input_number_of_contact = checkInput("Please input your Number of Contact from the list Above : ")

        input_number_of_contact = int(input_number_of_contact)

        if check_availibity_index < input_number_of_contact:
            print("Error, please try again")
        else:
            break

    x = list(dictPages)[input_number_of_contact-1]
    y = dictPages[x]

    input_edit_menu = editMenuPages()

    input_edit_menu = int(input_edit_menu)

    while True:
        if input_edit_menu == 1:
            input_contact_name = str(input("Please input your Contact Name : "))

            del dictPages[x]
            dictPages[input_contact_name] = y

            print("Data edit successful!")
            break

        elif input_edit_menu == 2:
            input_no_telp = input("Please input your Contact Number : ")

            dictPages[x]["no_telp"] = input_no_telp
            
            print("Data edit successful!")

            break
            
        elif input_edit_menu == 3: 
            input_address = input("Please input your Address : ")

            dictPages[x]["address"] = input_address

            print("Data edit successful!")
            break

        else:
            print("The data edit failed!")
            continue

def deletePages():
    listPages()
    print("Which contact you want to delete? ")
    
    while True:
        check_availibity_index = len(dictPages)

        input_delete_pages = checkInput("Please input your Number of Contact from the list Above : ")

        input_delete_pages = int(input_delete_pages)

        if check_availibity_index < input_delete_pages:
            print("Error, Record not found!")
        else:
            break

    x = list(dictPages)[input_delete_pages-1]

    print("----------------------------------------------------------------------------------------------------------")
    print(f"| Contact Name\t\t| Number\t | Address \t\t\t\t\t\t |")
    print("----------------------------------------------------------------------------------------------------------")

    print(f"| {x:<21} | {dictPages[x]["no_telp"]:<14} | {dictPages[x]["address"]}\t |")

    confirm_delete = checkInput("Is this the data for deletion? (y/n) ")

    if confirm_delete == "y" or confirm_delete == "Y":
        del dictPages[x]
        print("Data has been deleted!")

def searchUser():
    searching = str(input("Please input your Contact Name: "))
    searching_result = dict(filter(lambda item: searching.lower() in item[0].lower(), dictPages.items()))

    if searching_result:
        print("Your Search results:")

        header = "| Contact Name\t\t| Number\t | Address \t\t\t\t\t\t |"

        # Check if any contact has additional columns to create header
        additional_columns = set()
        for contact_details in searching_result.values():
            additional_columns.update(contact_details.keys() - {"no_telp", "address"})

        for col in additional_columns:
            header += f" {col}\t |"
        print(header)
        print("---------------------------------------------------------------------------------------------------------------------")

        for contact_name, contact_details in searching_result.items():
            row = f"| {contact_name:<24} | {contact_details['no_telp']:<14} | {contact_details['address']:<53} |"
            
            for col in additional_columns:
                row += f" {contact_details.get(col, ''):<10}\t |"
            
            print(row)
            print("---------------------------------------------------------------------------------------------------------------------")

        print(f"We found : {len(searching_result)} result from your keywords")

    else:
        print("No matching contacts found.")

def addColumntoPages(): 
    listPages()
    
    while True:
        check_availibity_index = len(dictPages)

        input_contact_number = checkInput("Please input your Number of Contact that you want to add : ")

        input_contact_number = int(input_contact_number)

        if check_availibity_index < input_contact_number:
            print("Error, Record not found!")
        else:
            break

    input_column_name = checkInput("What Column Name you want to input : ")
    input_column_name_desc = checkInput("What is the content : ")
    
    x = list(dictPages)[input_contact_number-1]
    dictPages[x][input_column_name] = input_column_name_desc

    print("Data edit successful!")

menu()

while True : 
    input_menu_user = str(input("Please Enter Menu : "))
    if input_menu_user == "1":
        listPages()
        menu()

    elif input_menu_user == "2":
        createNewPages()
        listPages()
        menu()

    elif input_menu_user == "3":
        editPages()
        menu()

    elif input_menu_user == "4":
        deletePages()
        menu()
        
    elif input_menu_user == "5":
        searchUser()
        menu()

    elif input_menu_user == "6":
        addColumntoPages()
        menu()

    elif input_menu_user == "7" or input_menu_user == "" : 
        print("Thank you for using my application")
        break

    else:
        print("Your input is wrong")
        print("Please try again!")
