import random
from xml.etree.ElementTree import tostring

from game.shared.point import Point 
from game.shared.color import Color
from game.casting.artifact import Artifact


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self.points = 0
        self.artifact_floor = 40
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """

        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        # Makes sure there are always 40 artifacts
        if (len(artifacts) < self.artifact_floor):
            for n in range((self.artifact_floor - len(artifacts))):
                x = random.randint(1, 59)
                y = 0
                position = Point(x, y)
                postion = position.scale(15)

                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                color = Color(r, g, b)
                brown = Color(87,65,47)

                value = random.randint(0,1)
                text = ''

                artifact = Artifact()
                
                artifact.set_font_size(15)

                if (value == 0): 
                    # Rock
                    artifact.set_color(brown)
                    text = 'o'
                    artifact.set_text(text)
                    artifact.set_message(value -1)
                else: 
                    # Gem
                    text = '*'
                    artifact.set_color(color)
                    artifact.set_text(text)
                    artifact.set_message(value)

                
                artifact.set_position(position)
                
                
                cast.add_actor("artifacts", artifact)


        # Scroll the artifacts from top of screen down to bottom
        for artifact in artifacts:
            position = artifact.get_position()
            position._y += 1
            artifact.set_position(position)

        # use banner to set points in top screen for score
        banner.set_text(f"Score: {self.points}" )

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for artifact in artifacts:
            if robot.get_position().equals(artifact.get_position()):
                message = artifact.get_message()
                self.points += int(message)
                banner.set_text(f"Score: {self.points}")
                cast.remove_actor("artifacts", artifact)   
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()