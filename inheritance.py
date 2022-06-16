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

    def attack(self):
        self.stamina -= 10
        if (self.stamina < 0):
            self.stamina = 0

    def rest(self):
        self.stamina = 100

    def damage(self, damage):
        self.hp -= damage
        if (self.hp < 0):
            self.hp = 0

    def speak(self):
        print("Hello my name is " + self._name)

class Knight(Villager):
    def __init__(self, name):
        self.hp = 150
        self.stamina = 100
        self.attack = 15
        self._name = name
        self.armor = 50

    def loadSpecialAttack(self):
        if (self.stamina >= 50):
            self.stamina -= 50
        else:
            print("Not enough stamina")
    def damage(self, damage):
        self.armor =- damage
        if (self.armor < 0):
            self.armor = 0
        self.hp =- damage + self.armor

def main():
    x = Knight("alex")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        exit(84)