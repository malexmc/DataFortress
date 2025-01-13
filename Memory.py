from enum import Enum
import Utils

class Memory():
    def __init__(self, name=None, CPU=None, contents=None, memory_remaining=10,  coords=[0,0]):
        self.name = name
        self.CPU = CPU
        self.contents = contents
        self.memory_remaining = memory_remaining
        self.coords = coords

    def addToJSON(self, json_object):
        MU_STRING = "mu"
        MU_NODES_STRING = "muNodes"
        if MU_STRING not in json_object:
            json_object[MU_STRING] = []
        mu_dict = {
                    "key" : self.contents,
                    "value" : int(10-self.memory_remaining),
                  }
        json_object[MU_STRING].append(mu_dict)
        
        if MU_NODES_STRING not in json_object:
            json_object[MU_NODES_STRING] = []
        mu_nodes_dict = {
                            "x" : self.coords[0],
                            "y" : self.coords[1],
                        }
        json_object[MU_NODES_STRING].append(mu_nodes_dict)