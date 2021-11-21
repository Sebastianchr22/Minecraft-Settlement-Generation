#Settlers are the agents of simulation in this project. 
# An agent will be bord with a brain of two components: 
#       - The prefrontal cortex (impulsive, and controlling in order to achieve personal goals) also called 'system 1'
#       - The neo-cortex (thoughtful, decision making part) also called 'system 2'

from NeoCortex import NeoCortex
from PrefrontalCortex import PrefrontalCortex
from Decisions import Decisions

#To be removed
import sys

####To implement: All world grids must contains all its blocks, and all settlers upon the cell.

class Settler:
    def __init__(self, level, world_grid, origin) -> None:
        self.decisions = Decisions()
        self.system1 = PrefrontalCortex(self)
        self.system2 = NeoCortex(self, level, world_grid, origin)
        self.has_shelter = False
        self.food = 1
        self.has_mate = False
        self.children = 0

    def step(self) -> None:
        impulse, weights = self.system1.get_impulse()
        self.system2.handle_impulse(impulse, weights)

    #Hunger is proportionally small compared to the supply of food available to the settler
    def _get_hunger(self) -> float:
        return 1/self.food
    
    def add_food(self, food) -> None:
        self.food += food

    def _get_has_shelter(self) -> bool:
        return self.has_shelter
    
    def set_has_shelter(self) -> None:
        self.has_shelter = True

    def _get_has_mate(self) -> bool:
        return self.has_mate
    
    def set_has_mate(self) -> None:
        self.has_mate = True

    def _get_children_num(self) -> int:
        return self.children

    def add_children(self, num) -> None:
        self.children += num

    def _get_decisions(self) -> Decisions:
        return self.decisions

def main():
    n = 1
    settlers = [None] * n
    for i in range(0, n):
        settlers[i] = Settler(None, [0] * 14, 0)
    
    steps = 10

    for step in range(0, steps):
        for settler in settlers:
            settler.step()

    for settler in settlers:
        settler._get_decisions().print_decisions()


if __name__ == '__main__':
    sys.exit(main()) 
