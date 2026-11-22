usernames = ['johnv', 'hellocat', 'uppedog707', 'jajamy', 'admin']
for username in usernames:
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Welcome, {username}, thank you for logging in again.")
