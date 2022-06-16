##
## EPITECH PROJECT, 2022
## python
## File description:
## generator
##

import sys
import random

def generator():
    res = random.randint(0, 100)
    print(res)

def main():
    generator()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        exit(84)