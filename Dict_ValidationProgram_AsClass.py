import uuid

class TransactionProcessor:
    def __init__(self):
        self.seen_source_ids = set()

    def validate_uuid(self, account_id):
        """Helper to isolate UUID logic."""
        try:
            uuid.UUID(str(account_id))
            return True
        except (ValueError, TypeError, AttributeError):
            return False

    def process_batch(self, data):
        valid_transactions = []
        errors = []

        for record in data:
            source_id = record.get("source_id")
            account_id = record.get("account_id")
            amount = record.get("amount")

            # 1. Deduplication
            if source_id in self.seen_source_ids:
                errors.append({"source_id": source_id, "reason": "Duplicate"})
                continue

            # 2. Structure/UUID Validation
            if not self.validate_uuid(account_id):
                errors.append({"source_id": source_id, "reason": f"Bad UUID: {account_id}"})
                continue

            # 3. Business Logic
            if not isinstance(amount, (int, float)) or amount <= 0:
                errors.append({"source_id": source_id, "reason": f"Bad Amount: {amount}"})
                continue

            # Successful record
            self.seen_source_ids.add(source_id)
            valid_transactions.append(record)

        return valid_transactions, errors

    # --- Running the test ---
raw_data = [
        {"source_id": "tx-101", "account_id": "851996ec-", "amount": 100.50},
        {"source_id": "tx-102", "account_id": "851996ec-1234-4321-8888-1234567890ab", "amount": -50.00},
        {"source_id": "tx-103", "account_id": "851996ec-1234-4321-8888-1234567890ab", "amount": 25.00},
        {"source_id": "tx-103", "account_id": "851996ec-1234-4321-8888-1234567890ab", "amount": 25.00},
]

transaction_processor=TransactionProcessor()
valid,errors=transaction_processor.process_batch(raw_data)

print("✅ Valid Transactions:", valid)
print("❌ Errors Found:", errors)