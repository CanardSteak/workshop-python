##
## EPITECH PROJECT, 2022
## python
## File description:
## syntax
##

from locale import atoi
import sys
import math

def main(nb, nb1):
    res = int(nb) // int(nb1)
    print (res)

if __name__ == "__main__":
    try:
        main(sys.argv[1], sys.argv[2])
    except Exception as e:
        print("ErrorAlexis :", e, file=sys.stderr)
        exit(84)