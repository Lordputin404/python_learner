# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                    1. positional 2. default 3. keyword 4. arbitrary


def hello(greeting, first, last):
    print(f"{greeting} I am {first} {last}")

hello(greeting="Hello",last="NotABug",first="Definitely")