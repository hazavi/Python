name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron": # | = or
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # anything else but the match name cases
        print("Who?")