def account_creation(bank_data):

    print("\n====================================")
    print("       CREATE NEW ACCOUNT")
    print("====================================")

    customer_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email_address = input("Enter your email: ")
    initial_deposit = float(input("Enter initial deposit: ₹"))

    account_number = 1001 + len(bank_data)

    account_list = [
        account_number,
        customer_name,
        phone_number,
        email_address,
        initial_deposit,
        []
    ]

    bank_data[account_number] = account_list

    print("\nAccount Created Successfully!")
    print("------------------------------------")
    print("Your Account Number:", account_number)
    print("------------------------------------")