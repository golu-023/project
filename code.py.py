import json
import os
from datetime import datetime

FILE_NAME = "bank_data.json"


# ---------------- LOAD DATA ----------------

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


# ---------------- SAVE DATA ----------------

def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)


# ---------------- GENERATE ACCOUNT NUMBER ----------------

def generate_account_number():
    if not accounts:
        return "1001"

    numbers = [int(acc) for acc in accounts.keys()]
    return str(max(numbers) + 1)


# ---------------- CREATE ACCOUNT ----------------

def create_account():
    print("\n========== CREATE ACCOUNT ==========")

    name = input("Enter customer name: ")
    mobile = input("Enter mobile number: ")
    address = input("Enter address: ")

    while True:
        pin = input("Create a 4-digit PIN: ")

        if len(pin) == 4 and pin.isdigit():
            break
        else:
            print("PIN must contain exactly 4 digits.")

    while True:
        try:
            deposit = float(input("Enter initial deposit: ₹"))

            if deposit >= 0:
                break
            else:
                print("Deposit cannot be negative.")

        except ValueError:
            print("Please enter a valid amount.")

    account_number = generate_account_number()

    accounts[account_number] = {
        "name": name,
        "mobile": mobile,
        "address": address,
        "pin": pin,
        "balance": deposit,
        "transactions": []
    }

    accounts[account_number]["transactions"].append({
        "type": "Account Opening",
        "amount": deposit,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })

    save_data()

    print("\nAccount created successfully!")
    print("Your Account Number is:", account_number)


# ---------------- LOGIN ----------------

def login():
    print("\n========== CUSTOMER LOGIN ==========")

    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")

    if account_number in accounts:

        if accounts[account_number]["pin"] == pin:
            print("\nLogin successful!")
            print("Welcome,", accounts[account_number]["name"])

            customer_menu(account_number)

        else:
            print("Incorrect PIN.")

    else:
        print("Account not found.")


# ---------------- CHECK BALANCE ----------------

def check_balance(account_number):
    print("\n========== BALANCE ==========")

    balance = accounts[account_number]["balance"]

    print("Account Number:", account_number)
    print("Account Holder:", accounts[account_number]["name"])
    print("Available Balance: ₹", balance)


# ---------------- DEPOSIT ----------------

def deposit_money(account_number):
    print("\n========== DEPOSIT MONEY ==========")

    try:
        amount = float(input("Enter amount to deposit: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        accounts[account_number]["balance"] += amount

        accounts[account_number]["transactions"].append({
            "type": "Deposit",
            "amount": amount,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

        save_data()

        print("₹", amount, "deposited successfully.")
        print("New Balance: ₹", accounts[account_number]["balance"])

    except ValueError:
        print("Please enter a valid amount.")


# ---------------- WITHDRAW ----------------

def withdraw_money(account_number):
    print("\n========== WITHDRAW MONEY ==========")

    try:
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > accounts[account_number]["balance"]:
            print("Insufficient balance.")
            return

        accounts[account_number]["balance"] -= amount

        accounts[account_number]["transactions"].append({
            "type": "Withdrawal",
            "amount": amount,
            "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })

        save_data()

        print("₹", amount, "withdrawn successfully.")
        print("Remaining Balance: ₹", accounts[account_number]["balance"])

    except ValueError:
        print("Please enter a valid amount.")


# ---------------- TRANSFER MONEY ----------------

def transfer_money(account_number):
    print("\n========== MONEY TRANSFER ==========")

    receiver = input("Enter receiver account number: ")

    if receiver not in accounts:
        print("Receiver account not found.")
        return

    if receiver == account_number:
        print("You cannot transfer money to your own account.")
        return

    try:
        amount = float(input("Enter amount to transfer: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        if amount > accounts[account_number]["balance"]:
            print("Insufficient balance.")
            return

        accounts[account_number]["balance"] -= amount
        accounts[receiver]["balance"] += amount

        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        accounts[account_number]["transactions"].append({
            "type": "Transfer to " + receiver,
            "amount": amount,
            "date": date
        })

        accounts[receiver]["transactions"].append({
            "type": "Received from " + account_number,
            "amount": amount,
            "date": date
        })

        save_data()

        print("Money transferred successfully!")
        print("Transferred: ₹", amount)

    except ValueError:
        print("Please enter a valid amount.")


# ---------------- MINI STATEMENT ----------------

def mini_statement(account_number):
    print("\n========== MINI STATEMENT ==========")

    transactions = accounts[account_number]["transactions"]

    if not transactions:
        print("No transactions found.")
        return

    for transaction in transactions:
        print("--------------------------------")
        print("Type:", transaction["type"])
        print("Amount: ₹", transaction["amount"])
        print("Date:", transaction["date"])


# ---------------- ACCOUNT DETAILS ----------------

def account_details(account_number):
    print("\n========== ACCOUNT DETAILS ==========")

    account = accounts[account_number]

    print("Account Number :", account_number)
    print("Name           :", account["name"])
    print("Mobile         :", account["mobile"])
    print("Address        :", account["address"])
    print("Balance        : ₹", account["balance"])


# ---------------- CHANGE PIN ----------------

def change_pin(account_number):
    print("\n========== CHANGE PIN ==========")

    old_pin = input("Enter current PIN: ")

    if old_pin != accounts[account_number]["pin"]:
        print("Incorrect current PIN.")
        return

    while True:
        new_pin = input("Enter new 4-digit PIN: ")

        if len(new_pin) == 4 and new_pin.isdigit():
            break

        print("PIN must contain exactly 4 digits.")

    accounts[account_number]["pin"] = new_pin

    save_data()

    print("PIN changed successfully!")


# ---------------- CUSTOMER MENU ----------------

def customer_menu(account_number):

    while True:

        print("\n====================================")
        print("        CUSTOMER BANKING MENU")
        print("====================================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Mini Statement")
        print("6. Account Details")
        print("7. Change PIN")
        print("8. Logout")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(account_number)

        elif choice == "2":
            deposit_money(account_number)

        elif choice == "3":
            withdraw_money(account_number)

        elif choice == "4":
            transfer_money(account_number)

        elif choice == "5":
            mini_statement(account_number)

        elif choice == "6":
            account_details(account_number)

        elif choice == "7":
            change_pin(account_number)

        elif choice == "8":
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")


# ---------------- MAIN MENU ----------------

def main():

    while True:

        print("\n")
        print("==========================================")
        print("        BANK MANAGEMENT SYSTEM")
        print("==========================================")
        print("1. Create New Account")
        print("2. Customer Login")
        print("3. Exit")
        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            login()

        elif choice == "3":
            print("\nThank you for using our Bank Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


# ---------------- START PROGRAM ----------------

accounts = load_data()

main()