# printing rows in csv file
# csv = comma separated value
with open("students.csv") as file:
    for line in file:
        # 2 variables in one. left and right
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")