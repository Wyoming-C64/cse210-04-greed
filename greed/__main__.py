import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
CELL_SIZE = 20
FONT_SIZE = CELL_SIZE
COLS = 60
ROWS = 40
MAX_X = CELL_SIZE * COLS 
MAX_Y = CELL_SIZE * ROWS
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40

def main():
    
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y - CELL_SIZE)
    position = Point(x, y)

    player = Actor()
    player.set_text("☺")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("players", player)
    
    # create the artifacts
    with open(DATA_PATH) as file:
        data = file.read()
        messages = data.splitlines()

    plot_list = []

    for n in range(DEFAULT_ARTIFACTS):
        
        # message = messages[n]

        unique_point = False
        while not unique_point:
            x = random.randint(0,COLS)
            y = random.randint(1,ROWS)
            position = Point(x, y)
            if plot_list.count(position) < 1:
                unique_point = True
                plot_list.append(position)

        position = position.scale(CELL_SIZE)

        # # Rocks are some shade of grey.
        # # Gems are some shade of cyan.
        
        artifact = Artifact()

        decision = random.randint(64,255)
        if decision < 128:  # It's a rock.
            color = Color(decision, decision, decision)
            artifact.set_color(color)
            artifact.set_text('@')
            artifact.set_value(-1)
        else:               # It's a gem
            color = Color(0, decision, decision)
            artifact.set_color(color)
            artifact.set_text('*')
            artifact.set_value(1)

        # color = Color(k, k, k)

        # artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        # artifact.set_color(color)
        artifact.set_position(position)
        # artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()