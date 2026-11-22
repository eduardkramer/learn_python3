# Lijst van gasten
invitation_list = ['john', 'gaz', 'ghost']
print(f"Sadly {invitation_list[1].title()} couldn't make it!")

# Huidige gast Gaz wordt vervangen met roach
invitation_list[1] = 'roach'
print("Good news for TF141, we have found a bigger table so more people can join in!")

# Worden twee gasten toegevoegd met index 3 en 4 en een laatste gast geappend als laatste in de lijst.
invitation_list.insert(3, 'truck')
invitation_list.insert(4, 'laswell')
invitation_list.append('yong')

print(f"Hello, {invitation_list[0].title()}!")
print(f"Hello, {invitation_list[1].title()}!")
print(f"Hello, {invitation_list[2].title()}!")
print(f"Hello, {invitation_list[3].title()}!")
print(f"Hello, {invitation_list[4].title()}!")
print(f"Hello, {invitation_list[5].title()}!")

# Verwijderdt gasten met pop() method
removed_guest = invitation_list.pop()
print(f"Hi {removed_guest.title()}, sadly there isn't a spot left!")
removed_guest = invitation_list.pop()
print(f"Hi {removed_guest.title()}, sadly there isn't a spot left!")
removed_guest = invitation_list.pop()
print(f"Hi {removed_guest.title()}, sadly there isn't a spot left!")
removed_guest = invitation_list.pop()
print(f"Hi {removed_guest.title()}, sadly there isn't a spot left!")

# Verwijderd de laatste 2 gasten uit de lijst
del invitation_list[0]
del invitation_list[0]

# Checkt lijst of het leeg is
print(invitation_list)
