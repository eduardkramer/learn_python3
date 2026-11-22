favorite_cities = ['london', 'paris', 'tokyo', 'amsterdam']
print(favorite_cities)

# Permanently sorting with .sort() method
favorite_cities.sort()
print(favorite_cities)
favorite_cities.sort(reverse=True)
print(favorite_cities)

# Temporarily sorting with sorted() method
print(sorted(favorite_cities))

# Reverse order
favorite_cities.reverse()
print(favorite_cities)

# Finding length with len()
print(len(favorite_cities))

# Print index number with methods
print(favorite_cities[0].title())
print(favorite_cities[0].upper())
print(favorite_cities[0].lower())

# Modifying list
favorite_cities[0] = 'lisabon'
print(favorite_cities)

# Appending elements to a list
favorite_cities.append('beijing')
print(favorite_cities)

# Inserting elements into a list
favorite_cities.insert(0, 'antwerpen')
print(favorite_cities)

# Removing elements using del
del favorite_cities[0]
print(favorite_cities)

# Removing using the pop() method, verwijderd laatste item van de list
popped_favorite_cities = favorite_cities.pop()
print(favorite_cities)

# Popping Items from Any Posistion in a list
first_visited = favorite_cities.pop(0)
print(f"I have visited {first_visited.title()} last year!")

# Removing by value if you don't know the posistion
favorite_cities.remove('paris')
print(favorite_cities)


