# Creates dictionary with people and favorite programming languages
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "java"
}

# Creates a list with targeted people
friends = ['jen', 'edward']
for name in sorted(favorite_languages.keys()):
    print(f"\nHi {name.title()}")

# If the above names are in list, it will print targeted list
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, i see your love {language}")

# Checks if erin is in dictionary as a key
if 'erin' not in favorite_languages.keys():
        print("\nErin, please take our poll!\n")

# Prints out the values instead of keys
for language in favorite_languages.values():
     print(f"{language.title()}")

