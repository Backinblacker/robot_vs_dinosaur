# This is the battlefield where the action will happen
import random
from robot import Robot
from dinosaur import Dinosaur
# Herd goes here
# Fleet goes here

class Battlefield:
    def __init__(self, name):
        self.dinosaur = None
        self.robot = None
        self.name = name
        
    