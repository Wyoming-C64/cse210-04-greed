import random
from game.shared.point import Point 
from game.shared.color import Color
from game.casting.artifact import Artifact


class Director:
    """A thing that directs the game. 
    
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
        self.score = 0
        self._gems_available = True
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        
        while self._video_service.is_window_open() and self._gems_available:
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def do_end_game(self):
        """Display some information when the game has ended.
        
        Args:
            None.
        """
        print(chr(27)+"[2J")
        you_won = "You collected all the gems!" if not self._gems_available else ""
        print(f"The game is over. {you_won}")
        print(f"You were able to achieve a final score of: {self.score} points.")
        print()
        print("Thank you for playing.")
        print()


    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("players")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the player's position, the artifacts' positions and resolves 
        any collisions with player and artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """

        banner = cast.get_first_actor("banners")
        player = cast.get_first_actor("players")
        artifacts = cast.get_actors("artifacts")

        # Scroll the artifacts from top of screen down to bottom, and move the player.
        
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()

        player.move_next(max_x, max_y)
        player_bubble_size = int( (player.get_font_size()-1) / 2 ) 
        gems = 0

        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
            if player.get_position().collides_with(artifact.get_position(), player_bubble_size):
                points = artifact.get_points()
                self.score += points
                # Restart artifact at top.
                artifact.restart(True)
            if artifact.get_points() > 0:
                gems += 1

        banner.set_text(f"Score: {self.score}    Gems left: {gems}")

        if gems <= 0:
            self._gems_available = False 
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()