if __name__ == "__main__":
    import sys
"""subsequent elements from index 1"""
args = sys.argv[1:]
argument_number = len(args)
if argument_number == 0:
    print("0 arguments.")
else:
    print(f"{argument_number} {'argument' if argument_number == 1 else 'arguments'}:")
    for i, arg in enumerate(args, 1):
        print(f"{i}: {arg}")
