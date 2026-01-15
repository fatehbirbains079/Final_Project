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
    "Stairs Up": {
        "description": "You are at the stairs going up to the second floor.", 
        "exits": {"north": "Second Hallway", "northwest": "Second Hallway"}, 
        "type": "normal"
    }, 
    "Second Hallway": {
        "description": "You are at the stairs going back down.", 
        "exits": {"south": "Stairs Down", "east": "Security Room", "west": "Break Room"}, 
        "type": "normal"
    }, 
    "Stairs Down": {
        "description": "You are in the break room. Nothing useful here.", 
        "exits": {"north": "Second Hallway", "south": "Hallway"}, 
        "type": "normal"
    }, 
    "Break Room": {
        "description": "You are in the break room. Nothing useful here.", 
        "exits": {"west": "Second Hallway", "north": "Rooftop Exit"}, 
        "type": "normal"
    }, 
    "Security Room": { 
        "description": "You are in the security room. The exit is here.",
        "exits": {"west": "Second Hallway", "north: "Rooftop Exit"}, 
        "type": "math"
    }
}

current_room = "Lobby"
chances = 3


def show_room(room_name): 
    room = rooms[room_name]
    print("\nRoom:", room_name)
    print(room["description"])

    if room["exits"]: 
        print("Exits:", ", ".join(room["exits"].keys()))
    else:
        print("Exits:none")

def get_move(): 
    while True:
        move = input("\nMove (north/south/east/west) or quit: ").lower() 

        if move == "quit": 
            return "quit" 

        if move in ["north", "south", "east", "west"]: 
            return move 

        print("Invalid input. Try again.")


def ask_math_question(): 
    operation = random.choice(["+", "-", "*"])

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    if operation == "-": 
        if num1, num2 = num2, num1 
    correct = num1 - num2 
    question = f"{num1} * {num2}" 

    elif operation 
