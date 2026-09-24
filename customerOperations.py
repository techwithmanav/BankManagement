def customer_operations(bank_data):

    print("\n====================================")
    print("        BANK CUSTOMER LIST")
    print("====================================")

    customer_set = set()

    for account_number in bank_data:

        customer_name = bank_data[account_number][1]

        customer_set.add(customer_name)

    if len(customer_set) == 0:

        print("No customers registered.")

    else:

        print("\nRegistered Customers:")
        print("------------------------------------")

        for customer_name in customer_set:
            print("-", customer_name)

        print("------------------------------------")
        print("Total Customers:", len(customer_set))