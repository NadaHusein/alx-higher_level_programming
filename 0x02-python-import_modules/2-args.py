#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if (count == 0):
        print("0 arguments.")

    elif (count == 1):
        print("1 argument:")
    else:
        print(f"{count} arguments:")
    for arguments in range(count):
        print(f"{arguments + 1}: {sys.argv[arguments +1]}") 

