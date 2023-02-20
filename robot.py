# This sets up the Robot Class

from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 1000
        self.active_weapon = [Weapon("1: Incessant talking", 100), Weapon("Blinding Reflection", 100), Weapon("Call in the Cavalry", 150)]
    def attack(self, dinosaur):
        choose_weapon = input("What weapon would you like to use? 1: Incessant Talking, 2: Blinding Reflection, or 3: 'Call in the Cavalry'")
        if choose_weapon == "1":
            dinosaur.health -= self.active_weapon[0].attack_power
            print(f"{self.name} used {self.active_weapon[0].name} to bore {dinosaur.name} and caused {self.active_weapon[0]} damage!")
            print(f"{dinosaur.health} has {dinosaur.health} remaining.")
        elif choose_weapon == "2":
            dinosaur.health -= self.active_weapon[1].attack_power
            print(f"{self.name} used {self.active_weapon[1].name} to blind {dinosaur.name} and caused {self.active_weapon[1]} damage!")
            print(f"{dinosaur.health} has {dinosaur.health} remaining.")
        if choose_weapon == "3":
            dinosaur.health -= self.active_weapon[2].attack_power
            print(f"{self.name} used {self.active_weapon[2].name} to attack {dinosaur.name} and caused {self.active_weapon[2]} damage!")
            print(f"{dinosaur.health} has {dinosaur.health} remaining.")
        else:
            print("Invalid input, please select weapon using 1, 2, or 3.")