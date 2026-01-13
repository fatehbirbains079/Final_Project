# CS30 Final Project 
# Version 3: Movement + 3 Chances + Math Rooms 

import random 

rooms = {
    "Lobby": "{ 
        "description": "You are in the lobby. The doors are locked.", 
        "exits": {"east": "Hallway"}, 
        "type": "start"
    }, 
    "Hallway": {
        "description": "You are in a hallway. It is quiet and dark.", 
        "exits": {"west": "Lobby", "north": "Office", "east": "Stairs"}, 
        "type": "normal"
    }, 
    "Office": {
        "description": "You are in an office. There is a keypad on the door.", 
        "exits": {"south": "Hallway"}, 
        "type": "math" 
    }, 
    "Stairs": {
        "description": "You are at the stairs. You can go ",
        "exits": {}
        "type": "normal" 
    }, 
    "Exit": {
        "description": "You are at the stairs. You can go up to the exit door.",
        "exits": {}, 
        "type": "exit"
    }
}

current_room = "Lobby"
chances = 3


def show_room(room_name): 
    room = rooms[room_name]
    print("\nRoom:", room_name)
    print













    
    
