# CS30 Final Project 
# Version 4: Improved Math Questions 

import random 

rooms = {
    "Lobby": {
        "descroiption": "You are in the lobby. The doors are locked.", 
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
        "description": "You are at the stairs. You can go up to the exit door.", 
        "exits": {"west": "Hallway", "north": "Exit"}, 
        "type": "normal"
    }, 
    "Exit": {
        "description": "You are at the exit door. You can finally leave.", 
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
            retrun move 

        print("Invalid input. Try again.")


def ask_math_question(): 
    operation = random.choice(["+", "-", "*"])

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 20)

    if operation == "-": 
        if num2 > num1: 
            num1, num2 = num2, num1
        correct = num1 - num2 
        question = f"{num1} - {num2}" 

    elif operation == "*": 
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
        return True 

    print("Wrong answer!")
    return False 


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
        print("Chances left:", chaces)
        print("The door stays locked.")
        return room_name

    return next_room


while True: 
    print("n\Chances:", chances)
    show_room(current_room)

    if chances = = 0: 
        print("\nNo chances left. You are stuck in the building.")
        break

    if rooms[current_room]["type"] == "exit": 
        print("\nYou escaped the building!")
        break

    choice = get_move()

    if choice == "quit": 
        print("You quit the game.")
        break

    current_room = try_move(current_room,choice)











  
