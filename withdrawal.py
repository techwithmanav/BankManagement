def withdrawal(bank_data):

    print("\n====================================")
    print("          WITHDRAW MONEY")
    print("====================================")

    account_number = int(input("Enter your account number: "))

    if account_number not in bank_data:

        print("\nAccount not found!")
        return

    withdrawal_amount = float(
        input("Enter amount to withdraw: ₹")
    )

    account_list = bank_data[account_number]

    current_balance = account_list[4]

    if withdrawal_amount <= 0:

        print("\nPlease enter a valid amount.")

    elif withdrawal_amount > current_balance:

        print("\nInsufficient balance!")
        print("Available Balance: ₹", current_balance)

    else:

        account_list[4] = current_balance - withdrawal_amount

        account_list[5].append(
            "Withdraw: ₹" + str(withdrawal_amount)
        )

        print("\n====================================")
        print("      WITHDRAWAL SUCCESSFUL")
        print("====================================")
        print("Account Number:", account_number)
        print("Withdrawn Amount: ₹", withdrawal_amount)
        print("Remaining Balance: ₹", account_list[4])
        print("====================================")