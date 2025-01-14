from Utils import *

class DataWall():
    def __init__(self, str=0, coords=[1,1]):
        self.str = str
        self.coords = coords

    def addToJSON(self, json_object):
        DATAWALLSTR_STRING = "datawallStr"
        DATAWALLNODES_STRING = "datawallNodes"

        if DATAWALLSTR_STRING not in json_object:
            json_object[DATAWALLSTR_STRING] = self.str

        if DATAWALLNODES_STRING not in json_object:
            json_object[DATAWALLNODES_STRING] = []
            
        remote_dict = printCoords(self.coords)

        json_object[DATAWALLNODES_STRING].append(remote_dict)