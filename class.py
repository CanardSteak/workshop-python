##
## EPITECH PROJECT, 2022
## python
## File description:
## class
##

import sys

class Villager:
    def __init__(self, name):
        self.hp = 100
        self.stamina = 100
        self.attack = 5
        self._name = name
    def printInfo(self):
        print(self.attack)

def main():
    x = Villager("alex")
    x.printInfo()
    

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        exit(84)