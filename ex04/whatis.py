import sys

def main():
    # Check the number of arguments
    if len(sys.argv) != 2:
        raise AssertionError("more than one argument is provided" if len(sys.argv) > 2 else "No argument provided")
    
    arg = sys.argv[1]
    
    # Check if the argument is an integer
    try:
        number = int(arg)
    except ValueError:
        raise AssertionError("argument is not an integer")
    
    # Check if the number is even or odd
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()
