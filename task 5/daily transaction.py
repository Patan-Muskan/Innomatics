def transaction_limit_checker(amount):
    limit = 50000
    if amount <= limit:
        status = "Approved"
    else:
        status = "Declined"
    print("Transaction Amount:", amount)
    print("Transaction Status:", status)
transaction_limit_checker(60000)