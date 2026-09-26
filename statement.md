# Bank Management System — Project Statement

## 1. Problem Statement

Managing basic banking activities manually can be time-consuming and difficult to organize, especially when customer information, account balances, and transaction records need to be maintained consistently.

This project provides a simple **command-line Bank Management System** developed in Python to simulate essential customer banking operations in a structured and easy-to-use way.

The system allows a customer to create a bank account by providing basic personal information, a mobile number, an address, a four-digit PIN, and an initial deposit. After account creation, the system generates an account number and stores the account information locally.

Customers can then log in using their account number and PIN. After successful authentication, they can perform common banking operations such as checking their balance, depositing money, withdrawing money, transferring money to another account, viewing their transaction history, viewing account details, and changing their PIN.

The application uses a local JSON file named `bank_data.json` to store account information and transaction records. This allows account data to remain available when the program is closed and started again.

The project is intended as an educational and practical demonstration of how Python can be used to create a menu-driven application involving functions, dictionaries, lists, file handling, JSON storage, input validation, exception handling, and date/time recording.

This system is a **basic banking simulation for learning and demonstration purposes**. It is not intended to replace a real-world banking system because it does not implement production-level security, encryption, secure authentication, database management, or other infrastructure required for real financial applications.

---

# 2. Project Objective

The main objective of the Bank Management System is to create a simple console-based application that can organize and simulate common banking activities.

The project aims to:

- Provide a simple way to create customer accounts.
- Automatically generate account numbers.
- Allow customers to log in using an account number and PIN.
- Allow customers to check their current balance.
- Allow customers to deposit money.
- Allow customers to withdraw money when sufficient balance is available.
- Allow customers to transfer money between existing accounts.
- Maintain transaction records.
- Display a customer's mini statement.
- Display customer account details.
- Allow customers to change their PIN.
- Store account information persistently using a JSON file.
- Demonstrate basic validation and exception handling.
- Provide a simple menu-driven terminal interface.

---

# 3. Who Can Use This Project?

This project can be used by different types of users depending on their purpose.

## 3.1 Python Beginners

Python beginners can use this project to understand how several fundamental Python concepts work together in a complete application.

The project demonstrates:

- Variables
- Strings
- Numbers
- Dictionaries
- Lists
- Functions
- Loops
- Conditional statements
- Exception handling
- File handling
- JSON
- Date and time
- User input

---

## 3.2 Students

Students can use this project as a learning project or as a foundation for a Python-based academic project.

It can help students understand how to divide a larger problem into smaller functions and how different functions communicate through shared account data.

---

## 3.3 Students Learning File Handling

The project demonstrates how information can be saved to and loaded from a local file.

The application uses:

```text
bank_data.json
```

for persistent storage.

This makes the project useful for students learning:

- File reading
- File writing
- JSON serialization
- Persistent application data

---

## 3.4 Students Learning JSON

The project provides a practical example of storing structured information in JSON.

Customer information, account balances, PINs, and transactions are represented using dictionaries and lists and then stored in JSON format.

---

## 3.5 Students Learning Functions

Each major banking operation is implemented as a separate function.

Examples include:

- `create_account()`
- `login()`
- `check_balance()`
- `deposit_money()`
- `withdraw_money()`
- `transfer_money()`
- `mini_statement()`
- `account_details()`
- `change_pin()`

This makes the project useful for understanding function-based program organization.

---

## 3.6 Students Building Console Applications

Anyone learning how to create menu-driven command-line applications can use this project as an example.

The program contains both:

- A main application menu
- A customer banking menu

and uses user input to navigate between different operations.

---

## 3.7 Developers Building a Basic Prototype

A beginner developer can use the project as a starting point for developing a more advanced banking application.

The current structure can be extended with:

- Database support
- Better authentication
- Encryption
- Account management
- Administrative functionality
- Graphical interfaces
- Web interfaces
- Additional banking services

---

# 4. Main Features

## 4.1 New Account Creation

The system allows a new customer to create an account.

The customer provides:

- Name
- Mobile number
- Address
- Four-digit PIN
- Initial deposit

The application then generates an account number automatically.

The first account number is:

```text
1001
```

Subsequent account numbers are generated based on the highest existing account number.

---

## 4.2 Automatic Account Number Generation

The system automatically generates an account number instead of requiring the customer to enter one.

If no accounts exist, the first account number is:

```text
1001
```

If the existing account numbers are:

```text
1001
1002
1003
```

the next generated account number is:

```text
1004
```

This reduces the need for manual account-number assignment.

---

## 4.3 Four-Digit PIN Creation

During account creation, the customer must create a four-digit PIN.

The system checks that:

- The PIN contains exactly four characters.
- Every character is a digit.

For example:

```text
1234
```

is valid.

Inputs such as:

```text
123
12345
12A4
```

are rejected.

---

## 4.4 Initial Deposit

