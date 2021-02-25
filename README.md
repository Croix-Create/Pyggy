### Pyggy
This was Croix-Create's second capstone project for Python. It's purpose was to teach a familiarity towards libraries and the learning of them. This particular library is Pygame, a well documented coding library for creating games. This was the very first game Croix-Create, well, created.

## The Theme
The theme of the game was inspired by Monty Python's The Holy Grail. A fitting inspiration, considering where Monty Python's namesake comes from. You play as a picture of a pig, who must dodge the spooky skeletons and get to the Holy Grail to win.

## The Objective
The objective of the project was to allow the player to move left, right, up and down while there are enemy objects accelerating towards the player obejct. A prize object had to be created as a requirement to win the game. Hitboxes had to be createed to allow for interactivity.

## The How
At first the code initialises Pygame and declares the width and height of the player screen. Next the code loads the images for the hero (the player), the enemies and the Holy Grail. Next, the code sets the size of the game objects. Variables are created and the width and height of the game objects are assigned to these variables.
The spawn locations of the interacting game objects are set next.
At this point the code creates a while loop to run the game. Once the while loop is active the code 'blits' or spawns the game objects.
Next a for loop is created to loop through occurrences in the game. Inside this for loop the code for player movement reisdes. The loop checks if the player quits or if they have pressed they keys 'a', 'w', 's', 'd'. If either of these keys are pressed within the game environment the player will be moved by 50 units.
