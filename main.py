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
    print(room["description"])

    exits = room["exits"].keys()
    if len(room["exits"]) == 0: 
            print("Exits: none")
    else: 
        print("Exits:", ", ".join(exits))

def get_move(): 
    while True: 
        move = input("\nMove (north/south/east/west) or quit:").lower()

        if move == "quit"
            return "quit"

        if move in ["north", "south", "east", "west"]: 
            return move 

        print("Invalid input. Try again.")


    def ask_math_questions(): 
        num1 = random.randint(1, 10)
        num2 = random.randint(1. 10)
        correct = num1 + num2 

        while True: 
            answer = input(f"Solve to unlock the door: {num1} + {num2} = ")
            












    
    
