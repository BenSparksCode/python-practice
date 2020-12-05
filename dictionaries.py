# Dictionary: Key-Value pairs, unordered, mutable
dicty = {"name": "Ben", "age": 24, "city": "Cape Town"}

# Adding to dictionary
dicty["surname"] = "Sparks"
print(dicty)

# Removing from dictionary
dicty.pop("surname") #as of Python 3.7 -> this removes last added item, not random
print(dicty)