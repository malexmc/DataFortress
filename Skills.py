from enum import Enum

class SKILLS(Enum):
    ACCOUNTING = "Accounting",
    ANTHROPOLOGY = "Anthropology",
    BOTANY = "Botany",
    CHEMISTRY = "Chemistry",
    COMPOSITION = "Composition",
    CRYOTANK_OPERATION = "Cryotank Operation",
    DIAGNOSE_ILLNESS = "Diagnose Illness",
    DRIVING = "Driving",
    EDUCATION_GENERAL_KNOWLEDGE = "Education & General Knowledge",
    GAMBLE = "Gamble",
    GEOLOGY = "Geology",
    HEAVY_WEAPONS = "Heavy Weapons (as a mounted weapon)",
    HISTORY = "History",
    LANGUAGE = "Language",
    LIBRARY_SEARCH = "Library Search",
    MATHEMATICS = "Mathematics",
    OPERATE_HVY_MACHINERY = "Operate Hvy. Machinery",
    PAINT_OR_DRAW = "Paint or Draw",
    PHARMACEUTICALS = "Pharmaceuticals",
    PHYSICS = "Physics",
    PILOT = "Pilot",
    PLAY_INSTRUMENT = "Play Instrument (if electronic)",
    PROGRAMMING = "Programming",
    RIFLE = "Rifle (as a mounted weapon)",
    STOCK_MARKET = "Stock Market",
    SUBMACHINEGUN = "Submachinegun (as a mounted weapon)",
    SYSTEM_KNOWLEDGE = "System Knowledge",
    TEACHING = "Teaching",
    ZOOLOGY = "Zoology"

class Skill():
    def __init__(self, key="", value=0):
        self.key = key
        self.value = value

    def addToJSON(self, json_object):
        SKILLS_STRING = "skills"
        if SKILLS_STRING not in json_object:
            json_object[SKILLS_STRING] = []
        remote_dict = {
                        "key" : self.key,
                        "value" : self.value
                      }
        json_object[SKILLS_STRING].append(remote_dict)