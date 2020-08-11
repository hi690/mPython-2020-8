# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:02:09 2020

@author: user
"""

from mcpi.minecraft import Minecraft 
import time
mc=Minecraft.create()
while True:
    x,y,z=mc.player.getPos()
    mc.setBlock(x,y,z,38)
    time.sleep