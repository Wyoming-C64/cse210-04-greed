# cse210-04-Greed

__The Game of Greed__  
_He who is not contented with what he has,_  
_would not be contented with what he would like to have._  
_- Socrates -_

## Overview
Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

## Rules
Greed is played with the following rules:

- Gems (*) and rocks (o) randomly appear and fall from the top of the screen.
- The player (#) can move left or right along the bottom of the screen.
- If the player touches a gem they earn a point.
- If the player touches a rock they lose a point.
- Gems and rocks are removed when the player touches them.
- The game continues until the player closes the window.

## Getting Started
Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command.

python3 greed or py greed
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the dice folder and click the "run" button.

## Project Structure
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- greed               (source code for game)
  +-- game              (specific classes)
    +-- casting         (classes who are used to make the interactable objects in the game)
    +-- directing       (classes who direct the sequence of play)
    +-- services        (classes that provide input and output from monitor and keyboard)
    +-- shared          (classes who are used to manage attributes in other classes)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies
Python 3.8.0

## Authors
- Spencer Bell (bel21032@byui.edu)
- Dallas Eaton (deaton879@byui.edu)
- David Kikiani (davidkikiani@mail.com)
- Julian Hernandez (hernandezjuliang44@gmail.com)
- Mike Lewis (wyoming.c64@gmail.com)
- Jaden McCarrey (jadenmccarrey@gmail.com)