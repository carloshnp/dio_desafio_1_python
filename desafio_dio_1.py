"""
This program allows the user to perform banking operations such as deposit, withdrawal, and checking account statement.
The user is presented with a menu and can select the desired operation by entering the corresponding number.
The program keeps track of the account balance, withdrawal attempts, and generates an account statement.
The maximum withdrawal amount and the withdrawal limit are predefined constants.
"""

MAX_WITHDRAWAL = 500
account_statement = ""
withdrawal_attempts = 0
WITHDRAWAL_LIMIT = 3
balance = 0

menu = """

[1] Deposit
[2] Withdraw
[3] Account Statement
[4] Exit

=> """

def deposit():
    global balance, account_statement
    amount = float(input("Inform the amount of the deposit: "))
    if amount > 0:
        balance += amount
        account_statement += f"Deposit: R$ {amount:.2f}\n"
    else:
        print("Operation failed! The informed amount is invalid.")

def withdraw():
    global balance, account_statement, withdrawal_attempts
    amount = float(input("Inform the withdrawal amount: "))
    exceeded_balance = amount > balance
    exceeded_MAX_WITHDRAWAL = amount > MAX_WITHDRAWAL
    exceeded_withdrawals = withdrawal_attempts >= WITHDRAWAL_LIMIT

    if exceeded_balance:
        print("Operation failed! You do not have enough balance.")
    elif exceeded_MAX_WITHDRAWAL:
        print("Operation failed! The withdrawal amount has been exceeded.")
    elif exceeded_withdrawals:
        print("Operation failed! Maximum withdrawals exceeded.")
    elif amount > 0:
        balance -= amount
        account_statement += f"Withdrawal: R$ {amount:.2f}\n"
        withdrawal_attempts += 1
    else:
        print("Operation failed! The informed amount is invalid.")

def account_statement_func():
    global account_statement, balance
    print("\n================ Account Statement ================")
    print("No transitions were made." if not account_statement else account_statement)
    print(f"\nBalance: R$ {balance:.2f}")
    print("==========================================")

operations = {
    "1": deposit,
    "2": withdraw,
    "3": account_statement_func,
    "4": exit
}

while True:
    home = input(menu)
    try:
        operations[home]()
    except KeyError:
        print("Invalid operation, please re-select the desired option.")