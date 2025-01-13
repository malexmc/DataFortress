import random
from enum import Enum

class DIRECTIONS(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

def roll(faces):
    return random.randint(1,faces)

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
    x,y = origin.coords
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
    adjacent = getAdjacentDict(origin, fortress)
    adjacent_list = []
    for key in adjacent.keys():
        adjacent_list.append(adjacent[key]["coords"])
    return adjacent_list

    