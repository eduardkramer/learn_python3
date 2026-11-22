invitation_list = ['john', 'gaz', 'ghost']
print(f"Sadly {invitation_list[1].title()} couldn't come!")
invitation_list[1] = 'roach'
print(f"Hi {invitation_list[0].title()}, you have been invited!")
print(f"Hi {invitation_list[1].title()}, you have been invited!")
print(f"Hi {invitation_list[2].title()}, you have been invited!")