from sys import argv
if __name__ == "__main__":
    def print_arguments(args):
        number = len(argv)
        if number==0:
            print("{} argument")
        elif number==1:
            print("{} arguments.")
            print("{}: {}".format(number, args))

        
        
        