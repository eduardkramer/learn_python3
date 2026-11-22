requested_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'onions', 'chicken strips']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we are out of green peppers right now")
    if requested_topping == 'chicken strips':
        print("Sorry we are out of chicken strips right now")
    else:
        print(f"Added: {requested_topping}")

print("\nFinished making your pizza!")