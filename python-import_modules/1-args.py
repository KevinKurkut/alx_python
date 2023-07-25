from sys import argv
if __name__ == "__main__":
    y = len(argv)
for i in range(1, y+1):
    if y==0:
        print("{} arguments.".format(y))
    elif y==1:
        print("{} argument:".format(y))
        print("{}: {}".format(y, argv))
    else:
        print("{} arguments:".format(y))
        print("{}: {}".format(y, argv()))
