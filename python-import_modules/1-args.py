from sys import argv
if __name__ == "__main__":
    arg_len = len(argv)-1
    if arg_len == 0:
        print("0 arguments.")
    elif arg_len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_len))
        for i in range(i, len(arg_len)):
            print("{}: {}".format(i, arg_len[i]))
