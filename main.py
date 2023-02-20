# This is the main file for the project

from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon
active_weapon = Weapon("Incessant Talking", 60)
triceratops = Dinosaur("Cera", 100)
c3PO = Robot("C3PO")

triceratops.attack(c3PO)
c3PO.attack(triceratops)