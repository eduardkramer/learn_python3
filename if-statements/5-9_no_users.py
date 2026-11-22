usernames = []
if usernames == []:
        print(f"We need to find some users!")
for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Welcome, {username}, thank you for logging in again.")
