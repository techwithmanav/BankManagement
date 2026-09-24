def account_display(bank_data):

    print("\n====================================")
    print("       ACCOUNT DETAILS")
    print("====================================")

    account_number = int(input("Enter your account number: "))

    if account_number in bank_data:

        account_dictionary = {
            "Account Number": bank_data[account_number][0],
            "Customer Name": bank_data[account_number][1],
            "Phone Number": bank_data[account_number][2],
            "Email": bank_data[account_number][3],
            "Balance": bank_data[account_number][4]
        }

        print("\n------------------------------------")

        for key, value in account_dictionary.items():
            print(key + ":", value)

        print("------------------------------------")

    else:
        print("\nAccount not found!")