def account_status(bank_data):

    print("\n====================================")
    print("          ACCOUNT STATUS")
    print("====================================")

    account_number = int(input("Enter your account number: "))

    active_accounts = set(bank_data.keys())

    if account_number in active_accounts:

        print("\nAccount Found!")
        print("------------------------------------")
        print("Account Number:", account_number)
        print("Account Holder:", bank_data[account_number][1])
        print("Status: ACTIVE")
        print("------------------------------------")

    else:

        print("\nAccount not found!")
        print("Status: INACTIVE")