from enum import Enum
from Utils import *

class REMOTE_TYPES(Enum):
    TERMINAL = 6
    MICROPHONE = 7
    CAMERA = 8
    HOLODISPLAY = 9
    VIDEO = 10
    PRINTER = 11
    VEHICLE = 12
    ALARM = 13
    DOOR = 14
    ELEVATOR = 15
    MANIPULATOR = 16
    AUTOFACTORY = 17

    @classmethod
    def list_names(cls):
        return list(map(lambda c: c.name, cls))



class Remote():
    def __init__(self, name=None, subtype=None, coords=[0,0]):
        self.name = name
        self.type = subtype
        self.coords = coords

    @classmethod
    def rollRandomly(cls):
        name = ""
        subtype = None
        roll_val = roll(10)
        if roll_val == 1:
            name = "Microphone"
            subtype = REMOTE_TYPES.MICROPHONE
        elif roll_val == 2:
            name = "TV Camera"
            subtype = REMOTE_TYPES.CAMERA
        elif roll_val == 3:
            name = "Extra Terminal"
            subtype = REMOTE_TYPES.TERMINAL
        elif roll_val == 4:
            roll_val = (3)
            if roll_val < 3:
                name = "Videoboard"
                subtype = REMOTE_TYPES.VIDEO
            if roll_val == 3:
                name = "Holodisplay"
                subtype = REMOTE_TYPES.HOLODISPLAY
        elif roll_val == 5:
            name = "Printer"
            subtype = REMOTE_TYPES.PRINTER
        elif roll_val == 6:
            name = "Alarm"
            subtype = REMOTE_TYPES.ALARM
        elif roll_val == 7:
            name = "Remote Vehicle or Robot"
            subtype = REMOTE_TYPES.VEHICLE
        elif roll_val == 8:
            name = "Automatic door, gate"
            subtype = REMOTE_TYPES.DOOR
        elif roll_val == 9:
            name = "Elevator"
            subtype = REMOTE_TYPES.ELEVATOR
        elif roll_val == 10:
            roll_val = roll(2)
            if roll_val == 1:
                name = "Manipulator"
                subtype = REMOTE_TYPES.MANIPULATOR
            if roll_val == 2:
                name = "Autofactory"
                subtype = REMOTE_TYPES.AUTOFACTORY
        return cls(name=name, subtype=subtype, coords=[0,0])
    

    def addToJSON(self, json_object):
        REMOTES_STRING = "remotes"
        if REMOTES_STRING not in json_object:
            json_object[REMOTES_STRING] = []
        remote_dict = {
                        "name" : self.name,
                        "type" : self.type.value,
                        "coord" : printCoords(self.coords)
                      }
        json_object[REMOTES_STRING].append(remote_dict)