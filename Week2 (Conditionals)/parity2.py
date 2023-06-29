def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# if the number in parameter remainder equal to 0 then return True else its False
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main() 