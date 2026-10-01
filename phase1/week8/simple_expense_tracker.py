# Set the starting balance
starting_balance = 10000

records = [
    {"type": "expense", "amount": 200, "category": "food", "description": "lunch"},
    {"type": "income", "amount": 1000, "category": "investment", "description": "ETF-0050"},
    {"type": "expense", "amount": 150, "category": "transportation", "description": "gas"}
]

empty_records = []

def calculate_total_by_type(records, target_type):
    total = 0
    for record in records:
        if record["type"] == target_type:
            total += record["amount"]
    return total

def calculate_current_balance(records, starting_balance):
    total_income = calculate_total_by_type(records, "income")
    total_expense = calculate_total_by_type(records, "expense")

    current_balance = starting_balance + total_income - total_expense
    return current_balance

def add_transaction(records, starting_balance, transaction_type, amount, category, description):
    new_transaction = {
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "description": description
    }

    if new_transaction["type"] == "income":
        records.append(new_transaction)
        return True

    if new_transaction["type"] == "expense":
        current_balance = calculate_current_balance(records, starting_balance)
        if is_current_balance_enough(current_balance, amount):
            records.append(new_transaction)
            return True
        return False

def is_current_balance_enough(current_balance, expense_amount):
    if current_balance >= expense_amount:
        return True
    return False

def display_all_transactions(records):
    if len(records) == 0:
        print("No transactions found.")
        return

    transaction_number = 1

    for record in records:
        print(f"Transaction {transaction_number}")
        print(f"Type: {record['type']}")
        print(f"Amount: {record['amount']}")
        print(f"Category: {record['category']}")
        print(f"Description: {record['description']}")
        print()

        transaction_number += 1

def display_financial_summary(records, starting_balance):
    total_income = calculate_total_by_type(records, "income")
    total_expense = calculate_total_by_type(records, "expense")
    current_balance = calculate_current_balance(records, starting_balance)

    print("Financial Summary")
    print(f"Total income: {total_income}")
    print(f"Total expense: {total_expense}")
    print(f"Current balance: {current_balance}")


user_starting_balance = float(input("Please enter your current asset: "))
if user_starting_balance >= 0:
    while True:
        print("Simple Expense Tracker")
        print()
        print("1. Add transaction")
        print("2. View all transactions")
        print("3. View financial summary")
        print("4. Exit")
        print()
        choice = input("Please choose an option(1-4): ")
        if choice == "1":
            transaction_type = input("Please enter income or expense: ")
            if (transaction_type == "income") or (transaction_type == "expense"):
                amount = float(input("Please enter the amount: "))
                category = input("Please enter the category: ")
                description = input("Please enter the description: ")

                if add_transaction(records, user_starting_balance, transaction_type, amount, category, description):
                    print("交易已成功紀錄")
                else:
                    print("目前餘額不足扣款")
            else:
                print("Invalid transaction type")
        elif choice == "2":
            display_all_transactions(records)
        elif choice == "3":
            display_financial_summary(records, user_starting_balance)
        elif choice == "4":
            break
        else:
            print("Invalid option")


# print("正常資料測試")
# display_financial_summary(records, starting_balance)
# print()
# print("沒有交易測試")
# display_financial_summary(empty_records, starting_balance)

# print(f"正常案例:\ntest records 有 {len(records)} 筆")
# display_all_transactions(records)
# print()
# print(f"邊界案例:\nempty_records = []")
# display_all_transactions(empty_records)

# print(f"Test 1 : 收入\n目前 records = {len(test1_records)} 筆\n\n新增 income 2000\n")
# transaction1 = add_transaction(test1_records, 10000, 'income', 2000, 'salary', 'part-time job')
# print(f"Expected return: True\nActual return: {transaction1}\n\nExpected number of records: 4\nActual number of records: {len(test1_records)}\n")

# print(f"Test 2 : 合法支出\n假設目前餘額足夠\n\n新增 expense 500\n")
# transaction2 = add_transaction(test2_records, 10000, 'expense', 500, 'food', 'lunch')
# print(f"Expected return: True\nActual return: {transaction2}\n\nExpected number of records: 4\nActual number of records: {len(test2_records)}\n")

# print(f"Test 3 : 餘額不足\n設計一筆明顯超過目前餘額的 expense\n")
# transaction3 = add_transaction(test3_records, 10000, 'expense', 15000, 'game', 'LOL')
# print(f"Expected return: False\nActual return: {transaction3}\n\nExpected number of records: 3\nActual number of records: {len(test3_records)}\n")




# print(is_current_balance_enough(1000, 999))
# print(is_current_balance_enough(1000, 1000))
# print(is_current_balance_enough(1000, 1001))
# print(is_current_balance_enough(1000, 1500))