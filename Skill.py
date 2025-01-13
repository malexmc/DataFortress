from enum import Enum
from Utils import roll,getRand
import random

class SKILL_TYPES(Enum):
    ACCOUNTING = "Accounting"
    ANTHROPOLOGY = "Anthropology"
    BOTANY = "Botany"
    CHEMISTRY = "Chemistry"
    COMPOSITION = "Composition"
    CRYOTANK_OPERATION = "Cryotank Operation"
    DIAGNOSE_ILLNESS = "Diagnose Illness"
    DRIVING = "Driving"
    EDUCATION_GENERAL_KNOWLEDGE = "Education & General Knowledge"
    GAMBLE = "Gamble"
    GEOLOGY = "Geology"
    HEAVY_WEAPONS = "Heavy Weapons (as a mounted weapon)"
    HISTORY = "History"
    LANGUAGE = "Language"
    LIBRARY_SEARCH = "Library Search"
    MATHEMATICS = "Mathematics"
    OPERATE_HVY_MACHINERY = "Operate Hvy. Machinery"
    PAINT_OR_DRAW = "Paint or Draw"
    PHARMACEUTICALS = "Pharmaceuticals"
    PHYSICS = "Physics"
    PILOT = "Pilot"
    PLAY_INSTRUMENT = "Play Instrument (if electronic)"
    PROGRAMMING = "Programming"
    RIFLE = "Rifle (as a mounted weapon)"
    STOCK_MARKET = "Stock Market"
    SUBMACHINEGUN = "Submachinegun (as a mounted weapon)"
    SYSTEM_KNOWLEDGE = "System Knowledge"
    TEACHING = "Teaching"
    ZOOLOGY = "Zoology"

    @classmethod
    def list_names(cls):
        return list(map(lambda c: c.name, cls))

class Skill():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    @classmethod
    def rollRandomly(cls):
        skill_type = random.choice(SKILL_TYPES.list_names())
        value = roll(6)+4
        return cls(key=skill_type, value=value)

    def addToJSON(self, json_object):
        SKILLS_STRING = "skills"
        if SKILLS_STRING not in json_object:
            json_object[SKILLS_STRING] = []
        remote_dict = {
                        "key" : self.key,
                        "value" : self.value
                      }
        json_object[SKILLS_STRING].append(remote_dict)