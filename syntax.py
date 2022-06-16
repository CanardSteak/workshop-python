##
## EPITECH PROJECT, 2022
## python
## File description:
## syntax
##

import sys

def syntax():
    i = 0
    for i in range(i, 100):
        if (i % 3 == 0):
            print("three")
        elif (i % 5 == 0):
            print("five")
        elif (i % 3 == 0) and (i % 5 == 0):
            print("threeFive")
        else:
            print(i);

def main():
    syntax()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        exit(84)