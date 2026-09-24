def calculate_interest(bank_data):

    print("\n====================================")
    print("         INTEREST CALCULATOR")
    print("====================================")

    account_number = int(input("Enter your account number: "))

    if account_number not in bank_data:

        print("\nAccount not found!")
        return

    interest_rate = 5

    account_list = bank_data[account_number]

    account_details = (
        account_list[0],
        account_list[1],
        account_list[4]
    )

    interest_amount = (
        account_details[2] * interest_rate / 100
    )

    final_balance = (
        account_details[2] + interest_amount
    )

    print("\n====================================")
    print("       INTEREST CALCULATION")
    print("====================================")
    print("Account Number:", account_details[0])
    print("Customer Name:", account_details[1])
    print("Current Balance: ₹", account_details[2])
    print("Interest Rate:", interest_rate, "%")
    print("Annual Interest: ₹", interest_amount)
    print("Balance After Interest: ₹", final_balance)
    print("====================================")