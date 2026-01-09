 # Development Work (CS30 Final Project)

 # Project Name 
 Math Escape Game (3 Chances)

 # What the program will do 
 The player is trapped in a building. To escape they must answer the math questions correctly. The player has 3 chances (3 lives). If they use all their chances, they will losse and if they finish all the questions before chances hit 0, they will win. 

 # Plan (Versions)

 # Version 1: Make a Map (Rooms)
Goal: Create a simple building map using a data structure. 
- Use a dictionary to store all the rooms 
- Each room will have: 
    - description 
    - esits (north/south/east/west)
    - type of a room (normal, math door, exit)

# Version 2 (Make Player Movement) 
Goal: Let the player move on the map using the commands. 
- Player use data structure starts from the starting room (example: Lobby)
- Show current room descroiption and available directions 
- Ask user: "north / south / east / west / quit"
- Check if the direction if valid or not: 
    - If valid: move the player to new room  
    - If not: print "you can't go that way" and ask again

# Version 3: Add 3 Chances System 
Goal: Some rooms are required a math question to pass. 
- If player enters a room with type = "Math": 
    - Ask 1 math question to unlock that room/door
    - If correct: allow movement normally 
    - If wrong: substract a chance and keep the plater in the same room (or close the exit)

# Version 4: Improve Questions
Goal: Have the math question generate during the game.

# Version 5: Enlarge Game
Goal: Add another floor to my building.

# Version 6: Add more Dificulty 
Goal: Add more complexity to the math question.
Possibly add an option for the player to pick the dificulty.

# Version 7: Add Enemy
Goal: Add a enemy that walk around the map. If caought the plater will go back to start.
Extention: create a person class and make the player and the ememy child classes.


TimeLine:
