programming_words = {"variable": "A name that refers to a value.", 
                     "string": "A sequence of characters.", 
                     "list": "A collection of items.", 
                     "tuple": "An ordered collection of items that cannot be changed.", 
                     "dictionary": "Stores information as key-value pairs.",
                     "integer": "A whole number, positive or negative, without decimals.",
                     "float": "A number that has a decimal point.",
                     "boolean": "A data type that can only be True or False.",
                    "if statement": "A conditional statement that executes a block of code if a specified condition is true.",
                    "for loop": "A control flow statement that allows code to be executed repeatedly based on"
                     }
for k, v in programming_words.items():
    print(f"\n{k.title()}: {v}")
