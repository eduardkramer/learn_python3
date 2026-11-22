my_pizzas = ['plain', 'mushroom', '4 cheese', 'magarita']
friends_pizza = my_pizzas[:]
my_pizzas.append('hawain')
friends_pizza.append('greek')

for my_pizza in my_pizzas:
    print(f"My favorite pizza is: {my_pizza}")

print("\n")

for friend_pizza in friends_pizza:
    print(f"My friends favorite pizza is: {friend_pizza}")