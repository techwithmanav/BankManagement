# 🏦 Bank Account Management System

<div align="center">

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Level-Beginner-2EA44F?style=for-the-badge" />
<img src="https://img.shields.io/badge/Project-Mini%20Project-FF8C00?style=for-the-badge" />
<img src="https://img.shields.io/badge/Platform-Console-24292F?style=for-the-badge" />

<br><br>

🏦 &nbsp; 💳 &nbsp; 💰 &nbsp; 🧾 &nbsp; 📊

<h2>🐍 A Beginner-Friendly Python Banking Application</h2>

<p>
  <b>Account Creation • Deposit • Withdrawal • Balance • Transactions • Interest</b>
</p>

<br>

<a href="#-features">
  <img src="https://img.shields.io/badge/✨%20Explore%20Features-ff6b35?style=for-the-badge" />
</a>

&nbsp;&nbsp;

<a href="#-installation--setup">
  <img src="https://img.shields.io/badge/▶️%20Run%20Project-2ea44f?style=for-the-badge" />
</a>

<br><br>

<a href="https://github.com/techwithmanav/BankManagement">
  <img src="https://img.shields.io/badge/View%20on-GitHub-181717?style=for-the-badge&logo=github" />
</a>

</div>

---

> 🏦 **A practical Python mini project that combines basic programming concepts to simulate a real-world bank account management system.**

---

## 📑 Table of Contents

