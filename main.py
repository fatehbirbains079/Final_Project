# CS30 Final Project 
# Version 1: Map (Rooms)

rooms = {
  "Lobby": {
    "description": "You are in the lobby. The doors are locked.", 
    "exits": {"east": "Hallway"}, 
    "type": "start"
  },
  "Hallway": {
    "decription": "You are in the hallway. It is quiet and dark.",
    "exits": {"west": "Lobby", "north": "Office", ""east}: "Stairs"}, 
    "type": "normal"
  },
  "Office": {
      "decription": ""You are in an office. There is a keypad on the door.", 
      "exits": {"south": "Hallway"}, 
      "type": "math"
  }, 
  "Stairs": {
      "description": "You are at the stairs. You can go up to the exit door.",
      "exits": {"west": "Hallway", "north": ""Exits}, 
      "type": "normal"
  }, 
  "Exit": {
      "description": "You are at the exit door. You can finally leave.", 
              
