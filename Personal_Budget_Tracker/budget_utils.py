
import json
import os

file_path = 'Personal_Budget_Tracker/transactions.json'

def load_transactions():
    if not os.path.exists(file_path) or not os.path.getsize(file_path) > 0:
        return []
    with open(file_path, 'r') as f:
        return json.load(f)

def save_transaction(transaction):
    data = load_transactions()
    data.append(transaction)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def group_by_category():
    transactions = load_transactions()
    grouped = {}
    for txn in transactions:
        cat = txn['category']
        grouped.setdefault(cat, []).append(txn)
    return grouped

def calculate_totals(grouped):
    totals = {}
    for category, txns in grouped.items():
        total = sum(t['amount'] for t in txns)
        totals[category] = round(total, 2)
    return totals
