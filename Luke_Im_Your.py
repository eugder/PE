def relation_to_luke(name):
    names = {"Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "droid",}
    result = names[name]
    return "Luke, I am your {}.".format(result)

print(relation_to_luke("Leia"))