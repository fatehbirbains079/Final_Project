# CS30 Final Project 
# Version 5: Enlarge Game (More Rooms + Another Floor)

import random 

rooms = {
    "Lobby": {
          "description": "You are in the lobby. The doors are locked.", 
          "exits": {"east": "Hallway"}, 
          "type": "start"
    }, 
    "Hallway": {
        "descroiption": "You are in a hallway. It is quiet and dark.", 
        "exits": {"west": "Lobby", "north": "Office", "east": "Storage", "south": "Stairs Up"}, 
        "type": "normal"
    }, 
    "Office"" { 
        "description": "You are in an office. There is a keypad on the door.", 
        "exits": {"south": "Hallway"}, 
        "type": "math"  
    },
    "Storage": {
        "description": "You are in a storage room. Boxes are everywhere.", 
        "exits": {"west": "Hallway"}, 
        "type": "normal"
    }, 
    "Stairs "
