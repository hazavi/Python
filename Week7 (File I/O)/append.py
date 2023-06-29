name = input("What's your name? ")

# append text into a text file
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
 
