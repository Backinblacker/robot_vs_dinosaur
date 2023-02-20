# This sets up the Robot Class

from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 1000
        self.active_weapon = Weapon
    def attack(self, dinosaur):
        dinosaur.health -= active_weapon.attack_power
        print(dinosaur.health)

active_weapon = Weapon("Incessant Talking", 25)
weapon_2 = Weapon("Blinding Reflection", 50)
bonus_weapon = Weapon("Calls in the Cavalry", 200)