When creating an account, the customer can provide an initial deposit.

The system checks that:

- The amount is numeric.
- The amount is not negative.

A zero initial deposit is allowed by the current implementation.

The initial deposit becomes the account's starting balance.

---

## 4.5 Account Opening Transaction

When a new account is created, the initial deposit is also recorded as an:

```text
Account Opening
```

transaction.

The transaction stores:

- Transaction type
- Amount
- Date and time

This means the initial account activity becomes part of the customer's transaction history.

---

## 4.6 Customer Login

Customers can log in using:

- Account number
- PIN

The system first checks whether the account exists.

If the account exists, the entered PIN is compared with the stored PIN.

A successful login opens the customer banking menu.

---

## 4.7 Balance Checking

A logged-in customer can view their current balance.

The system displays:

- Account number
- Account holder name
- Available balance

The balance-checking operation does not modify account information.

---

## 4.8 Deposit Money

Customers can add money to their account.

The system:

1. Requests the deposit amount.
2. Converts the input into a numeric value.
3. Checks that the amount is greater than zero.
4. Adds the amount to the current balance.
5. Creates a deposit transaction.
6. Saves the updated account data.

The updated balance is displayed after the deposit.

---

## 4.9 Withdraw Money

Customers can withdraw money from their account.

The system checks:

- The amount is numeric.
- The amount is greater than zero.
- The amount does not exceed the available balance.

If all checks pass, the amount is deducted from the balance and a withdrawal transaction is recorded.

If the account does not have enough money, the system displays:

```text
Insufficient balance.
```

---

## 4.10 Money Transfer

Customers can transfer money to another existing account.

The system verifies:

1. The receiver account exists.
2. The receiver is not the same account as the sender.
3. The transfer amount is greater than zero.
4. The sender has sufficient balance.

When the transfer succeeds:

- Money is deducted from the sender.
- Money is added to the receiver.
- A transfer transaction is recorded for the sender.
- A received-money transaction is recorded for the receiver.
- The updated information is saved.

---

## 4.11 Transfer Transaction Records

A successful transfer creates records for both accounts.

For the sender, the transaction type is represented as:

```text
Transfer to <receiver account number>
```

For the receiver, it is represented as:

```text
Received from <sender account number>
```

Both records use the same transaction date and time generated during the transfer.

---

## 4.12 Mini Statement

Customers can view their stored transaction history through the mini statement feature.

For each transaction, the system displays:

- Type
- Amount
- Date

The current implementation displays all transactions stored for the account.

---

## 4.13 Account Details

Customers can view their account information.

The account-details feature displays:

- Account number
- Name
- Mobile number
- Address
- Current balance

The PIN is not displayed as part of the account details screen.

---

## 4.14 Change PIN

A logged-in customer can change their PIN.

The system first asks for the current PIN.

The current PIN must match the stored PIN.

The customer can then enter a new PIN.

The new PIN must:

- Contain exactly four characters.
- Contain only digits.

After successful validation, the new PIN is saved.

---

## 4.15 Persistent Data Storage

The application stores account data in:

```text
bank_data.json
```

The program loads this file when it starts.

When account information changes, the program saves the updated information back to the JSON file.

This allows account information and transaction history to persist between program runs.

---

## 4.16 Transaction Date and Time

Transactions include the date and time when they occur.

The program generates timestamps using the current date and time.

The format is:

```text
DD-MM-YYYY HH:MM:SS
```

For example:

```text
26-09-2026 20:30:15
```

---

## 4.17 Input Validation

The program performs validation for important operations.

Examples include:

### PIN

The PIN must contain exactly four digits.

### Initial Deposit

The initial deposit cannot be negative.

### Deposit

The deposit amount must be greater than zero.

### Withdrawal

The withdrawal amount must be greater than zero and cannot exceed the available balance.

### Transfer

The receiver must exist, the receiver cannot be the sender, the amount must be greater than zero, and the sender must have enough balance.

---

## 4.18 Exception Handling

The program uses `try`/`except` blocks for monetary input.

If the user enters an invalid value that cannot be converted to a number, the program catches the `ValueError` and displays:

```text
Please enter a valid amount.
```

This prevents invalid numeric input from immediately terminating the application.

---

## 4.19 Menu-Driven Interface

The project provides a simple terminal-based interface.

The main menu contains:

```text
1. Create New Account
2. Customer Login
3. Exit
```

After login, the customer menu contains:

```text
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Mini Statement
6. Account Details
7. Change PIN
8. Logout
```

---

# 5. Main Banking Operations

The project provides the following primary banking operations:

