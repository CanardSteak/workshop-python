##
## EPITECH PROJECT, 2022
## python
## File description:
## main
##

import sys


def cal():
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

def calculate(list):
    res = 0
    i = 0
    for i in range(i, len(list)):
        res += int (list[i])
    
    print(res)
        

def main():
    # cal();
    list = ["2", "3", "2"]
    calculate(list)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        exit(84)
