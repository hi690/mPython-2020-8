# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:13:35 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getPos()
mc.setSign(x,y,z,63,0,'minecraft','minecraft','minecraft','minecraft')