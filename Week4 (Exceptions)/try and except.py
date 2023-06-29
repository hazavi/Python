
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        #try code for error
        try:
            x = int(input("What's x? "))
        #if theres a value error, print something
        #use "pass" if u don't wanna prompt the user
        except ValueError:
            print("x is not an integer")
        else: # else it will break out of the loop
            return x

main()  