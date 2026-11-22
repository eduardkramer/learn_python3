favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

print("\t\tFavorite programming languages:")
for k, v in favorite_languages.items():
    print(f"{k.title()}: {v.title()}")

names = ['john', 'timmy', 'jen', 'edward', 'phil', 'sarah']

for name in names:
    if name not in favorite_languages:
        print(f"{name.title()} Please take the poll!")

    else:
        print(f"Thanks for taking the poll, {name.title()}!")
