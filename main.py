# CS30 Final Project
# Version 2: Map + Player Movement 

rooms = {
  "Lobby": {
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
      "exits": {}
      "type": "exit"
  }
}

current_room = "Lobby"


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
        move = input("\nMove (north/south/east/west) or quit: ").lower()

        if move == "quit": 
            return "quit"

        if move in ["north", "south", "east", "west"]: 
            return move 

        print("Invalid input. Try again.")


def move_player(room_name, direction): 
    room = rooms[room_name]

    if direction in room["exits"]: 
        return room["exits"][direction]

    print("You can't go that way.")
    return room_name 

While True: 
    show_room(current_room)

    if rooms[current_room]["type"] == "exit": 
        print("\nYou reached the exit!")
        break

    choice = get_move()

    if choice == "quit": 
        print("You quit the game")
        break

    current_room = move_player(current_room, choice)












      









