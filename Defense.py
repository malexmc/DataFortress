from enum import Enum
from Utils import roll,getRand
import json
import os, sys

OUT_DIR = os.path.dirname(os.path.realpath(__file__))
if getattr(sys, 'frozen', False):
    OUT_DIR = os.path.dirname(sys.executable)

class DEFENSE_TYPES(Enum):
    HELLHOUND = "Hellhound"

    @classmethod
    def list_names(cls):
        return list(map(lambda c: c.name, cls))



class Defense():
    def __init__(self, name=None, coord=None):
        self.name = name.title() if name is not None else None #make sure casing is correct
        self.coord = coord
        self.program = None

        if self.name is not None:
            program_text = ""
            with open("%s\\Programs\\%s.txt" % (OUT_DIR,self.name), 'r') as program_file:
                program_text += program_file.read()

            self.program = json.loads(program_text)

    @classmethod
    def rollRandomly(cls):
        type = roll(10)
        subtype = roll(6)
        memory_cost = 0
        if type in [1,2,3,4]:
            type = "Detection/Alarm"
            if subtype in [1,2]:
                subtype = "Watchdog"
                memory_cost = 5
            elif subtype in [3,4]:
                subtype = "Bloodhound"
                memory_cost = 5
            elif subtype in [5,6]:
                subtype = "Pitbull"
                memory_cost = 6
        elif type in [5,6]:
            type = "Anti-IC"
            if subtype in [1,2]:
                subtype = "Killer (str=%s)" % str(roll(6))
                memory_cost = 5
            elif subtype in [3,4]:
                subtype = "Manticore"
                memory_cost = 3
            elif subtype in [5,6]:
                subtype = "Aardvark"
                memory_cost = 3
        elif type in [7,8]:
            type = "Anti-System"
            if subtype == 1:
                subtype = "Flatline"
                memory_cost = 2
            elif subtype == 2:
                subtype = "Poison Flatline"
                memory_cost = 2
            elif subtype == 3:
                subtype = "Krash"
                memory_cost = 2
            elif subtype == 4:
                subtype = "Viral 15"
                memory_cost = 2
            elif subtype == 5:
                subtype = "DecKrash"
                memory_cost = 2
            elif subtype == 6:
                subtype = "Murphy"
                memory_cost = 2
        elif type in [9,10]:
            type = "Anti-Personnel"
            if subtype == 1:
                subtype = "Stun"
                memory_cost = 3
            elif subtype == 2:
                subtype = "Hellbolt"
                memory_cost = 4
            elif subtype == 3:
                subtype = "Brainwipe"
                memory_cost = 4
            elif subtype == 4:
                subtype = "Knockout"
                memory_cost = 3
            elif subtype == 5:
                subtype = "Zombie"
                memory_cost = 4
            elif subtype == 6:
                subtype = "Hellhound"
                memory_cost = 6

        return cls(name=subtype)
           

    def addToJSON(self, json_object):
        DEFENSES_STRING = "defenses"
        if DEFENSES_STRING not in json_object:
            json_object[DEFENSES_STRING] = []
        remote_dict = {
                        "name" : self.name,
                        "coord" : {
                                    "x" : self.coord[0],
                                    "y" : self.coord[1]
                                  },
                        "program" : self.program
                      }
        json_object[DEFENSES_STRING].append(remote_dict)