# Set the starting balance
starting_balance = 10000

records = [
    {"type": "expense", "amount": 200, "category": "food", "description": "lunch"},
    {"type": "income", "amount": 1000, "category": "investment", "description": "ETF-0050"},
    {"type": "expense", "amount": 150, "category": "transportation", "description": "gas"}
]

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

def add_transaction(records, transaction_type, amount, category, description):
    new_transaction = {
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "description": description
    }
    records.append(new_transaction)

print(f"Before:\n{len(records)} records\n\n加入一筆收入\n\n")
add_transaction(records, 'income', 2000, 'salary', 'part-time job')
print(f"Expected number of records:\n4\n\nActual:\n{len(records)}")
print(records)