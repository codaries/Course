"""import sys

try:
    print(3 / a)
except NameError:
    print("bruh It's", sys.exc_info()[1])
except ZeroDivisionError:
    print("It's", sys.exc_info()[1])"""

x = "hello"

assert x == "goodbye", "x should be hello"
