import sys

# Numbers (числа)
# Strings (строки)
# Lists (списки)
# Dictionaries (словари)
# Tuples (кортежи)
# Sets (множества)
# Boolean (логический тип данных)

# изменяемые(списки, словари и множества)
# неизменяемые(числа, строки и кортежи)
# упорядоченные(списки, кортежи, строки и словари)
# неупорядоченные(множества)

a1 = 1                  # numbers
a2 = 'abc'              # string (immutable, hashable)
a3 = [1, 2, 3, 3]       # list (mutable)
a4 = {'a': 1, 'b': 2}   # dict (mutable)
a5 = set(a3)            # set will be {1, 2, 3} (mutable)
a6 = (1, 2, 3, 3)       # tuple (immutable, hashable)

items = [a1, a2, a6]
my_hash = [hash(item) for item in items]      # immutable means (almost) hashable

assert sys.getsizeof(a3) > sys.getsizeof(a6)  # lists are bigger because mutable























