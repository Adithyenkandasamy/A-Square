from decimal import Decimal, InvalidOperation


def transfer_money(sender_account, receiver_account, amount):
    """Transfer money between two account dictionaries safely."""
    if not isinstance(sender_account, dict) or not isinstance(receiver_account, dict):
        return False, "Invalid account data"

    if "balance" not in sender_account or "balance" not in receiver_account:
        return False, "Invalid account data"

    try:
        transfer_amount = Decimal(str(amount))
        sender_balance = Decimal(str(sender_account["balance"]))
        receiver_balance = Decimal(str(receiver_account["balance"]))
    except (InvalidOperation, TypeError, ValueError):
        return False, "Invalid amount"

    if transfer_amount <= 0:
        return False, "Invalid amount"

    if transfer_amount > sender_balance:
        return False, "Insufficient funds"

    sender_account["balance"] = sender_balance - transfer_amount
    receiver_account["balance"] = receiver_balance + transfer_amount
    return True, "Transfer successful"
