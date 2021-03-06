from pymclevel import alphaMaterials, MCSchematic, MCLevel, BoundingBox
from mcplatform import *
import numpy as np
import random as rand
from TempHouse import TempHouse

wool_floor          = 171
water_block         = 9
cobblestone         = 4
oak_wood_plants     = 5
glass_block         = 20
white_wool          = 35
oak_fence           = 85
red_bed             = 26
furnace             = 62
cake                = 92

walkable_blocks = [1, 2, 3, 5, 12, 13]
directions = {0: "North", 1: "East", 2: "South", 3: "West"}

road_blocks = [(2,0), (98,1), (13,0), (98,2), (4,0), (44,3), (44,5), (3,2), (3,0)]

#Sets block with level (i.e 171:3 for light blue wool carpet)
def set_block_with_level(level, x, y, z, blockID, blockIDLevel):
    if blockID != -1:
        level.setBlockAt(x, y, z, blockID)
        level.setBlockDataAt(x, y, z, blockIDLevel)

def build_temp_house(level, origin):
    th = TempHouse()
    bp = th.get_blueprint()
    origin = origin.get_chunk()
    origin = origin[0]
    for y in range(0, len(bp)):
        for x in range(0, len(bp[y])):
            for z in range(0, len(bp[y][x])):
                #Analyze the box inwhich to build the house, to find the floor block with the maxy and the one with the miny
                #This is to properly generate a platform onwhich the house is built
                set_block_with_level(level, origin[0] + x, origin[1] + y, origin[2] + z, (bp[y][x][z])[0], (bp[y][x][z])[1]) 

def build_support_from(level, inity, structure_location):
    for loc in structure_location:
        height = 0
        while level.blockAt(loc[0], inity - height, loc[1]) not in walkable_blocks:
            set_block_with_level(level, loc[0], inity - height, loc[1], cobblestone, 0)
            height += 1

def get_floor_block_id():
    return wool_floor

def get_road_block_id():
    return road_blocks[int(rand.normalvariate(4, 2)) % len(road_blocks)]