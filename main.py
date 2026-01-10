# CS30 Final Project 
# Version 3: Movement + 3 Chances + Math Rooms 

import random 

rooms = {
    "Lobby": "{ 
        "description": "You are in the lobby. The doors are locked.", 
        "exits": {"west": "Lobby", "north": "Office", "east": "Stairs"}, 
