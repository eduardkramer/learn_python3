current_users = ['jason4', 'ameliax', 'telsnel2', 'star-5', 'jackv']
new_users = ['doggopoes', 'JASON4', 'jackv', 'itsyourboyV','yur5']
lowercase_users = []

for current_user in current_users:
    lowercase_users.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in lowercase_users:
        print(f"Please check your name {new_user}!")
    else:
        print(f"The username {new_user} is available!")
