import uuid
from importlib.util import source_hash


def process_transactions(data):
    valid_transactions = []
    errors = []
    seen_source_ids = set()  # To track duplicates in O(1) time

    for record in data:
        source_id = record.get("source_id")
        account_id = record.get("account_id")
        amount = record.get("amount")

        # 1. Check for Duplicate source_id
        if source_id in seen_source_ids:
            errors.append({"source_id": source_id, "reason": "Duplicate transaction ID"})
            continue

        # 2. Validate UUID format
        try:
            uuid.UUID(str(account_id))
        except (ValueError, TypeError, AttributeError):
            errors.append({"source_id": source_id, "reason": f"Invalid UUID: {account_id}"})
            continue

        # 3. Validate Amount (Business Logic)
        if not isinstance(amount, (int, float)) or amount <= 0:
            errors.append({"source_id": source_id, "reason": f"Invalid amount: {amount}"})
            continue

        # If all checks pass
        seen_source_ids.add(source_id)
        valid_transactions.append(record)

    return valid_transactions, errors


# --- Running the test ---
raw_data = [
    {"source_id": "tx-101", "account_id": "851996ec-", "amount": 100.50},
    {"source_id": "tx-102", "account_id": "851996ec-1234-4321-8888-1234567890ab", "amount": -50.00},
    {"source_id": "tx-103", "account_id": "851996ec-1234-4321-8888-1234567890ab", "amount": 25.00},
    {"source_id": "tx-103", "account_id": "851996ec-1234-4321-8888-1234567890ab", "amount": 25.00},
]





def validate_transaction(raw_data):

    uniquesource_id=set()
    error=[]
    valid_transactions=[]

    for record in raw_data:
        source_id=record.get("source_id")
        account_id=record.get("account_id")
        amount = record.get("amount")

        #1. Check for duplicate
        if source_id in uniquesource_id:
            error.append({"source_id":source_id,"account_id" : account_id, "amount": amount , "reason":"duplicate source ID"})
            continue

        #Check UUID vaid
        try:
            uuid.UUID(str(account_id))
        except (ValueError,TypeError,AttributeError):
            error.append({"source_id":source_id,"account_id" : account_id, "amount": amount , "reason":"InvalidUUID"})
            continue

        #Validate Amount

        if not isinstance(amount,(int,float)) or amount< 0 :
            error.append({"source_id":source_id,"account_id" : account_id, "amount": amount , "reason":"InvalidAmount"})
            continue


        uniquesource_id.add(source_id)
        valid_transactions.append({"source_id": source_id, "account_id": account_id, "amount": amount})


    return valid_transactions, error




valid, issues = validate_transaction(raw_data)

print("✅ Valid Transactions:", valid)
print("❌ Errors Found:", issues)