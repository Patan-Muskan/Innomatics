def duplicate_accounts(usernames):
    unique_usernames = set(usernames)
    if len(unique_usernames) < len(usernames):
        result = "Yes"
    else:
        result = "No"
    print("Duplicate Accounts Found:", result)
users = ["john", "alex", "john", "mike"]
duplicate_accounts(users)
