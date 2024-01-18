import random

WALL_VALUE = 'X'

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



class DataFortress():
    class FortressBoard():

        def __init__(self, method="traditional"):
            self.board = {}
            self.GRID_MAX = 7 #playing on an 8x8 board
            #Make blank board of 8x8
            for ii in range (8):
                row = {}
                for jj in range(8):
                    row[jj] = []
                self.board[ii] = row
            self.addWalls()

        def getAllIndices(self):
            indices = []
            for ii in range(0,self.GRID_MAX+1):
                for jj in range(0,self.GRID_MAX+1):
                    indices.append([ii,jj])
            return indices

        def getSurrounding(self,row,col):
            surrounding = []
            for ii in range(row-1,row+2):
                for jj in range(col-1,col+2):
                    if ii >= 0 and ii <= self.GRID_MAX and jj >= 0 and jj <= self.GRID_MAX:
                        surrounding.append([ii,jj,self.board[ii][jj]])
                    else:
                        surrounding.append([ii,jj,[]])
            return surrounding

        def isEmpty(self,ii,jj):
            return self.board[ii][jj] == []

        def setCellValue(self, ii,jj, value_array):
            self.board[ii][jj] = value_array

        
        def countEntrances(self):
            '''Draws "lines" from the edge of the board straight towards the middle. If it hits an "inner" tile (the middle 4x4), then it is an entrance'''
            entrance_count = 0
            #Get valid starting spaces. No Corners.
            indices = []
            for col in range(1,self.GRID_MAX):
                indices.append([0,col])
                indices.append([self.GRID_MAX,col])
            for row in range(1,self.GRID_MAX):
                indices.append([row,0])
                indices.append([row, self.GRID_MAX])

            for index in indices:
                if index[0] == 0: #coming from the top, so looking to hit row 2
                    continue #TODO: Finish this

        def addWalls(self):
            #Start with a random space in the outer 2 layers
            outer_layer_spaces = []
            for ii in [0,1,6,7]:
                for jj in range(0,7):
                    outer_layer_spaces.append([ii,jj])
            for jj in [0,1,6,7]:
                for ii in range(0,7):
                    if [ii,jj] not in outer_layer_spaces:
                        outer_layer_spaces.append([ii,jj])

            #set the first spot to a wall
            first_spot = outer_layer_spaces[random.randint(0,len(outer_layer_spaces))]
            self.setCellValue(first_spot[0],first_spot[1],[WALL_VALUE])

            #Place more outer walls
            fail_count = 0
            more_walls = True
            while more_walls:
                current_cell = outer_layer_spaces[random.randint(0,len(outer_layer_spaces)-1)]
                #If the cell is unused
                if self.isEmpty(current_cell[0],current_cell[1]):
                    #Count the surrounding walls
                    surroundings = self.getSurrounding(current_cell[0],current_cell[1])
                    count_walls = 0
                    for array in surroundings:
                        if array[2] == [WALL_VALUE]:
                            count_walls = count_walls + 1
                    if count_walls <= 3:
                        self.setCellValue(current_cell[0],current_cell[1], [WALL_VALUE])
                    else:
                        fail_count += 1
                        if fail_count:
                            more_walls = False

            

    def skills_set(self):
        skills_set = set()
        for skill in self.ALL_SKILLS:
            skills_set.add(skill)
        return skills_set
    
    def getVirtual(self):
        virtual = []
        value1 = roll(6)
        value2 = roll(6)
        if value1 == 1:
            virtual.append("Virtual Conference")
        elif value1 == 2:
            virtual.append("Virtual Office")
        elif value1 == 3:
            virtual.append("Virtual Rec-Area")
        elif value1 == 4:
            virtual.append("Virtual Building")
        elif value1 == 5:
            virtual.append("Virtual City")
        elif value1 == 6:
            virtual.append("Virtual World")

        if value2 == 1 or value2 == 2:
            virtual.append("Simple")
        elif value2 == 3:
            virtual.append("Contextual")
        elif value2 == 4:
            virtual.append("Fractal")
        elif value2 == 5:
            virtual.append("Photorealistic")
        elif value2 == 6:
            virtual.append("Superrealistic")
        
    def getFile(self):
        value = roll(6)
        if value == 1:
            return "Inter Office"
        elif value == 2:
            return "Database"
        elif value == 3:
            return "Business Records"
        elif value == 4:
            return "Financial Transactions"
        elif value == 5:
            return "Grey Ops"
        elif value == 6:
            return "Black Ops"
        
    def setPersonality(self):
        if self.intelligence >= 12:
            PERSONALITY_ROLL = roll(6)
            if PERSONALITY_ROLL == 1:
                self.personality = "Friendly, curious"
            elif PERSONALITY_ROLL == 2:
                self.personality = "Hostile, paranoid"
            elif PERSONALITY_ROLL == 3:
                self.personality = "Stable, intelligent, businesslike"
            elif PERSONALITY_ROLL == 4:
                self.personality = "Intellectual, detached"
            elif PERSONALITY_ROLL == 5:
                self.personality = "Machinelike"
            elif PERSONALITY_ROLL == 6:
                self.personality = "Remote and godlike"

            REACTION_ROLL = roll(6)
            if REACTION_ROLL == 1 or REACTION_ROLL == 2:
                self.reaction = "Neutral"
            elif REACTION_ROLL == 3:
                self.reaction = "Kill all intruders"
            elif REACTION_ROLL == 4:
                self.reaction = "Observe intruders, then act"
            elif REACTION_ROLL == 5:
                self.reaction = "Report all intruders"
            elif REACTION_ROLL == 6:
                self.reaction = "Talk to intruder to find intent"

            ICON_ROLL = roll(6)
            if ICON_ROLL == 1:
                self.ICON = "Human"
            elif ICON_ROLL == 2:
                self.ICON = "Geometric"
            elif ICON_ROLL == 3:
                self.ICON = "Mythological"
            elif ICON_ROLL == 4:
                self.ICON = "Voice Only"
            elif ICON_ROLL == 5:
                self.ICON = "Technic"
            elif ICON_ROLL == 6:
                self.ICON = "Humanoid"
   
    def getDefense(self):
        type = roll(10)
        subtype = roll(6)
        if type in [1,2,3,4]:
            type = "Detection/Alarm"
            if subtype in [1,2]:
                subtype = "Watchdog"
            elif subtype in [3,4]:
                subtype = "Bloodhound"
            elif subtype in [5,6]:
                subtype = "Pitbull"
        elif type in [5,6]:
            type = "Anti-IC"
            if subtype in [1,2]:
                subtype = "Killer (str=%s)" % str(roll(6))
            elif subtype in [3,4]:
                subtype = "Manticore"
            elif subtype in [5,6]:
                subtype = "Aardvark"
        elif type in [7,8]:
            type = "Anti-System"
            if subtype == 1:
                subtype = "Flatline"
            elif subtype == 2:
                subtype = "Poison Flatline"
            elif subtype == 3:
                subtype = "Krash"
            elif subtype == 4:
                subtype = "Viral 15"
            elif subtype == 5:
                subtype = "DecKrash"
            elif subtype == 6:
                subtype = "Murphy"
        elif type in [9,10]:
            type = "Anti-Personnel"
            if subtype == 1:
                subtype = "Stun"
            elif subtype == 2:
                subtype = "Hellbolt"
            elif subtype == 3:
                subtype = "Brainwipe"
            elif subtype == 4:
                subtype = "Knockout"
            elif subtype == 5:
                subtype = "Zombie"
            elif subtype == 6:
                subtype = "Hellhound"

            return [type, subtype]
        
    def getRemote(self):
        type = roll(10)
        if type == 1:
            type = "Microphone"
        elif type == 2:
            type = "TV Camera"
        elif type == 3:
            type = "Extra Terminal"
        elif type == 4:
            type = "Videoboard"
        elif type == 5:
            type = "Printer"
        elif type == 6:
            type = "Alarm"
        elif type == 7:
            type = "Remote Vehicle or Robot"
        elif type == 8:
            type = "Automatic door, gate"
        elif type == 9:
            type = "Elevator"
        elif type == 10:
            type = "Manipulator or Autofactory"


    
    def printBoard(self, board):
        outString = ""
        for ii in board:
            for jj in board[ii]:
                outString += "|%s|" % (' ' if len(board[ii][jj]) == 0 else WALL_VALUE)
            outString += "\n"
        print(outString)
            


    def __init__(self):
        WALL_VALUE = 'x'
        self.printBoard(self.FortressBoard().board)

        #Step #1: CPU info (p164)
        self.CPUs = roll(6)
        self.memory = {}
        for memory_slot in range(4*self.CPUs):
            self.memory[memory_slot] = []
        self.code_gates = self.CPUs
        self.terminal = self.CPUs
        self.intelligence = 3*self.CPUs 
        self.personality = ""
        self.reaction = ""
        self.ICON = ""


        self.ALL_SKILLS = ["Accounting", "Anthropology", "Botany", "Chemistry", "Composition", "Cryotank Operation",
                       "Diagnose Illness", "Driving", "Education & General Knowledge", "Gamble", "Geology",
                       "Heavy Weapons (as a mounted weapon)", "History.", "Language", "Library Search", "Mathematics",
                       "Operate Hvy. Machinery", "Paint or Draw", "Pharmaceuticals", "Physics", "Pilot",
                       "Play Instrument (if electronic)", "Programming", "Rifle (as a mounted weapon)", "Stock Market",
                       "Submachinegun (as a mounted weapon)", "System Knowledge", "Teaching", "Zoology"]
        
        #Step #2: Wall Strength (p164)
        self.wall_strength = roll(6) + round(self.CPUs/2.0)

        #Step #3: Code Gate Strength (p164)
        self.code_gate_strength = roll(6) + round(self.CPUs/2.0)

        #Step #4: 5 Skills (p164, and skill list from p157)
        self.skills = {}
        for index in getRand(5,1,len(self.ALL_SKILLS)):
            self.skills[self.ALL_SKILLS[index]] = roll(6)+4

        #Step #5: Types of files (p164)
        for ii in range(2*len(self.memory.keys())):
            file = self.getFile()
            memory_unit = roll(len(self.memory.keys()))
            self.memory[memory_unit] = self.memory[memory_unit].append(file)
        
        #Step #6 Virtuals (p164)
        self.virtuals = []
        if roll(3) == 3:
            self.virtuals.append(self.getVirtual())
        
        self.remotes = []
        for ii in range(roll(6)):
            self.remotes.append(self.getRemote())

newFort = DataFortress()                                                                                                                                              