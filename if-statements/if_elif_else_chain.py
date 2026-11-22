age = 12
if age < 4:
    print("Your admission cost is $0.") # Korting voor kleuters

elif age == 12:
    print("Your admission cost is $5.") # Korting voor tieners

elif age == 18:
    print("Your admission cost is $12.") # Korting voor studenten

elif age >= 65:
    print("Your admission cost is $9.") # Korting voor senioren

else:
    print("Your admission cost is $16.") # Normale prijs

