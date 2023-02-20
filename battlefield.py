from robot import Robot
from dinosaur import Dinosaur
from fleet import Fleet
from herd import Herd
import random

class Battlefield:
    def __init__(self, name):
        self.dinosaur = Dinosaur(self, 175)
        self.robot = Robot(self)
        self.herd = Herd(self.herd.herd)
        self.fleet = Fleet(self.fleet.robot_fleet)
        self.name = name
        
    def welcome_to_the_fight(self):
        print(f"Today we witness {self.robot.name} getting lost in a prehistoric jungle and now has to fight for their life against a {self.dinosaur.name}")
    
    def random_dino(self,):
        dino_select = random.choice(self.herd.herd)
        self.dinosaur = dino_select
        print(f"{dino_select} is today's Dino Champion!")
        return dino_select
    
    def random_robot(self,):
        robot_select = random.choice(self.fleet.robot_fleet)
        self.robot = robot_select
        print(f"{robot_select} is today's Robot Champion!")
        return robot_select
    
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