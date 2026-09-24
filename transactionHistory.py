def transaction_history(bank_data):

    print("\n====================================")
    print("        TRANSACTION HISTORY")
    print("====================================")

    account_number = int(input("Enter your account number: "))

    if account_number not in bank_data:
        print("\nAccount not found!")
        return

    transaction_list = bank_data[account_number][5]

    print("\n------------------------------------")

    if len(transaction_list) == 0:
        print("No transactions available.")

    else:
        transaction_index = 0

        while transaction_index < len(transaction_list):

            print(
                transaction_index + 1,
                ".",
                transaction_list[transaction_index]
            )

            transaction_index += 1

    print("------------------------------------")