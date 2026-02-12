# Message Length Analyzer
messages = ["Hi", "Welcome to the platform", "OK"]
# analyze the length of message
for message in messages:
    length = len(message)
    print(f"Message: '{message}' - Length: {length}")

# flag message longer than 10 characters
print("\nMessages flagged (longer than 10 characters):")
for message in messages:
    if len(message) > 10:
        print(f"Message: '{message}' is flagged.")
