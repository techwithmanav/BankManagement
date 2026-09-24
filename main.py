import accountCreation
import accountDisplay
import transactionHistory
import accountSearch
import balanceCheck
import withdrawal
import accountStatus
import depositMoney
import calculateInterest
import customerOperations


# ==========================================
# BANK DATA
# ==========================================

bank_data = {}


# ==========================================
# FILE HANDLING
# ==========================================

file_list = [
    "accountCreation.py",
    "accountDisplay.py",
    "transactionHistory.py",
    "accountSearch.py",
    "balanceCheck.py",
    "withdrawal.py",
    "accountStatus.py",
    "depositMoney.py",
    "calculateInterest.py",
    "customerOperations.py"
]


print("\n==========================================")
print("        PYTHON BANK MANAGEMENT")
print("==========================================")
print("        Secure | Simple | Reliable")
print("==========================================")


# ==========================================
# OPEN ALL PYTHON FILES
# ==========================================

for file_name in file_list:

    file = open(file_name, "r")

    file_data = file.read()

    file.close()


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n==========================================")
    print("              MAIN MENU")
    print("==========================================")

    print("1. Create New Account")
    print("2. Account Details")
    print("3. Check Balance")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Transaction History")
    print("7. Account Status")
    print("8. Search Account")
    print("9. Calculate Interest")
    print("10. View All Customers")
    print("11. Exit")

    choice = input("\nEnter your choice: ")


    # ======================================
    # CREATE ACCOUNT
    # ======================================

    if choice == "1":

        accountCreation.account_creation(bank_data)


    # ======================================
    # ACCOUNT DETAILS
    # ======================================

    elif choice == "2":

        if len(bank_data) == 0:

            print("\nNo accounts have been created yet.")

        else:

            accountDisplay.account_display(bank_data)


    # ======================================
    # CHECK BALANCE
    # ======================================

    elif choice == "3":

        if len(bank_data) == 0:

            print("\nNo accounts have been created yet.")

        else:

            balanceCheck.balance_check(bank_data)


    # ======================================
    # DEPOSIT MONEY
    # ======================================

    elif choice == "4":

        if len(bank_data) == 0:

            print("\nNo accounts have been created yet.")

        else:

            depositMoney.deposit_money(bank_data)


    # ======================================
    # WITHDRAW MONEY
    # ======================================

    elif choice == "5":

        if len(bank_data) == 0:

            print("\nNo accounts have been created yet.")

        else:

            withdrawal.withdrawal(bank_data)


    # ======================================
    # TRANSACTION HISTORY
    # ======================================

    elif choice == "6":

        if len(bank_data) == 0:

            print("\nNo accounts have been created yet.")

        else:

            transactionHistory.transaction_history(bank_data)


    # ======================================
    # ACCOUNT STATUS
    # ======================================

    elif choice == "7":

        if len(bank_data) == 0:

            print("\nNo accounts have been created yet.")

        else:

            accountStatus.account_status(bank_data)


    # ======================================
    # SEARCH ACCOUNT
    # ======================================

    elif choice == "8":

        if len(bank_data) == 0:

            print("\nNo accounts have been created yet.")

        else:

            accountSearch.account_search(bank_data)


    # ======================================
    # CALCULATE INTEREST
    # ======================================

    elif choice == "9":

        if len(bank_data) == 0:

            print("\nNo accounts have been created yet.")

        else:

            calculateInterest.calculate_interest(bank_data)


    # ======================================
    # VIEW ALL CUSTOMERS
    # ======================================

    elif choice == "10":

        customerOperations.customer_operations(bank_data)


    # ======================================
    # EXIT
    # ======================================

    elif choice == "11":

        print("\n==========================================")
        print("       THANK YOU FOR USING PYTHON BANK")
        print("==========================================")
        print("             Have a nice day!")
        print("==========================================")

        break


    # ======================================
    # INVALID CHOICE
    # ======================================

    else:

        print("\nInvalid choice!")
        print("Please select a number from 1 to 11.")