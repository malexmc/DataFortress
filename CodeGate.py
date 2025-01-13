from Utils import *
import math

class CodeGate():
    def __init__(self, str=None, cpu_count=1, coords=[1,1]):
        if str is None:
            self.str = math.floor(roll(6)/2) + cpu_count
        self.str = str
        self.coords = coords

    def addToJSON(self, json_object):
        CODEGATES_STRING = "codegates"
        if CODEGATES_STRING not in json_object:
            json_object[CODEGATES_STRING] = []
        remote_dict = {
                        "str" : self.str,
                        "coord" : {
                                    "x" : self.coords[0],
                                    "y" : self.coords[1]
                                  }
                      }
        json_object[CODEGATES_STRING].append(remote_dict)