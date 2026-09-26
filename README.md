# Bank Management System

A simple **command-line Bank Management System** written in Python. The program allows customers to create bank accounts, log in using an account number and 4-digit PIN, manage their balance, transfer money, view transaction history, inspect account details, and change their PIN.

The application stores account information and transaction records locally in a JSON file named `bank_data.json`, so data can remain available after the program is closed and started again.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Purpose of the Project](#purpose-of-the-project)
3. [Who Can Use This Project](#who-can-use-this-project)
4. [Main Features](#main-features)
5. [Technologies Used](#technologies-used)
6. [Python Modules Used](#python-modules-used)
7. [Project Structure](#project-structure)
8. [Data Storage](#data-storage)
9. [Account Data Structure](#account-data-structure)
10. [Transaction Data Structure](#transaction-data-structure)
11. [Program Initialization](#program-initialization)
12. [Detailed Function Documentation](#detailed-function-documentation)
13. [Application Workflow](#application-workflow)
14. [Main Menu](#main-menu)
15. [Creating a New Account](#creating-a-new-account)
16. [Customer Login](#customer-login)
17. [Checking Balance](#checking-balance)
18. [Depositing Money](#depositing-money)
19. [Withdrawing Money](#withdrawing-money)
20. [Transferring Money](#transferring-money)
21. [Mini Statement](#mini-statement)
22. [Account Details](#account-details)
23. [Changing the PIN](#changing-the-pin)
24. [Logout](#logout)
25. [Exit](#exit)
26. [Input Validation](#input-validation)
27. [Transaction Recording](#transaction-recording)
28. [Account Number Generation](#account-number-generation)
29. [How Data Is Saved](#how-data-is-saved)
30. [How to Run the Project](#how-to-run-the-project)
31. [Example User Flow](#example-user-flow)
32. [Example JSON Data](#example-json-data)
33. [Error and Validation Messages](#error-and-validation-messages)
34. [Important Implementation Details](#important-implementation-details)
35. [Limitations](#limitations)
36. [Security Considerations](#security-considerations)
37. [Possible Future Improvements](#possible-future-improvements)
38. [Summary of Functions](#summary-of-functions)
39. [Conclusion](#conclusion)

---

## Project Overview

This project is a **menu-driven banking application** implemented in Python.

The program uses:

- Python functions for organizing operations.
- `input()` for user interaction.
- A Python dictionary for maintaining accounts while the program is running.
- JSON for persistent local storage.
- `datetime` for recording transaction timestamps.
- Basic validation to prevent invalid deposits, withdrawals, transfers, and PINs.

The system is designed around two major menus:

### Main Menu

The main menu provides:

1. Create New Account
2. Customer Login
3. Exit

### Customer Banking Menu

After successful login, the customer can:

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. View Mini Statement
6. View Account Details
7. Change PIN
8. Logout

---

## Purpose of the Project

The purpose of this project is to demonstrate how a basic banking application can be implemented using core Python concepts.

It demonstrates:

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
- JSON serialization
- Date and time handling
- User input validation
- Menu-driven programming
- Persistent data storage

This is suitable as a learning project for understanding how multiple Python concepts can be combined into a complete console application.

---

## Who Can Use This Project

This project can be useful for:

- Python beginners
- Students learning programming
- Students learning file handling
- Students learning JSON
- Students practicing functions
- Students building console-based projects
- Beginners learning CRUD-style application logic
- Anyone wanting a simple example of a local banking simulation

It can also serve as a foundation for a larger banking application, although it should **not be treated as production banking software**.

---

## Main Features

### 1. Create New Account

A user can create an account by providing:

- Customer name
- Mobile number
- Address
- A 4-digit PIN
- Initial deposit

The program automatically generates the account number.

---

### 2. Customer Login

Customers log in using:

- Account number
- PIN

The system checks whether the account exists and whether the entered PIN matches the stored PIN.

---

### 3. Check Balance

A logged-in customer can view:

- Account number
- Account holder name
- Current balance

---

### 4. Deposit Money

Customers can deposit money into their account.

The program:

1. Reads the amount.
2. Checks that it is greater than zero.
3. Adds it to the account balance.
4. Records the transaction.
5. Saves the updated data.

---

### 5. Withdraw Money

Customers can withdraw money if:

- The entered amount is greater than zero.
- The account has enough balance.

The balance is reduced and a withdrawal transaction is recorded.

---

### 6. Transfer Money

A customer can transfer money to another existing account.

The program verifies:

- Receiver account exists.
- Receiver is not the same as the sender.
- Transfer amount is greater than zero.
- Sender has sufficient balance.

Both accounts receive a transaction record.

---

### 7. Mini Statement

Customers can view all transaction records stored for their account.

Each transaction displays:

- Transaction type
- Amount
- Date and time

---

### 8. Account Details

The customer can view:

- Account number
- Name
- Mobile number
- Address
- Current balance

---

### 9. Change PIN

A customer can change their PIN after entering the current PIN.

The new PIN must contain exactly four digits.

---

### 10. Persistent JSON Storage

The program stores account data in:

```text
bank_data.json
```

This means account information can be loaded when the application starts again.

---

# Technologies Used

## Programming Language

**Python**

The source program uses standard Python functionality and does not require third-party packages.

## Data Storage

**JSON**

The application uses JSON to store:

- Customer information
- PINs
- Account balances
- Transaction history

## Interface

**Command-line / terminal interface**

The application runs entirely in a terminal or command prompt.

---

# Python Modules Used

The program imports three standard-library modules.

## 1. `json`

```python
import json
```

The `json` module is used to read and write account data.

It is used in:

- `load_data()`
- `save_data()`

`json.load()` converts JSON data from the file into Python objects.

`json.dump()` converts Python data into JSON and writes it to the file.

---

## 2. `os`

```python
import os
```

The `os` module is used to check whether the data file exists.

The program uses:

```python
os.path.exists(FILE_NAME)
```

This prevents the application from trying to open a file that does not yet exist.

---

## 3. `datetime`

```python
from datetime import datetime
```

The `datetime` class is used to record transaction dates and times.

The program formats timestamps using:

```python
datetime.now().strftime("%d-%m-%Y %H:%M:%S")
```

The resulting format is:

```text
day-month-year hour:minute:second
```

For example:

```text
26-09-2026 20:15:30
```

---

# Project Structure

The main source file contains the complete application.

A typical project directory will look like:

```text
Bank-Management-System/
│
├── code3.py
├── bank_data.json
└── README.md
```

### `code3.py`

Contains all Python logic for the banking system.

### `bank_data.json`

Contains saved account information.

This file is created when account data is first saved if it does not already exist.

### `README.md`

Contains documentation for the project.

---

# Data Storage

The program defines:

```python
FILE_NAME = "bank_data.json"
```

Therefore, the application expects the account database to be stored in a file named:

```text
bank_data.json
```

The program does not use an external database such as MySQL, PostgreSQL, MongoDB, or SQLite.

Instead, it uses a local JSON file.

---

# Account Data Structure

The global `accounts` variable contains the data loaded from `bank_data.json`.

Conceptually, the structure is:

```python
accounts = {
    "1001": {
        "name": "Customer Name",
        "mobile": "9876543210",
        "address": "Customer Address",
        "pin": "1234",
        "balance": 5000.0,
        "transactions": []
    }
}
```

The account number is used as the dictionary key.

For example:

```text
"1001"
```

The value associated with that key is another dictionary containing the customer's information.

---

## Account Fields

### `name`

Stores the customer's name.

Example:

```json
"name": "Rahul"
```

---

### `mobile`

Stores the mobile number entered by the customer.

Example:

```json
"mobile": "9876543210"
```

The current implementation stores it as entered and does not perform detailed mobile-number validation.

---

### `address`

Stores the customer's address.

Example:

```json
"address": "Bhopal, Madhya Pradesh"
```

---

### `pin`

Stores the customer's four-digit PIN.

Example:

```json
"pin": "1234"
```

The program compares this value during login and PIN changes.

---

### `balance`

Stores the customer's current balance.

Example:

```json
"balance": 5000.0
```

The value is treated as a numeric amount.

---

### `transactions`

Stores a list of transaction dictionaries.

Example:

```json
"transactions": [
    {
        "type": "Account Opening",
        "amount": 5000.0,
        "date": "26-09-2026 20:15:30"
    }
]
```

---

# Transaction Data Structure

Every transaction is stored as a dictionary containing three main fields.

## `type`

Describes the transaction.

Possible values generated by the current program include:

```text
Account Opening
Deposit
Withdrawal
Transfer to <account number>
Received from <account number>
```

---

## `amount`

Stores the transaction amount.

Example:

```json
"amount": 1000.0
```

---

## `date`

Stores the date and time when the transaction was created.

Example:

```json
"date": "26-09-2026 20:30:15"
```

---

# Detailed Function Documentation

The source program is organized into multiple functions.

---

# `load_data()`

## Purpose

Loads existing account data from `bank_data.json`.

## Logic

The function first checks:

```python
if os.path.exists(FILE_NAME):
```

If the file exists, it opens it in read mode:

```python
with open(FILE_NAME, "r") as file:
```

Then it loads the JSON:

```python
return json.load(file)
```

If the file does not exist, it returns:

```python
{}
```

This creates an empty account collection.

## Why this is important

Without this function, previously saved accounts would not be available after restarting the program.

---

# `save_data()`

## Purpose

Saves the current `accounts` dictionary into `bank_data.json`.

The function opens the file in write mode:

```python
with open(FILE_NAME, "w") as file:
```

Then writes the account data:

```python
json.dump(accounts, file, indent=4)
```

## `indent=4`

The `indent=4` argument makes the JSON file easier for humans to read.

---

# `generate_account_number()`

## Purpose

Generates a new account number.

## Logic

If there are no accounts:

```python
if not accounts:
    return "1001"
```

Therefore, the first account number is:

```text
1001
```

If accounts already exist, their keys are converted to integers:

```python
numbers = [int(acc) for acc in accounts.keys()]
```

The maximum account number is found:

```python
max(numbers)
```

Then one is added:

```python
max(numbers) + 1
```

Finally, it is converted back to a string:

```python
return str(max(numbers) + 1)
```

## Example

If existing accounts are:

```text
1001
1002
1003
```

the next account number will be:

```text
1004
```

---

# `create_account()`

## Purpose

Creates a new customer account.

## Step 1: Display heading

The function prints:

```text
========== CREATE ACCOUNT ==========
```

---

## Step 2: Collect customer information

The program asks for:

```python
name = input("Enter customer name: ")
mobile = input("Enter mobile number: ")
address = input("Enter address: ")
```

The entered values are stored in variables.

---

## Step 3: Validate the PIN

The program repeatedly asks:

```text
Create a 4-digit PIN:
```

The validation condition is:

```python
len(pin) == 4 and pin.isdigit()
```

The PIN is accepted only if:

- Its length is exactly 4.
- Every character is a digit.

Otherwise, the program displays:

```text
PIN must contain exactly 4 digits.
```

---

## Step 4: Validate the initial deposit

The program attempts to convert the entered amount to a floating-point number:

```python
deposit = float(input("Enter initial deposit: ₹"))
```

If the amount is negative:

```python
if deposit >= 0:
```

the program rejects it and displays:

```text
Deposit cannot be negative.
```

If the input cannot be converted to a number, `ValueError` is caught and the program displays:

```text
Please enter a valid amount.
```

The initial deposit can therefore be zero or greater.

---

## Step 5: Generate account number

The function calls:

```python
account_number = generate_account_number()
```

---

## Step 6: Create account record

The program creates an account dictionary containing:

```python
{
    "name": name,
    "mobile": mobile,
    "address": address,
    "pin": pin,
    "balance": deposit,
    "transactions": []
}
```

---

## Step 7: Record account opening transaction

The program immediately adds an initial transaction:

```python
{
    "type": "Account Opening",
    "amount": deposit,
    "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
}
```

This means the initial deposit is recorded in the transaction history.

---

## Step 8: Save data

The function calls:

```python
save_data()
```

so the account is persisted to disk.

---

## Step 9: Display result

The program prints:

```text
Account created successfully!
Your Account Number is: <account number>
```

---

# `login()`

## Purpose

Authenticates a customer using account number and PIN.

## Input

The user enters:

```text
Enter account number:
Enter PIN:
```

## Account verification

The program checks:

```python
if account_number in accounts:
```

If the account does not exist:

```text
Account not found.
```

If the account exists, the PIN is compared:

```python
if accounts[account_number]["pin"] == pin:
```

If correct:

```text
Login successful!
Welcome, <name>
```

Then the customer menu is opened:

```python
customer_menu(account_number)
```

If the PIN is incorrect:

```text
Incorrect PIN.
```

---

# `check_balance(account_number)`

## Purpose

Displays the customer's current balance.

The function retrieves:

```python
balance = accounts[account_number]["balance"]
```

Then displays:

- Account number
- Account holder
- Available balance

This function does not change any account data.

---

# `deposit_money(account_number)`

## Purpose

Adds money to the customer's account.

## Step 1: Read amount

The amount is converted to a floating-point number:

```python
amount = float(input("Enter amount to deposit: ₹"))
```

---

## Step 2: Validate amount

The amount must be greater than zero.

If:

```python
amount <= 0
```

the program displays:

```text
Amount must be greater than zero.
```

and returns without changing the account.

---

## Step 3: Update balance

The amount is added:

```python
accounts[account_number]["balance"] += amount
```

---

## Step 4: Record transaction

A transaction is appended:

```python
{
    "type": "Deposit",
    "amount": amount,
    "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
}
```

---

## Step 5: Save data

The updated account information is written to the JSON file.

---

## Step 6: Display result

The program displays:

```text
₹ <amount> deposited successfully.
New Balance: ₹ <new balance>
```

---

# `withdraw_money(account_number)`

## Purpose

Withdraws money from the customer's account.

## Step 1: Read amount

The program asks:

```text
Enter amount to withdraw: ₹
```

The value is converted to `float`.

---

## Step 2: Validate positive amount

If the amount is zero or negative, the program displays:

```text
Amount must be greater than zero.
```

---

## Step 3: Check available balance

The program checks:

```python
if amount > accounts[account_number]["balance"]:
```

If the requested withdrawal is greater than the balance:

```text
Insufficient balance.
```

No money is removed.

---

## Step 4: Update balance

For a valid withdrawal:

```python
accounts[account_number]["balance"] -= amount
```

---

## Step 5: Record transaction

The transaction is stored as:

```python
{
    "type": "Withdrawal",
    "amount": amount,
    "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
}
```

---

## Step 6: Save data

The updated information is saved.

---

# `transfer_money(account_number)`

## Purpose

Transfers money from the logged-in customer's account to another account.

## Step 1: Enter receiver

The program asks:

```text
Enter receiver account number:
```

---

## Step 2: Verify receiver

The program checks:

```python
if receiver not in accounts:
```

If the receiver does not exist:

```text
Receiver account not found.
```

---

## Step 3: Prevent self-transfer

The program checks:

```python
if receiver == account_number:
```

If true:

```text
You cannot transfer money to your own account.
```

---

## Step 4: Read transfer amount

The user enters the amount.

The amount must be greater than zero.

---

## Step 5: Check sender balance

The program checks whether the sender has enough balance.

If not:

```text
Insufficient balance.
```

---

## Step 6: Update both balances

The sender's balance is decreased:

```python
accounts[account_number]["balance"] -= amount
```

The receiver's balance is increased:

```python
accounts[receiver]["balance"] += amount
```

---

## Step 7: Generate a shared timestamp

The function creates:

```python
date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
```

The same timestamp is used for both transaction records.

---

## Step 8: Record sender transaction

The sender receives:

```python
{
    "type": "Transfer to " + receiver,
    "amount": amount,
    "date": date
}
```

For example:

```text
Transfer to 1002
```

---

## Step 9: Record receiver transaction

The receiver receives:

```python
{
    "type": "Received from " + account_number,
    "amount": amount,
    "date": date
}
```

For example:

```text
Received from 1001
```

---

## Step 10: Save data

Both account changes are saved using:

```python
save_data()
```

---

# `mini_statement(account_number)`

## Purpose

Displays the customer's complete stored transaction history.

The function gets:

```python
transactions = accounts[account_number]["transactions"]
```

If the list is empty:

```text
No transactions found.
```

Otherwise, it loops through every transaction:

```python
for transaction in transactions:
```

and displays:

```text
--------------------------------
Type: <transaction type>
Amount: ₹ <amount>
Date: <date>
```

The current implementation displays all stored transactions rather than limiting the output to a fixed number.

---

# `account_details(account_number)`

## Purpose

Displays detailed customer account information.

It retrieves the account dictionary:

```python
account = accounts[account_number]
```

Then displays:

- Account number
- Name
- Mobile
- Address
- Balance

---

# `change_pin(account_number)`

## Purpose

Allows a logged-in customer to change their PIN.

## Step 1: Verify current PIN

The user enters:

```text
Enter current PIN:
```

The entered PIN is compared with the stored PIN.

If it does not match:

```text
Incorrect current PIN.
```

The function returns.

---

## Step 2: Enter new PIN

The program repeatedly asks:

```text
Enter new 4-digit PIN:
```

The new PIN must satisfy:

```python
len(new_pin) == 4 and new_pin.isdigit()
```

If not:

```text
PIN must contain exactly 4 digits.
```

---

## Step 3: Update PIN

The account's PIN is replaced:

```python
accounts[account_number]["pin"] = new_pin
```

---

## Step 4: Save data

The new PIN is persisted using:

```python
save_data()
```

---

## Step 5: Display result

The program displays:

```text
PIN changed successfully!
```

---

# `customer_menu(account_number)`

## Purpose

Provides the authenticated customer with all banking operations.

The function uses:

```python
while True:
```

so the customer remains inside the banking menu until choosing logout.

The available choices are:

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

## Choice 1

Calls:

```python
check_balance(account_number)
```

---

## Choice 2

Calls:

```python
deposit_money(account_number)
```

---

## Choice 3

Calls:

```python
withdraw_money(account_number)
```

---

## Choice 4

Calls:

```python
transfer_money(account_number)
```

---

## Choice 5

Calls:

```python
mini_statement(account_number)
```

---

## Choice 6

Calls:

```python
account_details(account_number)
```

---

## Choice 7

Calls:

```python
change_pin(account_number)
```

---

## Choice 8

Displays:

```text
Logged out successfully.
```

and exits the customer menu using `break`.

---

## Invalid Choice

For any other input:

```text
Invalid choice. Please try again.
```

---

# `main()`

## Purpose

Controls the application's main menu.

It uses an infinite loop:

```python
while True:
```

The menu contains:

```text
1. Create New Account
2. Customer Login
3. Exit
```

---

## Choice 1

Calls:

```python
create_account()
```

---

## Choice 2

Calls:

```python
login()
```

---

## Choice 3

Displays:

```text
Thank you for using our Bank Management System!
```

and exits the loop using `break`.

---

## Invalid Choice

Any other input produces:

```text
Invalid choice. Please try again.
```

---

# Application Workflow

The complete application flow is:

```text
Program Starts
      |
      v
Load bank_data.json
      |
      v
Display Main Menu
      |
      +--------------------------+
      |                          |
      v                          v
Create Account               Customer Login
      |                          |
      v                          v
Save Account                 Verify Account
                                 |
                                 v
                          Customer Menu
                                 |
              +------------------+------------------+
              |        |         |        |         |
              v        v         v        v         v
           Balance  Deposit  Withdraw  Transfer  Statement
              |
              +------------------+------------------+
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

# Main Menu

When the program starts, it displays:

```text
==========================================
        BANK MANAGEMENT SYSTEM
==========================================
1. Create New Account
2. Customer Login
3. Exit
==========================================
```

The user enters a choice.

---

# Creating a New Account

A new customer follows this sequence:

```text
Create New Account
        |
        v
Enter customer name
        |
        v
Enter mobile number
        |
        v
Enter address
        |
        v
Create 4-digit PIN
        |
        v
Enter initial deposit
        |
        v
Generate account number
        |
        v
Create account record
        |
        v
Record Account Opening transaction
        |
        v
Save to bank_data.json
        |
        v
Display account number
```

The account number should be kept by the customer because it is required for login.

---

# Customer Login

Login follows:

```text
Enter account number
        |
        v
Check account exists
        |
        +---- No ----> Account not found
        |
       Yes
        |
        v
Enter PIN
        |
        v
Compare with stored PIN
        |
        +---- Wrong ----> Incorrect PIN
        |
       Correct
        |
        v
Customer Banking Menu
```

---

# Checking Balance

The balance operation reads the current balance from the logged-in customer's account and displays it.

It does not modify the balance.

---

# Depositing Money

The deposit operation follows:

```text
Enter amount
     |
     v
Convert to float
     |
     v
Is amount > 0?
     |
  No +----> Reject
     |
    Yes
     |
     v
Increase balance
     |
     v
Add transaction
     |
     v
Save JSON
```

---

# Withdrawing Money

The withdrawal operation follows:

```text
Enter amount
     |
     v
Convert to float
     |
     v
Is amount > 0?
     |
  No +----> Reject
     |
    Yes
     |
     v
Is balance sufficient?
     |
  No +----> Insufficient balance
     |
    Yes
     |
     v
Decrease balance
     |
     v
Add transaction
     |
     v
Save JSON
```

---

# Transferring Money

The transfer operation follows:

```text
Enter receiver account
          |
          v
Does receiver exist?
          |
       No +----> Reject
          |
         Yes
          |
          v
Is receiver the sender?
          |
        Yes +----> Reject
          |
          No
          |
          v
Enter amount
          |
          v
Is amount > 0?
          |
        No +----> Reject
          |
         Yes
          |
          v
Is sender balance sufficient?
          |
        No +----> Reject
          |
         Yes
          |
          v
Subtract from sender
          |
          v
Add to receiver
          |
          v
Record both transactions
          |
          v
Save JSON
```

---

# Mini Statement

The mini statement reads the `transactions` list associated with the account.

For every transaction it prints:

```text
Type
Amount
Date
```

The transaction history is stored in the order in which transactions are appended.

---

# Account Details

Account details provide a summary of the account.

The current implementation displays:

```text
Account Number
Name
Mobile
Address
Balance
```

The PIN is not printed in the account-details display.

---

# Changing the PIN

The PIN change flow is:

```text
Enter current PIN
       |
       v
Is current PIN correct?
       |
     No +----> Reject
       |
      Yes
       |
       v
Enter new PIN
       |
       v
Is it exactly 4 digits?
       |
     No +----> Ask again
       |
      Yes
       |
       v
Update PIN
       |
       v
Save JSON
```

---

# Logout

Selecting option `8` in the customer menu ends the current authenticated session.

The program displays:

```text
Logged out successfully.
```

The user then returns to the main menu.

---

# Exit

Selecting option `3` from the main menu ends the program.

The program displays:

```text
Thank you for using our Bank Management System!
```

---

# Input Validation

The application contains several validation checks.

## PIN Validation

A PIN must:

- Contain exactly four characters.
- Contain only digits.

Examples accepted:

```text
1234
0000
9876
```

Examples rejected:

```text
123
12345
12a4
abcd
```

---

## Initial Deposit Validation

During account creation:

- Zero is allowed.
- Positive values are allowed.
- Negative values are rejected.
- Non-numeric input is rejected.

---

## Deposit Validation

For normal deposits:

- Amount must be greater than zero.
- Invalid numeric input is caught.

---

## Withdrawal Validation

For withdrawals:

- Amount must be greater than zero.
- Amount cannot exceed current balance.
- Invalid numeric input is caught.

---

## Transfer Validation

For transfers:

- Receiver account must exist.
- Sender cannot transfer to themselves.
- Amount must be greater than zero.
- Sender must have sufficient balance.
- Invalid numeric input is caught.

---

## Login Validation

Login verifies:

1. Account number exists.
2. PIN matches the stored PIN.

---

# Transaction Recording

The program records transactions whenever account money changes.

## Account Opening

When an account is created, an `Account Opening` transaction is added.

---

## Deposit

A `Deposit` transaction is added.

---

## Withdrawal

A `Withdrawal` transaction is added.

---

## Transfer

Two transaction records are generated:

### Sender

```text
Transfer to <receiver account>
```

### Receiver

```text
Received from <sender account>
```

Both use the same generated timestamp.

---

# Account Number Generation

Account numbers begin at:

```text
1001
```

The function finds the largest existing account number and adds one.

For example:

```text
Existing:
1001
1002
1003

New:
1004
```

The account number is stored as a string key in the dictionary.

---

# How Data Is Saved

The program saves data through:

```python
json.dump(accounts, file, indent=4)
```

This converts the Python dictionary into JSON.

For example, Python data such as:

```python
{
    "1001": {
        "name": "Amit",
        "balance": 5000.0
    }
}
```

is stored in JSON-compatible form.

The application calls `save_data()` after operations that modify persistent information, including:

- Account creation
- Deposit
- Withdrawal
- Transfer
- PIN change

---

# How to Run the Project

## Step 1: Install Python

Install Python 3 on your computer.

You can verify the installation with:

```bash
python --version
```

or:

```bash
python3 --version
```

depending on your operating system.

---

## Step 2: Place the Python File in a Folder

For example:

```text
Bank-Management-System/
└── code3.py
```

---

## Step 3: Open Terminal

Open Command Prompt, PowerShell, Terminal, or another terminal application.

Navigate to the project directory.

Example:

```bash
cd path/to/Bank-Management-System
```

---

## Step 4: Run the Program

Run:

```bash
python code3.py
```

If your system uses `python3`:

```bash
python3 code3.py
```

---

## Step 5: Use the Menu

The program will show:

```text
BANK MANAGEMENT SYSTEM

1. Create New Account
2. Customer Login
3. Exit
```

Choose an option by entering its number.

---

# Example User Flow

A typical session may look like this:

```text
BANK MANAGEMENT SYSTEM

1. Create New Account
2. Customer Login
3. Exit

Enter your choice: 1
```

The program asks for:

```text
Enter customer name: Rahul
Enter mobile number: 9876543210
Enter address: Bhopal
Create a 4-digit PIN: 1234
Enter initial deposit: ₹5000
```

The program creates an account, for example:

```text
Account created successfully!
Your Account Number is: 1001
```

The customer can then return to the main menu and choose:

```text
2. Customer Login
```

After entering:

```text
Account number: 1001
PIN: 1234
```

the customer reaches the banking menu.

They can then:

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

# Example JSON Data

After creating an account, the JSON file will conceptually contain data similar to:

```json
{
    "1001": {
        "name": "Rahul",
        "mobile": "9876543210",
        "address": "Bhopal",
        "pin": "1234",
        "balance": 5000.0,
        "transactions": [
            {
                "type": "Account Opening",
                "amount": 5000.0,
                "date": "26-09-2026 20:15:30"
            }
        ]
    }
}
```

After a deposit, another transaction is added:

```json
{
    "type": "Deposit",
    "amount": 1000.0,
    "date": "26-09-2026 20:20:00"
}
```

The balance would become:

```text
6000.0
```

---

# Example Transfer Data

Suppose account `1001` transfers ₹500 to account `1002`.

The sender's transaction history receives:

```json
{
    "type": "Transfer to 1002",
    "amount": 500.0,
    "date": "26-09-2026 20:30:00"
}
```

The receiver's history receives:

```json
{
    "type": "Received from 1001",
    "amount": 500.0,
    "date": "26-09-2026 20:30:00"
}
```

At the same time:

```text
Sender balance = Sender balance - 500
Receiver balance = Receiver balance + 500
```

---

# Error and Validation Messages

The current program contains the following important user-facing messages.

## PIN

```text
PIN must contain exactly 4 digits.
```

## Negative Initial Deposit

```text
Deposit cannot be negative.
```

## Invalid Amount

```text
Please enter a valid amount.
```

## Account Not Found

```text
Account not found.
```

## Incorrect PIN

```text
Incorrect PIN.
```

## Invalid Deposit/Withdrawal/Transfer Amount

```text
Amount must be greater than zero.
```

## Insufficient Balance

```text
Insufficient balance.
```

## Receiver Not Found

```text
Receiver account not found.
```

## Self Transfer

```text
You cannot transfer money to your own account.
```

## Incorrect Current PIN

```text
Incorrect current PIN.
```

## Invalid Menu Choice

```text
Invalid choice. Please try again.
```

---

# Important Implementation Details

## 1. Accounts Are Stored Globally

The program eventually initializes:

```python
accounts = load_data()
```

This makes the loaded account dictionary available to the functions.

Functions such as:

- `save_data()`
- `generate_account_number()`
- `create_account()`
- `login()`
- `deposit_money()`
- `withdraw_money()`
- `transfer_money()`

use the shared `accounts` data.

---

## 2. The JSON File Is Loaded Before the Main Menu

At the bottom of the program:

```python
accounts = load_data()
main()
```

The sequence is therefore:

```text
Load saved data
      |
      v
Start main menu
```

---

## 3. The Program Uses Functions for Separation of Responsibilities

Each major operation has its own function.

This makes the program easier to understand than putting the entire application inside one large block.

---

## 4. Customer Menu Receives the Account Number

After successful login:

```python
customer_menu(account_number)
```

The account number is passed to banking functions.

For example:

```python
check_balance(account_number)
```

This allows the application to know which account should be modified or displayed.

---

## 5. The Program Uses Exception Handling for Numeric Input

Operations involving amounts use `try`/`except ValueError`.

This prevents the program from immediately crashing when a user enters something that cannot be converted to a number.

For example:

```text
abc
```

instead of:

```text
1000
```

produces:

```text
Please enter a valid amount.
```

---

## 6. Transaction Dates Are Generated at Operation Time

The program calls:

```python
datetime.now()
```

when creating transaction records.

Therefore, each transaction receives a timestamp corresponding to the time the operation occurs.

---

# Limitations

This project is a simple educational banking simulation. The following limitations are present in the current implementation.

## 1. PINs Are Stored as Plain Text

The PIN is stored directly in the JSON data.

For example:

```json
"pin": "1234"
```

A real banking application should not store authentication secrets in plain text.

---

## 2. No Encryption

The JSON file is ordinary local text data.

There is no encryption mechanism implemented.

Anyone who can access the file may be able to read its contents.

---

## 3. No Advanced Authentication

The system does not include:

- OTP authentication
- Two-factor authentication
- Biometric authentication
- Account lockout
- Login attempt limits
- Password/PIN hashing
- Session tokens

---

## 4. No Detailed Mobile Number Validation

The program asks for a mobile number but does not verify its format.

For example, it does not explicitly enforce:

- Exact length
- Country code
- Numeric-only content
- Valid telecommunications format

---

## 5. No Detailed Name Validation

The customer name is accepted as entered.

The program does not check:

- Empty names
- Character composition
- Maximum length

---

## 6. No Detailed Address Validation

The address is accepted as free-form text.

---

## 7. Floating-Point Money Representation

The program uses Python `float` for monetary amounts.

For financial software, floating-point arithmetic can create precision issues.

A production financial application would generally use a decimal/fixed-precision approach appropriate for monetary calculations.

---

## 8. No Database

The application uses a JSON file rather than a database.

This is simple for a learning project but is not suitable for large-scale banking operations.

---

## 9. No Concurrent Access Handling

The program does not implement mechanisms for multiple users/processes changing the JSON file simultaneously.

---

## 10. No Transaction Rollback System

The transfer operation updates both accounts and then saves the data.

There is no database transaction system providing sophisticated atomicity or rollback behavior.

---

## 11. No Admin Module

The application currently provides customer operations only.

There is no separate administrator interface for:

- Viewing all accounts
- Closing accounts
- Blocking accounts
- Managing customers
- Auditing activity

---

## 12. No Account Deletion

The current program does not provide an account deletion or account-closing feature.

---

## 13. No Interest Calculation

The system does not calculate:

- Savings interest
- Loan interest
- Fixed deposit interest

---

## 14. No Loan Management

There is no loan functionality.

---

## 15. No ATM/Card Management

There are no:

- ATM cards
- Debit cards
- Credit cards
- Card limits
- Card blocking features

---

## 16. No Receipt Generation

Transactions are displayed in the terminal but no PDF, print-ready, or downloadable receipt is generated by the program.

---

## 17. No Search or Filtering of Transactions

The mini statement displays the stored transactions without providing filtering by:

- Date
- Transaction type
- Amount

---

# Security Considerations

This project should be considered an **educational banking simulation**, not a real financial system.

Important security limitations include:

- PINs are stored directly in JSON.
- There is no encryption.
- There is no secure database.
- There is no secure authentication protocol.
- There is no account lockout.
- There is no audit/security monitoring system.
- Local users with file access can potentially inspect or modify the JSON file.
- Input handling is basic rather than hardened for production use.

For a real financial system, significantly stronger security architecture would be required.

---

# Possible Future Improvements

The current project can be expanded in many ways.

## Security Improvements

Possible improvements include:

- Hash PINs instead of storing them directly.
- Add login attempt limits.
- Add account lockout.
- Add OTP-based verification.
- Encrypt sensitive information.
- Use secure authentication/session management.

---

## Database Improvements

Replace JSON storage with a database such as:

- SQLite
- PostgreSQL
- MySQL

This would provide more structured persistence and better support for larger datasets.

---

## Account Management

Add:

- Account deletion
- Account blocking
- Account reactivation
- Customer profile editing
- Multiple account types

---

## Banking Features

Add:

- Interest calculation
- Loan management
- Fixed deposits
- Recurring deposits
- Bill payments
- Beneficiary management
- Scheduled transfers

---

## Transaction Features

Add:

- Transaction IDs
- Transaction filtering
- Transaction search
- Date range filtering
- Downloadable statements
- Receipt generation

---

## User Interface

The command-line interface could later be replaced with:

- Tkinter desktop GUI
- PyQt/PySide GUI
- Web application
- Mobile application

---

# Summary of Functions

| Function | Purpose |
|---|---|
| `load_data()` | Loads accounts from `bank_data.json` |
| `save_data()` | Saves accounts to `bank_data.json` |
| `generate_account_number()` | Generates the next account number |
| `create_account()` | Creates a new customer account |
| `login()` | Authenticates a customer |
| `check_balance()` | Displays the current balance |
| `deposit_money()` | Deposits money and records a transaction |
| `withdraw_money()` | Withdraws money after balance validation |
| `transfer_money()` | Transfers money between two accounts |
| `mini_statement()` | Displays transaction history |
| `account_details()` | Displays account information |
| `change_pin()` | Changes the customer's PIN |
| `customer_menu()` | Controls the logged-in customer menu |
| `main()` | Controls the main application menu |

---

# Complete Program Flow Summary

The complete program can be summarized as:

```text
START
  |
  v
Import json, os, datetime
  |
  v
Define bank_data.json
  |
  v
Define functions
  |
  v
Load existing account data
  |
  v
Main Menu
  |
  +-----------------------------+
  |                             |
  v                             v
Create Account              Customer Login
  |                             |
  v                             v
Collect details             Verify credentials
  |                             |
  v                             v
Validate PIN                Customer Menu
  |                             |
  v                             +-----------------------------+
Validate deposit                |       |       |      |      |
  |                             v       v       v      v      v
  v                          Balance Deposit Withdraw Transfer Statement
Generate account number
  |                             |
  v                             +------------------+
Create account record                              |
  |                                                v
  v                                          Account Details
Add opening transaction                            |
  |                                                v
  v                                            Change PIN
Save data                                           |
  |                                                v
  v                                             Logout
Return to Main Menu                                |
                                                   v
                                              Main Menu
                                                   |
                                                   v
                                                 Exit
```

---

# Conclusion

This Bank Management System is a compact Python console application demonstrating how a complete menu-driven application can be built using standard Python features.

It combines:

- File handling
- JSON data storage
- Dictionaries
- Lists
- Functions
- Loops
- Conditional logic
- Exception handling
- Input validation
- Date/time handling
- Transaction management
- Customer authentication

The program supports the complete basic customer flow from **account creation** through **login**, **balance management**, **money transfer**, **transaction history**, **account details**, **PIN change**, and **logout**.

Because the application uses a local JSON file and basic authentication, it is best understood as an **educational project and prototype**. It provides a useful foundation for learning and can later be extended with stronger security, database storage, advanced account management, richer transaction features, and a graphical or web-based interface.

---

## Quick Start

For the shortest path to running the application:

```bash
python code3.py
```

Then choose:

```text
1. Create New Account
```

Create an account, remember the generated account number, return to the main menu, and select:

```text
2. Customer Login
```

After logging in, use the customer menu to manage the account.

---

## Project File

The main Python implementation documented by this README contains the complete banking workflow, from loading persistent data through the main menu and customer operations to program exit. 
