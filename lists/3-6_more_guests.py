invitation_list = ['john', 'gaz', 'ghost']
print(f"Sadly {invitation_list[1].title()} couldn't make it!")
invitation_list[1] = 'roach'
print("Good news for TF141, we have found a bigger table so more people can join in!")
invitation_list.insert(3, 'truck')
invitation_list.insert(4, 'laswell')
invitation_list.append('yong')
print(f"Hi {invitation_list[0].title()}, you have been invited!")
print(f"Hi {invitation_list[1].title()}, you have been invited!")
print(f"Hi {invitation_list[2].title()}, you have been invited!")
print(f"Hi {invitation_list[3].title()}, you have been invited!")
print(f"Hi {invitation_list[4].title()}, you have been invited!")
print(f"Hi {invitation_list[5].title()}, you have been invited!")
print("Please take your seats at the table!")