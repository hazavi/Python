# defining own funtion 
def main(): 
    name = input("What is your name? ").strip().title()
    print(name)

def hello(to = "world"): 
    print("hello,", to)

# calling the funtion
main()