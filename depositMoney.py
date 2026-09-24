def deposit_money(bank_data):

    print("\n====================================")
    print("           DEPOSIT MONEY")
    print("====================================")

    account_number = int(input("Enter your account number: "))

    if account_number not in bank_data:

        print("\nAccount not found!")
        return

    deposit_amount = float(
        input("Enter amount to deposit: ₹")
    )

    if deposit_amount <= 0:

        print("\nPlease enter a valid amount.")
        return

    account_list = bank_data[account_number]

    account_details = (
        account_list[0],
        account_list[1],
        account_list[4]
    )

    old_balance = account_details[2]

    new_balance = old_balance + deposit_amount

    account_list[4] = new_balance

    account_list[5].append(
        "Deposit: ₹" + str(deposit_amount)
    )

    print("\n====================================")
    print("        DEPOSIT SUCCESSFUL")
    print("====================================")
    print("Account Number:", account_details[0])
    print("Customer Name:", account_details[1])
    print("Deposited Amount: ₹", deposit_amount)
    print("Old Balance: ₹", old_balance)
    print("New Balance: ₹", new_balance)
    print("====================================")