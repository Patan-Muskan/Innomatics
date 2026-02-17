user_ids = ["user1", "user2", "user1", "user3", "user1", "user3"]
# count user ids
user_count = {}
for user in user_ids:
    user_count[user] = user_count.get(user, 0) + 1
# print duplicates
for user, count in user_count.items():
    if count > 1:
        print(user, "->", count, "times")
        