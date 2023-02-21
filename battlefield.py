# This is the battlefield where the action will happen
import random
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:
    def __init__(self, name):
        self.dinosaur = Dinosaur("Triceratops", random.randint(100,250))
        self.robot = Robot("C3PO")
        self.name = name
        
    def welcome_to_the_fight(self):
        print(f"Today we witness {self.robot.name} getting lost in a prehistoric jungle and now has to fight for their life against a {self.dinosaur.name}")
    
    def the_battle(self):
        while self.robot.health >= 0 and self.dinosaur.health >= 0:
            self.robot.attack(self.dinosaur)
            if self.robot.health <= 0:
                print(f"{self.robot.name} has been defeated.")
                break
            elif self.dinosaur.health <= 0:
                print(f"{self.dinosaur.name} has been defeated.")
                break
            self.dinosaur.attack(self.robot)
            if self.robot.health <= 0:
                print(f"{self.robot.name} has been defeated.")
                break
            elif self.dinosaur.health <= 0:
                print(f"{self.dinosaur.name} has been defeated.")
                break
        else:
            print("Let's go again!")
    
    def who_won(self):
        if self.robot.health <= 0:
            print(f"{self.dinosaur.name} has defeated {self.robot.name}!")
        elif self.dinosaur.health <= 0:
            print(f"{self.robot.name} has shocked the historians and defeated {self.dinosaur.name}!")
            
    def run_battle(self):
        self.welcome_to_the_fight()
        self.the_battle()
        self.who_won()

battlefield = Battlefield("Lost in the Jungle")