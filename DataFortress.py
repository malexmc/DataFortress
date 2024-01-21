import random
import math

WALL_VALUE = '---'
BLANK_VALUE = '   '
CODE_GATE_VALUE = "G"
CPU_MAX_DISTANCE = 5

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
            self.board_legend = {}
            self.GRID_MAX = 19 #playing on an 8x8 board
            #Make blank board of 8x8
            for ii in range (self.GRID_MAX+1):
                row = {}
                for jj in range(self.GRID_MAX+1):
                    row[jj] = []
                self.board[ii] = row

        def getAllIndices(self):
            indices = []
            for ii in range(0,self.GRID_MAX+1):
                for jj in range(0,self.GRID_MAX+1):
                    indices.append([ii,jj])
            return indices

        def isNeighbor(self, home, neighbor):
            #Check orthogonal neighbors
            adjacent = []
            for ii in range(home[0]-1, home[0]+2):
                for jj in range(home[1]-1, home[1]+2):
                    adjacent.append([ii,jj])
            return neighbor in adjacent

        def getSurrounding(self,row,col):
            surrounding = []
            for ii in range(row-1,row+2):
                for jj in range(col-1,col+2):
                    if ii >= 0 and ii <= self.GRID_MAX and jj >= 0 and jj <= self.GRID_MAX:
                        surrounding.append([ii,jj,self.board[ii][jj]])
                    else:
                        surrounding.append([ii,jj,[]])
            return surrounding

        def isEmpty(self,ii_jj_array):
            return self.board[ii_jj_array[0]][ii_jj_array[1]] == []

        def setCellValue(self, ii,jj, value_array):
            self.board[ii][jj] = value_array

    def setEntranceMax(self):
        self.ENTRANCE_MAX = 0
        result = roll(10)
        if result in [1]:
            self.ENTRANCE_MAX = 4
        elif result in [2,3]:
            self.ENTRANCE_MAX = 3
        elif result in [4,5,6,7]:
            self.ENTRANCE_MAX = 2
        elif result in [8,9,10]:
            self.ENTRANCE_MAX = 1

    def setInnerWallMax(self):
        self.INNER_WALL_MAX = 0
        result = roll(10)
        if result in [1]:
            self.INNER_WALL_MAX = 5
        elif result in [2,3,4,5]:
            self.INNER_WALL_MAX = 4
        elif result in [6,7,8]:
            self.INNER_WALL_MAX = 3
        elif result in [9,10]:
            self.INNER_WALL_MAX = 2            

    def countEntrances(self):
        '''Draws "lines" from the edge of the board straight towards the middle. If it hits an "inner" tile (the middle 4x4), then it is an entrance'''
        entrance_count = 0
        entrances = []
        #Get valid starting spaces. No Corners.
        indices = []
        for col in range(1,self.GRID_MAX):
            indices.append([0,col])
            indices.append([self.GRID_MAX,col])
        for row in range(1,self.GRID_MAX):
            indices.append([row,0])
            indices.append([row, self.GRID_MAX])

        for ii,jj in indices:
            if ii == 0: #coming from the top, so looking to pass through walls on left and right
                while ii < self.GRID_MAX-1:
                    if (self.board[ii][jj] == [] and
                        self.board[ii+1][jj] == [] and
                        self.board[ii][jj-1] == [WALL_VALUE] and
                        self.board[ii][jj+1] == [WALL_VALUE]
                    ):
                        entrance_count += 1
                        entrances.append([ii,jj])
                    ii += 1
            elif ii == self.GRID_MAX: #coming from the bottom, so looking to pass through walls on left and right
                while ii > 1:
                    if (self.board[ii][jj] == [] and
                        self.board[ii-1][jj] == [] and
                        self.board[ii][jj-1] == [WALL_VALUE] and
                        self.board[ii][jj+1] == [WALL_VALUE]
                    ):
                        entrance_count += 1
                        entrances.append([ii,jj])
                    ii -= 1
            elif jj == 0: #coming from the bottom, so looking to pass through walls on left and right
                while jj < self.GRID_MAX-1:
                    if (self.board[ii][jj] == [] and
                        self.board[ii][jj+1] == [] and
                        self.board[ii-1][jj] == [WALL_VALUE] and
                        self.board[ii+1][jj] == [WALL_VALUE]
                    ):
                        entrance_count += 1
                        entrances.append([ii,jj])
                    jj += 1
            elif jj == self.GRID_MAX: #coming from the bottom, so looking to pass through walls on left and right
                while jj > 1:
                    if (self.board[ii][jj] == [] and
                        self.board[ii][jj-1] == [] and
                        self.board[ii-1][jj] == [WALL_VALUE] and
                        self.board[ii+1][jj] == [WALL_VALUE]
                    ):
                        entrance_count += 1
                        entrances.append([ii,jj])
                    jj -= 1

        return entrance_count

    def getOuterSpaceIndices(self):
        outer_space_indices = []
        for ii in [0,1,6,7]:
            for jj in range(0,7):
                outer_space_indices.append([ii,jj])
        for jj in [0,1,6,7]:
            for ii in range(0,7):
                if [ii,jj] not in outer_space_indices:
                    outer_space_indices.append([ii,jj])
        return outer_space_indices
    
    def getInnerSpaceIndices(self):
        inner_layer_spaces = []
        for ii in [2,3,4,5]:
            for jj in range(0,7):
                inner_layer_spaces.append([ii,jj])
        for jj in [2,3,4,5]:
            for ii in range(0,7):
                if [ii,jj] not in inner_layer_spaces:
                    inner_layer_spaces.append([ii,jj])
        return inner_layer_spaces
        

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
                outString += "|%s|" % (BLANK_VALUE if len(board[ii][jj]) == 0 else ' : '.join(board[ii][jj]))
            outString += "\n\n"
        print(outString)
            
    def placeCPUsAndMemory(self):
        #Allow placement on any cell but outermost layer
        valid_cell_indices  = []
        for ii in range(4,self.fortress.GRID_MAX-4):
            for jj in range(4,self.fortress.GRID_MAX-4):
                valid_cell_indices.append([ii,jj])
        cpus_placed = 0
        cpu_first_spot = []
        memory_placed = 0
        while cpus_placed < self.CPUs:
            cpu_cell = None
            if cpus_placed > 0:
                #If we've placed a CPU, make sure others are within CPU_MAX_DISTANCE to aid clustering
                within_range = False
                while not within_range:
                    cpu_cell = valid_cell_indices[random.randint(0,len(valid_cell_indices)-1)]
                    cpu_distance = abs(cpu_cell[0] - cpu_first_spot[0]) + abs(cpu_cell[1] - cpu_first_spot[1])
                    if cpu_distance <= CPU_MAX_DISTANCE:
                        within_range = True
            else:
                cpu_cell = valid_cell_indices[random.randint(0,len(valid_cell_indices)-1)]
            if self.fortress.isEmpty(cpu_cell):
                current_cells = [cpu_cell]
                memory_cells = []
                while len(memory_cells) < 4:
                    memory_cell = valid_cell_indices[random.randint(0,len(valid_cell_indices)-1)]
                    has_component_neighbor = False
                    for component in current_cells:
                        if self.fortress.isNeighbor(memory_cell,component):
                            has_component_neighbor = True
                            break
                    if (
                        memory_cell not in current_cells and 
                        memory_cell in valid_cell_indices and
                        self.fortress.isEmpty(memory_cell) and
                        has_component_neighbor
                        ):
                        memory_cells.append(memory_cell)
                        current_cells.append(memory_cell)
                for cell in memory_cells:
                    cell_value = "M%s" % "{:02d}".format(memory_placed)
                    self.fortress.setCellValue(cell[0], cell[1],[cell_value])
                    memory_placed += 1
                cell_value = "C%s" % "{:02d}".format(cpus_placed)
                self.fortress.setCellValue(cpu_cell[0], cpu_cell[1],[cell_value])
                if cpu_first_spot == []:
                    cpu_first_spot = cpu_cell
                cpus_placed += 1

    def setBoundingBox(self):
        '''Once CPUs and memory are placed, create a "bounding box".
        Entrances will be placed along the bounding box'''
        top_row = self.fortress.GRID_MAX
        bottom_row = 0
        left_col = self.fortress.GRID_MAX
        right_col = 0
        for row in range(self.fortress.GRID_MAX+1):
            for col in range(self.fortress.GRID_MAX+1):
                current_cell = [row,col]
                if self.fortress.board[row][col] == []:
                    continue
                current_row = current_cell[0]
                current_col = current_cell[1]
                if current_cell[0] != []:
                    if current_row < top_row:
                        top_row = current_row
                    if current_row > bottom_row:
                        bottom_row = current_row
                    if current_col < left_col:
                        left_col = current_col
                    if current_col > right_col:
                        right_col = current_col

        #Set the bounding coordinates with a buffer of 2 (if possible)
        self.top_row = max(0,top_row - 2)
        self.bottom_row = min(self.fortress.GRID_MAX,bottom_row + 2)
        self.left_col = max(0,left_col - 2)
        self.right_col = min(self.fortress.GRID_MAX,right_col + 2)

    def getBoundingBoxPerimiter(self):
        perimiter = []
        #Add top points. Don't add corners
        col_range = range(self.left_col+1, self.right_col)
        row_range = range(self.top_row+1, self.bottom_row)
        for ii in col_range:
            perimiter.append([self.top_row, ii])
        for ii in row_range:
            perimiter.append([ii, self.right_col])
        for ii in reversed(col_range):
            perimiter.append([self.bottom_row, ii])
        for ii in reversed(row_range):
            perimiter.append([ii, self.left_col])
        return perimiter

    def isOnBoundingBox(self,coordinates):
        '''Checks if coordinates are on the perimiter of the bounding box. Used for entrance creation.'''
        perimiter = self.getBoundingBoxPerimiter()
        return coordinates in perimiter
    
    def isInBoundingBox(self, coordinates):
        '''Checks if coordinates are inside the bounding box. On the edges are excluded (see isOnBoundingBox()).
        Used to add peripherals once the box is set.'''
        valid_cells = []
        #Add top points. Don't add corners
        for ii in range(self.top_row+1, self.bottom_row):
            for jj in range(self.left_col+1, self.right_col):
                valid_cells.append([ii,jj])
        return coordinates in valid_cells

    def setEntrances(self):
        perimiter = self.getBoundingBoxPerimiter()
        entrance_count = 0
        while entrance_count < self.ENTRANCE_MAX:
            entrance_cell = perimiter[random.randint(0,len(perimiter)-1)]
            if self.fortress.isEmpty(entrance_cell):
                self.fortress.setCellValue(entrance_cell[0], entrance_cell[1], ["%s%s" % (CODE_GATE_VALUE,"{:02d}".format(entrance_count))])
                entrance_count+=1       


    #TODO: Rewrite this to work with new CPU Placement
    def addWalls(self):
        perimiter = self.getBoundingBoxPerimiter()
        #Walk along the perimiter
        offset = 0
        walls = []
        for bound_cell in perimiter:
            if self.fortress.isEmpty(bound_cell):
                #30% chance to shift the offset in/out by 1
                if roll(10) > 7:
                    if offset == 0:
                        if roll(2) == 1:
                            offset = -1
                    else:
                        offset = 0
                if bound_cell[0] == self.top_row:
                    self.fortress.setCellValue(bound_cell[0]+offset, bound_cell[1], [WALL_VALUE])
                    walls.append([bound_cell[0]+offset, bound_cell[1]])
                if bound_cell[0] == self.bottom_row:
                    self.fortress.setCellValue(bound_cell[0]-offset, bound_cell[1], [WALL_VALUE])
                    walls.append([bound_cell[0]-offset, bound_cell[1]])
                if bound_cell[1] == self.left_col:
                    self.fortress.setCellValue(bound_cell[0], bound_cell[1]+offset, [WALL_VALUE])
                    walls.append([bound_cell[0], bound_cell[1]+offset])
                if bound_cell[1] == self.right_col:
                    self.fortress.setCellValue(bound_cell[0], bound_cell[1]-offset, [WALL_VALUE])
                    walls.append([bound_cell[0], bound_cell[1]-offset])
            else:
                walls.append([bound_cell[0], bound_cell[1]])
        self.printBoard(self.fortress.board)
        last_wall = walls[-1]
        temp_wall = []
        for wall in walls:
            distance = abs(last_wall[0]-wall[0]) + abs(last_wall[1]-wall[1])
            if distance > 1:
                walls_needed = math.ceil(distance/2.0)
                for ii in range(walls_needed):
                    if (wall[0] != last_wall[0] and wall[1] != last_wall[1]):
                        #If we're a gate, we need special conditions to ensure we don't get blocked
                        if self.fortress.board[wall[0]][wall[1]] != [WALL_VALUE]:
                            if wall[0] == self.top_row or wall[0] == self.bottom_row:
                                if last_wall[1] > wall[1]:
                                    self.fortress.setCellValue(wall[0], wall[1]+1, [WALL_VALUE])
                                    last_wall = [wall[0], wall[1]+1]
                                else:
                                    self.fortress.setCellValue(wall[0], wall[1]-1, [WALL_VALUE])
                                    last_wall = [wall[0], wall[1]-1]
                            elif wall[1] == self.left_col or wall[1] == self.right_col:
                                if last_wall[0] > wall[0]:
                                    self.fortress.setCellValue(wall[0]+1, wall[1], [WALL_VALUE])
                                    last_wall = [wall[0]+1, wall[1]]
                                else:
                                    self.fortress.setCellValue(wall[0]-1, wall[1], [WALL_VALUE])
                                    last_wall = [wall[0]-1, wall[1]]
                            temp_wall = wall
                            wall = last_wall                        
                        elif last_wall[0] == self.left_col or last_wall[0] == self.right_col:
                            if wall[0] > last_wall[0]:
                                self.fortress.setCellValue(last_wall[0]+1, last_wall[1], [WALL_VALUE])
                                last_wall = [last_wall[0]+1, last_wall[1]]
                            elif wall[0] < last_wall[0]:
                                self.fortress.setCellValue(last_wall[0]-1, last_wall[1], [WALL_VALUE])
                                last_wall = [last_wall[0]-1, last_wall[1]]
                        else:
                            if wall[1] > last_wall[1]:
                                self.fortress.setCellValue(last_wall[0], last_wall[1]+1, [WALL_VALUE])
                                last_wall = [last_wall[0], last_wall[1]+1]
                            elif wall[1] < last_wall[1]:
                                self.fortress.setCellValue(last_wall[0], last_wall[1]-1, [WALL_VALUE])
                                last_wall = [last_wall[0], last_wall[1]-1]
            if temp_wall != []:
                last_wall = temp_wall
                temp_wall = []
            else:
                last_wall = wall

        self.printBoard(self.fortress.board)
    def __init__(self):
        WALL_VALUE = 'x'
        self.setEntranceMax()
        self.fortress = self.FortressBoard()
        #self.printBoard()

        #Step #1: CPU info (p164)
        self.CPUs = roll(6)
        self.memory = {}
        for memory_slot in range(4*self.CPUs):
            self.memory[memory_slot] = []
        self.placeCPUsAndMemory()
        self.code_gates = self.CPUs
        self.terminal = self.CPUs
        self.intelligence = 3*self.CPUs 
        self.personality = ""
        self.reaction = ""
        self.ICON = ""

        self.setBoundingBox()
        self.setEntrances()
        self.addWalls()

        self.ALL_SKILLS = ["Accounting", "Anthropology", "Botany", "Chemistry", "Composition", "Cryotank Operation",
                       "Diagnose Illness", "Driving", "Education & General Knowledge", "Gamble", "Geology",
                       "Heavy Weapons (as a mounted weapon)", "History.", "Language", "Library Search", "Mathematics",
                       "Operate Hvy. Machinery", "Paint or Draw", "Pharmaceuticals", "Physics", "Pilot",
                       "Play Instrument (if electronic)", "Programming", "Rifle (as a mounted weapon)", "Stock Market",
                       "Submachinegun (as a mounted weapon)", "System Knowledge", "Teaching", "Zoology"]
        
        #Step #2: Wall Strength (p164)
        self.wall_strength = roll(6) + round(self.CPUs/2.0)
        self.fortress.board_legend[WALL_VALUE] = "A Data Wall (Strength=%s)" %self.wall_strength

        #Step #3: Code Gate Strength (p164)
        self.code_gate_strength = roll(6) + round(self.CPUs/2.0)

        #Step #4: 5 Skills (p164, and skill list from p157)
        self.skills = {}
        for ii in range(5):
            index = random.randint(0,len(self.ALL_SKILLS)-1)
            self.skills[self.ALL_SKILLS[index]] = roll(6)+4

        #Step #5: Types of files (p164)
        for ii in range(2*len(self.memory.keys())):
            file = self.getFile()
            memory_unit = random.randint(0,len(self.memory.keys())-1)
            self.memory[memory_unit].append(file)
        
        #Step #6 Virtuals (p164)
        self.virtuals = []
        if roll(3) == 3:
            self.virtuals.append(self.getVirtual())
        
        #Step#7
        self.defenses = []
        for ii in range(roll(6)+self.CPUs):
            self.defenses.append(self.getDefense())

        #Step #8 Remotes
        self.remotes = []
        for ii in range(roll(6)):
            self.remotes.append(self.getRemote())

newFort = DataFortress()                                                                                                                                              