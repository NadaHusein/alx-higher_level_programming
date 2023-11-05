#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    '''
    
    Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
    : (or . if no arguments were passed) followed by
    a new line, followed by (if at least one argument),
    one line per argument:
        the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
'''

    count = len(sys.argv) - 1
    if (count == 0):
        print("0 arguments.")

    elif (count == 1):
        print("1 argument:")
    else:
        print(f"{count} arguments:")
    for arguments in range(count):
        print(f"{arguments + 1}: {sys.argv[arguments +1]}") 

