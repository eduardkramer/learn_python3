person = {
    "first_name": "john",
    "last_name": "kramer",
    "age": 72,
    "city": "den haag"
}
print(person.get('country'))
country_search = person.get('country')
if country_search is None:
    print("404: country not found!")