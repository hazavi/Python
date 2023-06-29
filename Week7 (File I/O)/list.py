names = []

for _ in range(3):
    names.append(input("What's ur name? "))
# sort names
for name in sorted(names):
    print(f"hello, {name}")