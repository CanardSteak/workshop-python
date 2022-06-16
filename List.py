##
## EPITECH PROJECT, 2022
## python
## File description:
## main
##

import sys 

def List(list):
    res = 0
    i = 0
    for i in range(i, len(list)):
        res += int (list[i])
    
    print(res)

def main():
    list = ["2", "3", "2"]
    List(list)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        exit(84)
