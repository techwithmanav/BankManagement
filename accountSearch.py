def account_search(bank_data):

    print("\n====================================")
    print("           SEARCH ACCOUNT")
    print("======================================")
    
    account_number = int(input("Enter account number: "))

    account_dictionary = bank_data

    found = False

    for number in account_dictionary:

        if number == account_number:

            print("\nAccount Found!")
            print("------------------------------------")
            print("Account Number:", bank_data[number][0])
            print("Customer Name:", bank_data[number][1])
            print("Phone Number:", bank_data[number][2])
            print("Email:", bank_data[number][3])
            print("------------------------------------")

            found = True

    if not found:
        print("\nAccount not found!")