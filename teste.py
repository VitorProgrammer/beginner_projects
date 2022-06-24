starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary["c"] = 7
final_dictionary = starting_dictionary

print(final_dictionary)