from html.entities import name2codepoint


# defining own function 
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

# defining function that returns square
def square(n):
    return n * n

# calling function
main()