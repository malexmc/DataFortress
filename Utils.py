import random
from enum import Enum

class DIRECTIONS(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    @classmethod
    def list_names(cls):
        return list(map(lambda c: c.name, cls))

def roll(faces):
    return random.randint(1,faces)

def percentChance(percent):
    odds = []
    for ii in range(percent):
        odds.append(1)
    for ii in range(100-percent):
        odds.append(0)
    if random.choice(odds) == 1:
        return True
    return False

def getRand(count, start, stop):
    values = []
    for ii in range(count):
        number = random.randint(start,stop)
        if number not in values:
            values.append(number)
        else:
            ii = ii-1
    return values

#Used to get the objects in cardinal adjacency to the provided object
def getAdjacentDict(origin, fortress):
    x = origin[0]
    y = origin[1]
    board = fortress.board
    adjecent = {}
    if x > 0:
        adjecent[DIRECTIONS.LEFT] = {
                                        "value": board[x-1][y],
                                        "coords" : [x-1, y]
                                    }
    if x < len(fortress.board)+1:
        adjecent[DIRECTIONS.RIGHT] = {
                                        "value": board[x+1][y],
                                        "coords" : [x+1, y]
                                     }
    if x > 0:
        adjecent[DIRECTIONS.UP] = {
                                        "value": board[x][y-1],
                                        "coords" : [x, y-1]
                                  }
    if x < len(fortress.board[1])+1:
        adjecent[DIRECTIONS.DOWN] = {
                                        "value": board[x][y+1],
                                        "coords" : [x, y+1]
                                    }
    return adjecent

def getAdjacentList(origin, fortress):
    current_cell = fortress.getBoardCell(origin)
    adjacent = getAdjacentDict(origin, fortress)
    adjacent_list = []
    for key in adjacent.keys():
        adjacent_list.append(adjacent[key]["coords"])
    return adjacent_list

#Our program uses 1 as the first index, but the website uses 0. Make that translation.
def printCoords(coords):
    out_coords = {
                                    "x" : coords[0]-1,
                                    "y" : coords[1]-1
                }
    return out_coords

    