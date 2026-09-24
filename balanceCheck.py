def balance_check(bank_data):

    print("\n====================================")
    print("           CHECK BALANCE")
    print("====================================")

    account_number = int(input("Enter your account number: "))

    account_balance = {}

    for number in bank_data:
        account_balance[number] = bank_data[number][4]

    if account_number in account_balance:

        print("\nAccount Found!")
        print("------------------------------------")
        print("Account Number:", account_number)
        print("Current Balance: ₹", account_balance[account_number])
        print("------------------------------------")

    else:

        print("\nAccount not found!")