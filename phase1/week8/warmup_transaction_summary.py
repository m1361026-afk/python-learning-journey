records = [
    {"type": "income", "amount": 5000},
    {"type": "expense", "amount": 1200},
    {"type": "income", "amount": 3000},
    {"type": "expense", "amount": 800},
    {"type": "expense", "amount": 400}
]

def calculate_total_by_type(records, target_type):
    target_type_total = 0
    for record in records:
        if record["type"] == target_type:
            target_type_total += record["amount"]
    return target_type_total

def calculate_balance(records):
    income_total = calculate_total_by_type(records, "income")
    expense_total = calculate_total_by_type(records, "expense")
    return income_total - expense_total

income = calculate_total_by_type(records, "income")
expense = calculate_total_by_type(records, "expense")
balance = calculate_balance(records)

print(f"Income: {income}")
print(f"Expense: {expense}")
print(f"Balance: {balance}")