| Feature | Description |
|---|---|
| Account Creation | Creates a new customer account |
| Account Number Generation | Automatically assigns an account number |
| Customer Login | Authenticates the customer using account number and PIN |
| Balance Check | Displays the current account balance |
| Deposit | Adds money to the account |
| Withdrawal | Removes money when sufficient balance is available |
| Transfer | Transfers money between two existing accounts |
| Mini Statement | Displays stored transaction history |
| Account Details | Displays customer and account information |
| PIN Change | Allows the customer to update the PIN |
| Logout | Ends the current customer session |
| JSON Storage | Saves account information locally |
| Transaction Recording | Records account activity with date and time |

---

# 6. Type of Application

This project is a:

- Command-line application
- Menu-driven application
- Customer banking simulation
- File-based data management application
- Python educational project

It does not use a graphical user interface or web interface.

---

# 7. Data Managed by the System

The system manages the following customer and account information:

### Customer Information

- Name
- Mobile number
- Address

### Authentication Information

- Four-digit PIN

### Account Information

- Account number
- Balance

### Transaction Information

- Transaction type
- Transaction amount
- Transaction date and time

---

# 8. Expected User Experience

A normal user experience follows this process:

```text
Start Program
      |
      v
Main Menu
      |
      +------------------------+
      |                        |
      v                        v
Create Account            Customer Login
      |                        |
      v                        v
Enter Details             Verify Credentials
      |                        |
      v                        v
Account Created           Customer Menu
                               |
                +--------------+--------------+
                |      |       |      |       |
                v      v       v      v       v
             Balance Deposit Withdraw Transfer Statement
                |
                +-------------+
                |
                v
          Account Details
                |
                v
            Change PIN
                |
                v
             Logout
                |
                v
           Main Menu
```

---

# 9. Project Scope

The current project focuses on basic customer banking operations.

The scope includes:

- Customer account creation
- Customer authentication
- Account balance management
- Basic money transactions
- Transaction history
- Customer account information
- PIN management
- Local data persistence

The project does not currently include advanced banking infrastructure such as:

- Real bank integration
- Online payments
- Card processing
- Internet banking
- OTP services
- Bank APIs
- Administrative banking systems
- Secure production databases

---

# 10. Educational Value

This project is useful because it combines several programming concepts into one practical application.

A learner can study how:

```text
User Input
     |
     v
Validation
     |
     v
Business Logic
     |
     v
Data Structure
     |
     v
Transaction Record
     |
     v
Persistent Storage
     |
     v
User Feedback
```

works as a complete application flow.

The project therefore provides practical experience beyond isolated Python exercises.

---

# 11. Project Limitations

The system is intended for learning and demonstration rather than real-world banking.

Important limitations include:

- PINs are stored in the JSON file in plain form.
- The application does not encrypt sensitive information.
- There is no advanced authentication system.
- There is no OTP or two-factor authentication.
- There is no account lockout system.
- There is no database server.
- There is no administrator module.
- There is no account deletion feature.
- There is no loan-management feature.
- There is no interest calculation.
- There is no ATM or card management.
- There is no online banking connection.
- The application does not provide production-level financial security.

These limitations should be considered before using the project for anything beyond education, demonstration, or prototyping.

---

# 12. Possible Future Expansion

The current project can be expanded into a more advanced system by adding:

## Security

- PIN hashing
- Encryption
- OTP verification
- Two-factor authentication
- Login attempt limits
- Account lockout

## Database

- SQLite
- MySQL
- PostgreSQL

## Account Management

- Account deletion
- Account blocking
- Profile editing
- Account types

## Banking Services

- Interest calculation
- Loans
- Fixed deposits
- Recurring deposits
- Bill payments
- Beneficiary management

## Transaction Management

- Transaction IDs
- Transaction search
- Transaction filtering
- Date-range statements
- Receipts
- Downloadable statements

## Interface

- Desktop GUI
- Web application
- Mobile application

---

# 13. Short Problem Statement

### Problem

Basic banking activities such as creating accounts, maintaining balances, recording transactions, and transferring money require organized data management. A simple educational system is needed to demonstrate how these operations can be handled through a computer program.

### Proposed Solution

The Bank Management System provides a Python-based command-line solution where customers can create accounts, log in, manage balances, transfer money, view transaction history, view account information, and change their PIN. Account and transaction information is stored locally in a JSON file for persistence.

---

# 14. One-Line Project Description

> **A Python-based command-line Bank Management System that allows customers to create accounts, authenticate themselves, manage balances, transfer money, view transactions, and maintain account information using local JSON storage.**

---

# 15. Final Summary

The Bank Management System is designed to provide a simple and understandable simulation of common customer banking activities.

Its main purpose is to demonstrate how a Python program can:

- Create and manage accounts.
- Authenticate users.
- Maintain balances.
- Process deposits.
- Process withdrawals.
- Transfer money between accounts.
- Record transactions.
- Display account information.
- Change customer PINs.
- Persist information using JSON.

The project is particularly suitable for **Python learners, students, beginners, and developers practicing console-based application development**.

It provides a foundation that can later be expanded into a more advanced system with stronger security, database integration, additional banking services, and a graphical or web interface.
