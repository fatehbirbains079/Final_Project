#CS30 Final Project 
#Version 6: Difficulty Option 

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
        "type": "normal"
    }, 
    "Office": {
        "description": "You are in an Office. There is a keypad on the door.",
        "exits": {"south": "Hallway"}, 
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
        "description": "You are on the second floor hallway. It is colder here.", 
        "exits": {"south": "Strairs Down", "east": "Security Room", "west": "Break Room"}, 
        "type": "normal"
    }, 
    "Stairs Down"
        "description": "You are at the stairs going back down.", 
        "exits": {"north": "Second Hallway", "south": "Hallway"}, 
        "type": "normal"        
    }, 
    "Break Room": {
        "description": "You are in the break room. Nothing useful here.", 
        "exits": {"east": "Second Hallway"}, 
        "type": "math"
    }, 
    "Rooftop Exit": {
        "description": "You reached the rooftop exit door. You can finally leave!", 
        "exits": {}
        "type": "exit"    
    }
} 

current_room = "Lobby"
chances = 3 
difficulty = "easy"


def pick_difficulty(): 
    while True: 
        choice = input("Choose difficulty (easy/medium/hard): ").lower()
        if choice in ["easy", "medium", "hard"]: 
            return choice 
        print("Invalid choice. Try again.")


def number_range(): 
    if difficulty == "easy"
        return 1, 10 
    if difficulty == "medium"
        return 5, 20 
    return 10, 30 


def operations_list(): 
    if difficulty == "hard": 
        return ["+", "-", "*", "*"]
    return ["+", "-", "*"]


def show_room(room_name): 
    room = rooms[room_name]
    print("\nRoom:", room_name)






        






      
  
