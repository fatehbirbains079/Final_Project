# CS30 Final Project 
# Version 7: Add Enemy 

import random 

rooms = { 
    "Lobby": { 
        "description": "You are in the lobby. The doors are locked.", 
        "exits": {"east": "Hallway"}, 
        "type": "start"
    }, 
    "Hallway": {
        "description": "You are in a hallway. It is quiet and dark.", 
        "exits": {"west": "Lobby", "north": "Office", "east": "Storage", "south": "Stairs Up"}, 
        "type": "math"
    }, 
    "Storage": {
        "description": "You are in a storage room. Boxes are everywhere.", 
        "exits": {"west": "Hallway"}, 
        "type": "normal"
    }, 
    "Stairs Up": {
        "description": "You are at the stairs going up to the second floor.",
        "exits": {"north": "Second Hallway"}, 
        "type": "normal"
    }, 
    "Second Hallway": { 
        "description": "You are on the second flooor "
