# hier wordt een lege lijst gemaakt
squares = []

# for-loop met de value van 1 t/m 10
for value in range(1, 11):
    # nieuwe waarde = value waarde ** 2 (tot de macht 2)
    square = value ** 2

    # de uitkomst verwerkt hij in de empty list
    squares.append(square)

    # print resultaat
print(squares)

