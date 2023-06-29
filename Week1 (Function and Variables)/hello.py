# defining ur own function, def hello (parameter)
def hello(to = "world"): 
    print("hello,", to)

# calling function w/o a parameter, will automatically asign to "world"
hello()

# user input
name = input("What is your name? ").strip().title()

#calling the function with a single parameter
hello(name)