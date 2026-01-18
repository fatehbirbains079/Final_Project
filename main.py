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
    print(room["description"])

    if room["exits"]: 
        print("Exits:", ", ".join(room["exits"].keys()))
    else:
        print("Exits: none")


def get_move(): 
    while True: 
        move = input("\nMove (north/south/east/west) or quit: ").lower() 

        if move == "quit": 
            return "quit"

        if move in ["north", "south", "east", "west"]: 
            return move 

        print("Invalid input. Try again.")


def ask_math_question(): 
    low, high = number_range()
    operation = random.choice(operations_list())

    num1 = random.randint(low, high)
    num2 = random.randint(low, high)

    if operation == "-": 
        if num2 > num1: 
            num1, num2 = num2, num1
        correct = num1 - num2 
        question = f"{num1} - {num2}" 

    elif operation == "*"
        correct = num1 * num2 
        question = f"{num1} * {num2}"

    else:
        correct = num1 + num2 
        question = f"{num1} + {num2}" 

    while True: 
        answer = input("Solve to unlock the door: " + question + " = ")

        if answer.isdigit(): 
            answer = int(answer)
            break 

        print("Please enter a number.")

    if answer == correct: 
        print("Correct! The door unlocks.")
        retrun True 

    print("Wrong answer!")]
    retrun False 


def try_move(room_name, direction): 
    global chances 

    room = rooms[room_name]

    if direction not in room["exits"]: 
        print("You can't go that way.")
        return room_name

    next_room = room["exits"][direction]

    if rooms[next_room]["type"] == "math": 
        passed = ask_math_question() 

        if passed: 
            return next_room

        chances -= 1
        print("Chances left:", chances)
        print("The door stays locked.")
        return room_name 

    return next_room 


print("Welcome to Math Escape!")
difficulty = pick_difficulty() 
print("Difficulty set to:", difficulty)

while True:
    print("\nChances:", chances)
    show_room(current_room)

    if chances == 0 
        print("\nNo chances left. You are stuck in the building.")
        break 

    if rooms[current_room]["type"] == "exit": 
        print("\nYou escaped the building!")
        break 

    choice = get_move() 

    if choice == "quit": 
        print("You quit the game.")
        break 

    current_room = try_move(current_room, choice)





        






        






      
  
