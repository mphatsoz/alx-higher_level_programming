import sys

def add_arguments(*args):
    result = sum(int(arg) for arg in args)
    print(result)

if __name__ == "__main__":
    arguments = sys.argv[1:]  # Exclude the script name from the arguments
    add_arguments(*arguments)

