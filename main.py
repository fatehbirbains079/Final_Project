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