- [🌟 Overview](#-overview)
- [📊 Project Snapshot](#-project-snapshot)
- [✨ Features](#-features)
- [🏦 Account Management](#-account-management)
- [💰 Transactions](#-transactions)
- [🧾 Transaction History](#-transaction-history)
- [📈 Interest Calculator](#-interest-calculator)
- [👥 Customer Management](#-customer-management)
- [🔄 Application Flow](#-application-flow)
- [🧩 Functions](#-functions)
- [🛠️ Technologies & Concepts](#️-technologies--concepts)
- [📂 Project Structure](#-project-structure)
- [🚀 Installation & Setup](#-installation--setup)
- [🖥️ Terminal Preview](#️-terminal-preview)
- [📚 Learning Outcomes](#-learning-outcomes)
- [💡 Why This Project](#-why-this-project)
- [🚀 Future Roadmap](#-future-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🌟 Overview

The **Bank Account Management System** is a Python-based console application that simulates basic banking operations.

Customers can:

- 📝 Create a bank account
- 👤 View account details
- 💰 Check account balance
- 💵 Deposit money
- 💸 Withdraw money
- 🧾 View transaction history
- 🔍 Search for an account
- 🔐 Check account status
- 📈 Calculate interest
- 👥 View registered customers

The project is intentionally designed using **beginner-level Python concepts**, making it suitable for learning functions, modules, data structures, loops, conditions, and file handling.

---

## 📊 Project Snapshot

<div align="center">

| 🐍 Python | 🎯 Level | 🏦 Accounts | 💰 Transactions | 📂 Modules |
|:---:|:---:|:---:|:---:|:---:|
| 3.x | Beginner | ✅ | ✅ | ✅ |

| 💵 Deposit | 💸 Withdrawal | 📊 Balance | 📈 Interest | 👥 Customers |
|:---:|:---:|:---:|:---:|:---:|
| ✅ | ✅ | ✅ | ✅ | ✅ |

</div>

---

## ✨ Features

| Feature | Description |
|---|---|
| 📝 **Account Creation** | Creates a new customer account |
| 👤 **Account Details** | Displays customer and account information |
| 📞 **Customer Information** | Stores name, phone and email |
| 💰 **Balance Check** | Displays the current account balance |
| 💵 **Deposit Money** | Adds money to an account |
| 💸 **Withdrawal** | Withdraws money after balance validation |
| 🧾 **Transaction History** | Records deposits and withdrawals |
| 🔍 **Account Search** | Searches for an account using account number |
| 🔐 **Account Status** | Checks whether an account is active |
| 📈 **Interest Calculator** | Calculates annual interest |
| 👥 **Customer List** | Displays registered customers |
| 📂 **File Handling** | Opens and reads Python files using `open()` |

---

# 🏦 Account Management

## 📝 Account Creation

Customers can create a new account by entering:

```text
👤 Full Name
📞 Phone Number
📧 Email Address
💰 Initial Deposit
````

After successful registration, the system generates an account number.

```text
====================================
       🏦 CREATE NEW ACCOUNT
====================================

👤 Enter your full name: Manav
📞 Enter your phone number: 9876543210
📧 Enter your email: manav@gmail.com
💰 Enter initial deposit: ₹5000

🏦 Account Created Successfully!
------------------------------------
💳 Your Account Number: 1001
------------------------------------
```

---

## 👤 Account Details

Customers can enter their account number to view:

```text
💳 Account Number
👤 Customer Name
📞 Phone Number
📧 Email
💰 Balance
```

---

# 💰 Transactions

## 💵 Deposit Money

Customers can add money to their account.

```text
====================================
        🏦💵 DEPOSIT MONEY
====================================

💳 Enter your account number: 1001
💵 Enter amount to deposit: ₹2000

====================================
        ✅ DEPOSIT SUCCESSFUL
====================================
💳 Account Number: 1001
👤 Customer Name: Manav
💵 Deposited Amount: ₹2000
💰 Old Balance: ₹5000
💰 New Balance: ₹7000
====================================
```

---

## 💸 Withdrawal

The system checks whether the customer has sufficient balance before completing a withdrawal.

```text
💳 Account Number: 1001
💸 Enter amount to withdraw: ₹1500

====================================
      ✅ WITHDRAWAL SUCCESSFUL
====================================

💳 Account Number: 1001
💸 Withdrawn Amount: ₹1500
💰 Remaining Balance: ₹5500
```

If the requested amount is greater than the available balance:

```text
❌ Insufficient balance!
💰 Available Balance: ₹500
```

---

# 📊 Balance Check

Customers can check their current account balance at any time.

```text
====================================
          💰 CHECK BALANCE
====================================

💳 Account Number: 1001
💰 Current Balance: ₹5500
```

---

# 🧾 Transaction History

Every deposit and withdrawal is stored in the account's transaction history.

```text
====================================
        🧾 TRANSACTION HISTORY
====================================

1. 💵 Deposit: ₹2000
2. 💸 Withdraw: ₹1500
3. 💵 Deposit: ₹1000
```

If there are no transactions:

```text
📭 No transactions available.
```

---

# 🔍 Account Search

The search feature allows users to find an account using its account number.

```text
====================================
          🔍 SEARCH ACCOUNT
====================================

💳 Enter account number: 1001

✅ Account Found!
------------------------------------
💳 Account Number: 1001
👤 Customer Name: Manav
📞 Phone Number: 9876543210
📧 Email: manav@gmail.com
------------------------------------
```

---

# 🔐 Account Status

The system uses account information to determine whether an account is active.

```text
====================================
          🔐 ACCOUNT STATUS
====================================

💳 Account Number: 1001

✅ Account Found!
------------------------------------
💳 Account Number: 1001
👤 Account Holder: Manav
🔐 Status: ACTIVE
------------------------------------
```

---

# 📈 Interest Calculator

The application calculates annual interest using the account balance and interest rate.

```text
====================================
       📈 INTEREST CALCULATION
====================================

💳 Account Number: 1001
👤 Customer Name: Manav
💰 Current Balance: ₹5000
📈 Interest Rate: 5 %
💵 Annual Interest: ₹250
💰 Balance After Interest: ₹5250
====================================
```

> 📌 The current project uses a **5% interest rate** for calculation.

---

# 👥 Customer Management

The customer operations feature displays registered customers.

```text
====================================
        👥 BANK CUSTOMER LIST
====================================

👥 Registered Customers:
------------------------------------
👤 Manav
👤 Rahul
👤 Aman
------------------------------------
👥 Total Customers: 3
```

---

# 🔄 Application Flow

```text
🚀 START
   │
   ▼
🏦 MAIN MENU
   │
   ├───────────────┐
   ▼               ▼
📝 CREATE       👤 ACCOUNT
ACCOUNT         SERVICES
   │               │
   │       ┌───────┼────────┐
   │       ▼       ▼        ▼
   │     💰      🔍       🔐
   │   Balance  Search   Status
   │
   ▼
💳 ACCOUNT CREATED
   │
   ▼
💰 TRANSACTIONS
   │
   ┌──────────────┐
   ▼              ▼
💵 Deposit     💸 Withdraw
   │              │
   └──────┬───────┘
          ▼
     🧾 HISTORY
          │
          ▼
     📈 INTEREST
          │
          ▼
      👥 CUSTOMERS
          │
          ▼
        🚪 EXIT
```

---

# 🧩 Functions

```text
account_creation()
        │
        ▼
account_display()
        │
        ▼
transaction_history()
        │
        ▼
account_search()
        │
        ▼
balance_check()
        │
        ▼
withdrawal()
        │
        ▼
account_status()
        │
        ▼
deposit_money()
        │
        ▼
calculate_interest()
        │
        ▼
customer_operations()
```

Each function is responsible for a specific banking operation, keeping the program organized and easier to understand.

---

# 🛠️ Technologies & Concepts

### 🐍 Technology

* Python 3.x
* VS Code / PyCharm / IDLE
* Console / Terminal

### 📚 Python Concepts

* Variables
* Strings
* Integers
* Floats
* Lists
* Dictionaries
* Sets
* Tuples
* Input / Output
* `if`, `elif`, `else`
* `while` loop
* `for` loop
* Functions
* Parameters
* Basic arithmetic
* Modules
* File handling
* `open()`
* `.read()`
* `.close()`

> 📌 No external Python libraries are required.

---

# 📂 Project Structure

```text
🏦 BankManagement/
│
├── 📄 main.py
│
├── 📝 accountCreation.py
├── 👤 accountDisplay.py
├── 🧾 transactionHistory.py
├── 🔍 accountSearch.py
├── 💰 balanceCheck.py
├── 💸 withdrawal.py
├── 🔐 accountStatus.py
├── 💵 depositMoney.py
├── 📈 calculateInterest.py
│
├── 👥 customerOperations.py
├── 📄 README.md
└── 📄 LICENSE
```

---

# 📋 Assignment Requirements

| Requirement                     | Status |
| ------------------------------- | :----: |
| 🔁 4 files using loops          |    ✅   |
| 🔀 3 files using if-else        |    ✅   |
| ⚙️ 3 files of choice            |    ✅   |
| 📋 List                         |    ✅   |
| 📖 Dictionary                   |    ✅   |
| 🔹 Set                          |    ✅   |
| 🔢 Tuple                        |    ✅   |
| 🧩 Multiple Python modules      |    ✅   |
| 📂 File handling using `open()` |    ✅   |
| ⌨️ User input                   |    ✅   |
| ⚙️ User-defined functions       |    ✅   |

---

# 🚀 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/techwithmanav/BankManagement.git
```

### 2️⃣ Open the project

```bash
cd BankManagement
```

### 3️⃣ Run the program

```bash
python main.py
```

---

# 🖥️ Terminal Preview

```text
╔══════════════════════════════════════════╗
║       🏦 PYTHON BANK MANAGEMENT          ║
╠══════════════════════════════════════════╣
║                                          ║
║          🏦 MAIN MENU                    ║
║                                          ║
║  1. 📝 Create New Account                ║
║  2. 👤 Account Details                   ║
║  3. 💰 Check Balance                    ║
║  4. 💵 Deposit Money                    ║
║  5. 💸 Withdraw Money                   ║
║  6. 🧾 Transaction History               ║
║  7. 🔐 Account Status                   ║
║  8. 🔍 Search Account                   ║
║  9. 📈 Calculate Interest               ║
║ 10. 👥 View All Customers               ║
║ 11. 🚪 Exit                             ║
║                                          ║
╚══════════════════════════════════════════╝

👉 Enter your choice: 1

====================================
       🏦📝 CREATE NEW ACCOUNT
====================================

👤 Enter your full name: Manav
📞 Enter your phone number: 9876543210
📧 Enter your email: manav@gmail.com
💰 Enter initial deposit: ₹5000

🏦 Account Created Successfully!
------------------------------------
💳 Your Account Number: 1001
------------------------------------
```

---

# 📚 Learning Outcomes

This project provides practical experience with:

* ✅ Python variables and data types
* ✅ User input and validation
* ✅ Conditional statements
* ✅ `for` and `while` loops
* ✅ Lists and dictionaries
* ✅ Sets and tuples
* ✅ User-defined functions
* ✅ Python modules
* ✅ File handling
* ✅ Basic banking calculations
* ✅ Real-world problem solving
* ✅ Console application design

---

# 💡 Why This Project?

### 🧠 Learn

```text
Variables
    +
Data Types
    +
Conditions
    +
Loops
    +
Lists
    +
Dictionaries
    +
Sets & Tuples
    +
Functions
```

### 🛠️ Build

```text
📝 Account Creation
       +
💰 Balance Management
       +
💵 Deposits
       +
💸 Withdrawals
       +
🧾 Transactions
       +
📈 Interest
       +
👥 Customer Management
```

### 🚀 Practice

```text
Problem Solving
      +
Program Flow
      +
User Interaction
      +
Data Handling
      +
Modular Programming
```

---

# 🚀 Future Roadmap

### 🟢 Phase 1 — Basic Improvements

* 🔐 PIN-based account security
* 🔄 Account-to-account transfers
* 🗑️ Account deletion
* 🧾 Detailed bank statements
* 📅 Transaction dates

### 🟡 Phase 2 — Data Storage

* 💾 File-based data storage
* 📄 JSON data storage
* 🗄️ SQLite database
* 🗃️ MySQL database

### 🔴 Phase 3 — Advanced Version

* 🖥️ Graphical User Interface
* 🌐 Web-based banking system
* 👨‍💼 Admin dashboard
* 🔐 Authentication system
* ☁️ Cloud data storage
* 📱 Mobile-friendly interface

---

# ⚠️ Current Limitation

The current version stores account information temporarily in:

```text
bank_data = {}
```

Therefore, account information is lost when the program is closed.

> 💡 Database or file-based storage can be added in future versions for permanent data storage.

---

# 🤝 Contributing

Contributions and improvements are welcome! 🎉

```bash
git clone https://github.com/techwithmanav/BankManagement.git
git checkout -b feature-name
git add .
git commit -m "Add new feature"
git push origin feature-name
```

Then create a Pull Request.

---

# 📄 License

This project is created for **learning and educational purposes**.

You are free to modify and improve the project for your own learning.

---

<div align="center">

## 🏦 Bank Account Management System

### Simple • Beginner-Friendly • Python-Based

<br>

🏦   💳   💰   🧾   📊

<br><br>

**Built with ❤️ using Python 🐍**

<br><br>

<img src="https://img.shields.io/badge/Made%20with-❤️%20%26%20🐍%20Python-3776AB?style=for-the-badge" />
<img src="https://img.shields.io/badge/Beginner--Friendly-2EA44F?style=for-the-badge" />

<br><br>

⭐ **Like this project? Give the repository a star!** ⭐

<br><br>

<a href="https://github.com/techwithmanav/BankManagement">
  <img src="https://img.shields.io/badge/⭐%20Visit%20Repository-FFD700?style=for-the-badge&logo=github&logoColor=black" />
</a>

<br><br>

**Learn → Build → Improve → Repeat 🚀**

<br>

<sub>Bank Account Management System • Python Mini Project</sub>

</div>
