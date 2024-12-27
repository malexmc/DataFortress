import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os, sys

OUT_DIR = os.path.dirname(os.path.realpath(__file__))
if getattr(sys, 'frozen', False):
    OUT_DIR = os.path.dirname(sys.executable)

class ImageDrawer():

    def drawSquare(self, point1, point2, color, square_text, image_handle):
        point1_grid = (point1[0] * 100, point1[1] * 100)
        point2_grid = (point2[0] * 100, point2[1] * 100)
        fnt = ImageFont.load_default(size=40)
        draw = ImageDraw.Draw(image_handle)
        draw.rectangle((point1_grid[0], point1_grid[1],point2_grid[0], point2_grid[1]), fill=color, outline=(1, 1, 1, 255))
        if square_text != "---":
            draw.text((point1_grid[0]+7, point1_grid[1]+25), text=square_text, font=fnt,fill=(255,255,255,color[3]), outline=(1, 1, 1, 255))
        #draw.line((point1_grid[0], point1_grid[1], point2_grid[0], point1_grid[1]), fill=(1, 1, 1, 255)) #Top Line
        #draw.line((point1_grid[0], point1_grid[1], point1_grid[0], point2_grid[1]), fill=(1, 1, 1, 255)) #Left Line
        #draw.line((point2_grid[0], point1_grid[1], point2_grid[0], point2_grid[1]), fill=(1, 1, 1, 255)) #Right Line
        #draw.line((point1_grid[0], point2_grid[1], point2_grid[0], point2_grid[1]), fill=(1, 1, 1, 255)) #Bottom Line
        #draw.line()

    def __init__(self, board_map):
        image_location = OUT_DIR + '\\fortress_overlay.png'
        Image.new('RGBA', (2000, 2000), color = (255,255,255,0)).save(image_location)
        with Image.open(image_location) as im:
            for point_key in board_map.keys():

                draw = ImageDraw.Draw(im)
                #draw.line((0,0, 100, 100), fill=128)
                color = (1, 1, 1, 255)
                if "G" in board_map[point_key][0]:
                    color = (128,128,1,255)
                if "C" in board_map[point_key][0]:
                    color = (1,1,128,255)                    
                if "M" in board_map[point_key][0]:
                    color = (1,128,1,255)
                if "R" in board_map[point_key][0]:
                    color = (128,1,128,255)
                if "D" in board_map[point_key][0]:
                    color = (225,1,1,255)
                if board_map[point_key] == 'b':
                    color = (255,255,255,0)
                self.drawSquare(point_key, (point_key[0] + 1, point_key[1] + 1), color, board_map[point_key][0], im)
                #self.drawSquare((1,1), (2,2), (255, 1, 1, 255), im)
                #point_print = (0,0)
                #draw.line((0, im.size[1], im.size[0], 0), fill=128)

            # write to stdout
            im.save(image_location)
