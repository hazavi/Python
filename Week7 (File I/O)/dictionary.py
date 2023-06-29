students = []

with open("students.csv") as file:
    for line in file:
        # 2 variables in one. left and right
        name, house = line.rstrip().split(",")
        #dictionary
        student = {"name": name, "house": house}
        students.append(student)


# lambda = anonymos function, no name
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")