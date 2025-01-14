import random
import math
import numpy as np
from ImageDrawer import ImageDrawer
import tkinter as tk
from tkinter import *
import os, sys
from Utils import *
import json
from Remote import *
from Skill import *
from Defense import *
from CPU import *
from Memory import *
from DataWall import *
from CodeGate import *
import string
from wonderwords import RandomWord

WALL_VALUE = '---'
BLANK_VALUE = '   '
PERIPHERAL_VALUE = "P"
DEFENSE_VALUE = "D"
CODE_GATE_VALUE = "G"
CPU_MAX_DISTANCE = 3
OUT_DIR = os.path.dirname(os.path.realpath(__file__))
if getattr(sys, 'frozen', False):
    OUT_DIR = os.path.dirname(sys.executable)

class DataFortress():
   
    def createUI(self):
        # Top level window 
        frame = tk.Tk() 
        frame.title("Data Fortress Parameters") 
        frame.geometry('1200x800')
        #frame.grid_rowconfigure(0, weight=1)
        #frame.grid_columnconfigure(0, weight=1)
        self.cputext_output = "" 
        self.item_field_count = 0
        self.current_row = 1
        self.memory_type_options = ["File", "Remote", "Defense"]
        self.memory_subtype_options = ["NA"]
        STARTING_ROW_COUNT = 20
        STARTING_COL_COUNT = 20
        
        # Frame for CPU widgets
        CPU_item_frame = tk.Frame(frame)
        CPU_item_frame.grid(row=1)
        CPU_item_frame.grid(column=1)

        # Frame for Memory Item widgets
        memory_item_frame = tk.Frame(frame)
        memory_item_frame.grid(row=2)

        memory_item_dict = {}


        # Function for getting Input 
        # from textbox and printing it  
        # at label widget 

        def submit_text():
            self.cputext_output = int(cputext_field.get(1.0, "end-1c"))
            self.rowstext_output = int(rowtext_field.get(1.0, "end-1c"))
            self.colstext_output = int(coltext_field.get(1.0, "end-1c"))

            for key in memory_item_dict.keys():
                memory_item = memory_item_dict[key]
                type_text = memory_item[1].get()
                subtype_text = memory_item[2].get()
                my_text = memory_item[0].cget("text")
                detail_text = memory_item[3].get(1.0, "end-1c")
                if  type_text == self.memory_type_options[0]: #File
                    self.files.append(detail_text)
                if type_text == self.memory_type_options[1]: #Remote
                    new_remote = Remote(name=subtype_text, subtype=REMOTE_TYPES[subtype_text])
                    self.remotes.append(new_remote)
                if type_text == self.memory_type_options[2]: #Defense
                    new_defense = Defense(subtype_text)
                    self.defenses.append(new_defense)
            
            frame.destroy()

        def add_memory_item_row():
            self.item_field_count += 1

            memory_label = tk.Label(memory_item_frame,
                            text="Memory Item " + str(self.item_field_count),
                            height = 1, 
                            width = 20)
            memory_label.grid(row=self.current_row, column=0)

            memory_type_selection = StringVar()
            memory_type_selection.set("File")
            memory_type = tk.OptionMenu(memory_item_frame, memory_type_selection, *self.memory_type_options)
            memory_type.grid(row=self.current_row, column=1)
            memory_type.configure(width=20)

            memory_subtype_selection = StringVar()
            memory_subtype_selection.set("")
            memory_subtype = tk.OptionMenu(memory_item_frame, memory_subtype_selection, *self.memory_subtype_options)
            memory_subtype.grid(row=self.current_row, column=2)
            memory_subtype.configure(width=20)      

            def memory_type_selection_callback(row_number):
                if memory_type_selection.get() == "File":
                    self.memory_subtype_options = ["NA"]
                if memory_type_selection.get() == "Remote":
                    self.memory_subtype_options = REMOTE_TYPES.list_names()
                if memory_type_selection.get() == "Defense":
                    self.memory_subtype_options = DEFENSE_TYPES.list_names()
                memory_subtype = tk.OptionMenu(memory_item_frame, memory_subtype_selection, *self.memory_subtype_options)
                memory_subtype.grid(row=row_number, column=2)
                memory_subtype.configure(width=20)  

            memory_type_selection.trace_add("write", lambda x, y, z, row_number=self.current_row: memory_type_selection_callback(row_number))        

            memory_name = tk.Text(memory_item_frame,
                                height = 2,
                                width = 10)
            memory_name.grid(row=self.current_row, column=3)
            memory_name.configure(width=20)

            memory_item_dict[self.current_row] = [memory_label, memory_type_selection, memory_subtype_selection, memory_name]

            self.current_row += 1
            
        #Submit button
        submit_button = tk.Button(frame, text="Submit", command=submit_text)
        submit_button.grid(row=0, column=0)
        CPU_item_frame.columnconfigure(0, weight=1)

        # CPU fields creation
        cputext_label = tk.Label(CPU_item_frame,
                        text="CPU Count (integer 1-6)",
                        height = 5, 
                        width = 25)
        cputext_label.grid(row=1, column=0, ipady=1)

        cputext_field = tk.Text(CPU_item_frame, 
                        height = 1, 
                        width = 20) 
        cputext_field.grid(row=1, column=1, ipady=1)
        
        # Board size creation
        rowtext_label = tk.Label(CPU_item_frame,
                        text="Board Rows Count (integer 10+)",
                        height = 5, 
                        width = 25)
        rowtext_label.grid(row=2, column=0)

        rowtext_field = tk.Text(CPU_item_frame, 
                        height = 1, 
                        width = 20)
        rowtext_field.insert(END, STARTING_ROW_COUNT)
        rowtext_field.grid(row=2, column=1)

        coltext_label = tk.Label(CPU_item_frame,
                        text="Board Columns Count (integer 10+)",
                        height = 5, 
                        width = 25)
        coltext_label.grid(row=3, column=0)

        coltext_field = tk.Text(CPU_item_frame, 
                        height = 1, 
                        width = 20)
        coltext_field.insert(END, STARTING_COL_COUNT)
        coltext_field.grid(row=3, column=1)
        
        add_item_button = tk.Button(memory_item_frame, text="Add Memory Item", command=add_memory_item_row)
        add_item_button.grid(row=0, column=0)


        frame.mainloop()
    
    def writeToJSON(self):
        with open(OUT_DIR + "\%s.json" % self.name, "w") as outfile:
            board_json = {}
            board_json["name"] = self.name
            board_json["rows"] = int(self.rowstext_output)
            board_json["columns"] = int(self.colstext_output)
            board_json["remotes"] = []
            board_json["skills"] = []
            board_json["defenses"] = []
            board_json["datawallStr"] = self.data_wall_strength
            board_json["cpu"] = self.CPU_count
            for ii in range(1, len(self.board)): # all elements will have an addToJSON method, so run them all in a batch
                for jj in range(1, len(self.board[1])):
                    current_cell = self.getBoardCell([ii, jj])
                    if current_cell is not None:
                        current_cell.addToJSON(board_json)
            for skill in self.skills:
                skill.addToJSON(board_json)
            outfile.write(json.dumps(board_json))

    def setBoardCell(self, cell, value):
        self.board[cell[0]][cell[1]] = value

    def getBoardCell(self, cell):
        return self.board[cell[0]][cell[1]]

    def makeRemotes(self):
        for ii in range(roll(6) - len(self.remotes)):
            self.remotes.append(Remote().rollRandomly())

    def setRemotes(self):
        for remote in self.remotes:
            if remote.coords not in self.inside_coords:
                remote_placed = False
                unckecked_coords = [coord for coord in self.inside_coords]
                while not remote_placed:
                    current_cell = random.choice(unckecked_coords)
                    if self.getBoardCell(current_cell) is None:
                        remote.coords = current_cell
                        self.setBoardCell(current_cell, remote)
                        remote_placed = True
                    else:
                        unckecked_coords.remove(current_cell)

    def makeDefenses(self):
        for ii in range(roll(6)+self.CPU_count-len(self.defenses)):
            self.defenses.append(Defense().rollRandomly())

    def setDefenses(self):
        for defense in self.defenses:
            if defense.coords not in self.inside_coords:
                defense_placed = False
                while not defense_placed:
                    current_cell = random.choice(self.inside_coords)
                    if self.getBoardCell(current_cell) is None:
                        defense.coords = current_cell
                        self.setBoardCell(current_cell, defense)
                        defense_placed = True

    def setSkills(self):
       for ii in range(5):
            new_skill =Skill().rollRandomly()
            skill_placed = False
            while not skill_placed:
                current_skills = [skill.key for skill in self.skills]
                if new_skill.key not in current_skills:
                    self.skills.append(Skill().rollRandomly())
                    skill_placed = True
                else:
                    new_skill.rollRandomly()
                

    def setFiles(self):
        for ii in range((8*self.CPU_count)-len(self.files) ):
            value = roll(6)
            if value == 1:
                self.files.append("Inter Office")
            elif value == 2:
                self.files.append("Database")
            elif value == 3:
                self.files.append("Business Records")
            elif value == 4:
                self.files.append("Financial Transactions")
            elif value == 5:
                self.files.append("Grey Ops")
            elif value == 6:
                self.files.append("Black Ops")

    def setBounds(self):
        needed_spaces = self.CPU_count*5
        needed_spaces += len(self.files)
        needed_spaces += len(self.defenses)
        needed_spaces += len(self.remotes)
        needed_spaces += len(self.skills)
        print("Spaces to accommodate: %s" % str(needed_spaces))

    def setCPUsAndMemory(self):
        #TODO Place CPUs around the center
        #Allow placement on any cell but outermost layer
        INTERNAL_OFFSET = 4
        valid_cell_indices  = []
        for ii in range(1+INTERNAL_OFFSET,len(self.board)-INTERNAL_OFFSET):
            for jj in range(1+INTERNAL_OFFSET,len(self.board[1])-INTERNAL_OFFSET):
                valid_cell_indices.append([ii,jj])

        cpus_placed = 0
        center_cell = [math.floor(len(self.board)/2), math.floor(len(self.board[1])/2)]
        cpu_first_spot = []
        while cpus_placed < self.CPU_count:
        #Allow placement on any cell but outermost layer
            cpu_cell = None
                #If we've placed a CPU, make sure others are within CPU_MAX_DISTANCE to aid clustering
            within_range = False
            while not within_range:
                cpu_cell = random.choice(valid_cell_indices)
                cpu_distance = math.pow(cpu_cell[0] - center_cell[0], 2) + math.pow(cpu_cell[1] - center_cell[1], 2)
                cpu_distance = math.sqrt(cpu_distance)
                #cpu_distance = abs(cpu_cell[0] - center_cell[0]) + abs(cpu_cell[1] - center_cell[1])
                if cpu_distance <= CPU_MAX_DISTANCE:
                        print("CPU_CELL: %s" % str(cpu_cell))
                        print("DISTANCE: %s" % str(cpu_distance))
                        within_range = True
            #Place CPUs and Memory
            if self.getBoardCell(cpu_cell) is None:
                current_CPU = CPU(name=cpus_placed, coords=cpu_cell)
                cpu_first_spot = cpu_cell
                self.CPUs.append(current_CPU)
                self.setBoardCell(cpu_cell, current_CPU)
                cpus_placed +=1
                current_memories = []
                while len(current_memories) < 4:
                    all_valid_spots = [memory for memory in current_memories]
                    all_valid_spots.append(current_CPU)
                    memory_placed = False
                    while not memory_placed:
                        target = random.choice(all_valid_spots)
                        target_neighbors = getAdjacentDict(target.coords, self)
                        shuffled_directions = [e for e in target_neighbors.keys()]
                        random.shuffle(shuffled_directions)
                        for direction in shuffled_directions:
                            if target_neighbors[direction]['value'] is None and target_neighbors[direction]['coords'] in valid_cell_indices:
                                memory = Memory(
                                                            name=len(current_memories),
                                                            CPU=current_CPU,
                                                            coords=target_neighbors[direction]['coords']
                                                          )
                                self.memory.append(memory)
                                self.setBoardCell(memory.coords, memory)
                                current_memories.append(memory)
                                memory_placed = True
                                break
        #Place all the files into memory
        for file in self.files:
            file_placed = False
            while not file_placed:
                selected_memory = random.choice(self.memory)
                if selected_memory.memory_remaining > 0:
                    if selected_memory.contents is None:
                        selected_memory.contents = file
                    else:
                        selected_memory.contents += ", %s" % file
                    file_placed = True
    def setBoundsAndInsideSpaces(self):
        '''Once CPUs and memory are placed, create a "bounding box".
        This will represent the outermost inside perimiter before walls can be placed.'''

        #Find the minimum bounds. Start these opposite of intended
        self.top_bound = len(self.board[1])
        self.bottom_bound = 0
        self.left_bound = len(self.board)
        self.right_bound = 0
        for col in range(1, len(self.board)):
            for row in range(1, len(self.board[1])):
                current_cell = [col,row]
                if self.getBoardCell(current_cell) == None:
                    continue
                current_col = current_cell[0]
                current_row = current_cell[1]
                if current_row < self.top_bound:
                    self.top_bound = current_row
                if current_row > self.bottom_bound:
                    self.bottom_bound = current_row
                if current_col < self.left_bound:
                    self.left_bound = current_col
                if current_col > self.right_bound:
                    self.right_bound = current_col

        #Make sure the bounds have enough room for everyone. This alrogithm can be improved later

        inside_space_count = (self.bottom_bound-self.top_bound) * (self.right_bound-self.left_bound)
        required_space_count = (self.CPU_count*5) + len(self.remotes) + len(self.defenses) + 5 #This is not calculating right, so buffer by 5

        def getDistanceFromEdge(direction):
            if direction == DIRECTIONS.LEFT:
                return self.left_bound
            elif direction == DIRECTIONS.RIGHT:
                return len(self.board) - self.right_bound
            elif direction == DIRECTIONS.UP:
                return self.top_bound
            elif direction == DIRECTIONS.DOWN:
                return len(self.board[1]) - self.bottom_bound
        
        while inside_space_count < required_space_count:
            random_directions = DIRECTIONS.list_names()
            direction_text = random_directions[0]
            furthest_direction_from_edge = DIRECTIONS[direction_text]
            random_directions.remove(direction_text)
            while len(random_directions) > 0:
                direction_text = random.choice(random_directions)
                next_direction = DIRECTIONS[direction_text]
                next_distance = getDistanceFromEdge(next_direction)
                random_directions.remove(direction_text)
                if next_distance > getDistanceFromEdge(furthest_direction_from_edge):
                    furthest_direction_from_edge = next_direction
            
            if furthest_direction_from_edge == DIRECTIONS.LEFT:
                self.left_bound -= 1
            elif furthest_direction_from_edge == DIRECTIONS.RIGHT:
                self.right_bound += 1
            elif furthest_direction_from_edge == DIRECTIONS.UP:
                self.top_bound -= 1
            elif furthest_direction_from_edge == DIRECTIONS.DOWN:
                self.bottom_bound += 1

            top_to_bottom = self.bottom_bound-self.top_bound
            left_to_right = self.right_bound-self.left_bound
            inside_space_count = top_to_bottom * left_to_right

        self.inside_coords = []
        for col in range(self.left_bound, self.right_bound):
            for row in range(self.top_bound, self.bottom_bound):
                self.inside_coords.append([col,row])

    def setWallsAndGates(self):
        '''Place walls around the outside of the bounding box'''
        def updateOffset(offset):
            current_roll = roll(10)
            if current_roll <= 3:
                if offset == 0:
                    current_roll = roll(2)
                    if current_roll == 1:
                        offset = 1
                    else:
                        offset = -1
                else:
                    offset = 0
            return offset
        
        wall_box = [] #The "default" cells for all walls
        for col in range(self.left_bound-2, self.right_bound+2): #Top Row
            wall_box.append([col, self.top_bound-2])
        for row in range(self.top_bound-2, self.bottom_bound+2): #set offset for top at -1 since we placed -2 in the last batch
            wall_box.append([self.right_bound+2, row])
        for col in range(self.right_bound+2, self.left_bound-2, -1):
            wall_box.append([col, self.bottom_bound+2])
        for row in range(self.bottom_bound+2, self.top_bound-2, -1):
            wall_box.append([self.left_bound-2, row])
        banana = "pine"
        #TODO: Use wall box to go through wall placement algorithm
        offset = 0
        wall_list = []
        for wall_coords in wall_box:
            #If we aren't a corner...
            if not ((wall_coords[0] == self.left_bound-2 ^ wall_coords[0] == self.right_bound+2) and (wall_coords[1] == self.top_bound-2 ^ wall_coords[1] == self.bottom_bound+2)):
                #offset things as needed
                if wall_coords[1] == self.top_bound-2:
                    wall_coords[1] += offset
                elif wall_coords[1] == self.bottom_bound+2:
                    wall_coords[1] += offset
                elif wall_coords[0] == self.left_bound-2:
                    wall_coords[0] += offset
                elif wall_coords[0] == self.right_bound+2:
                    wall_coords[0] += offset
                offset = updateOffset(offset)
            else:
                offset = 0

            wall = DataWall(str=self.data_wall_strength, coords=wall_coords)
            self.setBoardCell(wall_coords, wall)
            wall_list.append(wall)
            
        for ii in range(self.CPU_count):
            gate_placed = False
            while not gate_placed:
                wall = random.choice(wall_list)
                if not ((wall.coords[0] == self.left_bound-2 ^ wall.coords[0] == self.right_bound+2) and (wall.coords[1] == self.top_bound-2 ^ wall.coords[1] == self.bottom_bound+2)):
                    gate_coords = wall.coords
                    gate = CodeGate(cpu_count=self.CPU_count, coords=gate_coords)
                    self.setBoardCell(gate_coords, gate)
                    wall_list.remove(wall)
                    gate_placed = True

        #Make Inner Walls
        for coords in self.inside_coords:
            if self.getBoardCell(coords) is None:
                wall_chance = percentChance(25)
                for neighbor_coords in getAdjacentList(coords, self):
                    if type(self.getBoardCell(neighbor_coords)) is DataWall:
                        wall_chance = percentChance(40)
                        break
                if wall_chance == 1:
                    wall = DataWall(str=self.data_wall_strength, coords=coords)
                    self.setBoardCell(coords, wall)

    def id_generator(self, size=4, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    
    def makeName(self):
        rw = RandomWord()
        return rw.word() + "_" + rw.word() + "_" + self.id_generator()
        # words = roll(3)
        # rw = RandomWord()
        # if words == 1:
        #     return rw.word() + "_" + self.id_generator()
        # if words == 2:
        #     return rw.word() + "_" + rw.word() + "_" + self.id_generator()
        #if words == 3:
        #    return rw.word() + "_" + rw.word() + "_" + rw.word() + "_" + self.id_generator()

    def __init__(self):
        self.name = self.makeName()
        self.board = {}
        self.CPUs = []
        self.memory = []
        self.files = []
        self.defenses = []
        self.remotes = []
        self.skills = []
        ui_input = self.createUI()

        for ii in range(1, self.rowstext_output+1):
            self.board[ii] = {}
            for jj in range(1, self.colstext_output+1):
                self.board[ii][jj] = None

        self.CPU_count = int(self.cputext_output)
        self.data_wall_strength = math.floor(roll(6)/2) + self.CPU_count
        self.setFiles()
        self.setCPUsAndMemory()
        self.makeRemotes()
        self.makeDefenses()
        self.setBoundsAndInsideSpaces()
        self.setWallsAndGates()
        self.setDefenses()
        self.setRemotes()
        self.setSkills()

print(REMOTE_TYPES.list_names())
fortress = DataFortress()
fortress.writeToJSON()