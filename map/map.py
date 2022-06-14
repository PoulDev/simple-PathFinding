import os
from .objects import Objects
from .prettifier import objects as prettifier_objects

class Map:
    def generateMap(self, width = 50, height = 50):
        self.width = width
        self.height = height
        self.map = [[Objects.NULL for _ in range(self.width+1)] for _ in range(self.height+1)]
        return self.map

    def print(self):
        os.system('cls')
        print('╒' + '═' * (self.width+1) + '╕')
        for row in self.map:
            print('│', end='')
            for cell in row:
                print(prettifier_objects.get(cell), end="")
            print('│')
        print('╘' + '═' * (self.width+1) + '╛')

    def spawn(self, object, position):
        if self.getPosition(position) not in [Objects.start, Objects.end, Objects.wall]:
            self.map[position[1]][position[0]] = object

    def clearAnimations(self):
        for rowIndex, row in enumerate(self.map):
            for cellIndex, cell in enumerate(row):
                if cell == Objects.path:
                    self.map[rowIndex][cellIndex] = Objects.NULL

    def getPosition(self, position):
        if position[1] < 0 or position[1] > self.height:
            return -1
        if position[0] < 0 or position[0] > self.width:
            return -1
        return self.map[position[1]][position[0]]
