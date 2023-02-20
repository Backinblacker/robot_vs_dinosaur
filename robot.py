# This sets up the Robot Class
import random
from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 1000
        self.active_weapon = [Weapon("Incessant talking", 125), Weapon("Blinding Reflection", 150), Weapon("Call in the Cavalry", 200)]
    def attack(self, dinosaur):
        choose_weapon = input("What weapon would you like to use? 1: Incessant Talking, 2: Blinding Reflection, or 3: 'Call in the Cavalry': ")
        # add for loop to print out all the weapons instead of hard coding it.
        if choose_weapon == "1":
            dinosaur.health -= self.active_weapon[0].attack_power
            print(f"{self.name} used {self.active_weapon[0].name} to bore {dinosaur.name} and caused {self.active_weapon[0].attack_power} damage!")
            print(f"{dinosaur.health} has {dinosaur.health} remaining.")
        elif choose_weapon == "2":
            dinosaur.health -= self.active_weapon[1].attack_power
            print(f"{self.name} used {self.active_weapon[1].name} to blind {dinosaur.name} and caused {self.active_weapon[1].attack_power} damage!")
            print(f"{dinosaur.health} has {dinosaur.health} remaining.")
        elif choose_weapon == "3":
            dinosaur.health -= self.active_weapon[2].attack_power
            print(f"{self.name} used {self.active_weapon[2].name} to attack {dinosaur.name} and caused {self.active_weapon[2].attack_power} damage!")
            print(f"{dinosaur.health} has {dinosaur.health} remaining.")
        else:
            print("Invalid input, please select weapon using 1, 2, or 3.")