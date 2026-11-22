# Een empty list maken
aliens = []

# Het maken van 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Loopt door de list en laat eerste 10 aliens zien
for alien in aliens[:10]:
    print(alien)
print("...")

# Print totale lijst van aliens
print(f"Total number of aliens: {len(aliens)}")