from enum import Enum
from Utils import *

CPU_MAX_DISTANCE = 5

class CPU():
    def __init__(self, name=None, coords=[0,0]):
        self.name = name
        self.coords = coords

    def addToJSON(self, json_object):
        CPU_NODES_STRING = "cpuNodes"
        if CPU_NODES_STRING not in json_object:
            json_object[CPU_NODES_STRING] = []
        cpu_nodes_dict = printCoords(self.coords)
        json_object[CPU_NODES_STRING].append(cpu_nodes_dict)