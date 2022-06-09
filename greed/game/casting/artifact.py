from pyray import pointer
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
import random

class Artifact(Actor):
    """
    A rock or gem with value.
    The responsability of the Artifact is to restart himself.
    
    Attributes:
        _points (int): The point value of the artifact.
        (All attributes of Actor)

    """
    def __init__(self):
        """Constructor. Initializes an instnance of Artifact.
        """
        super().__init__()
        self._points = 0
        self.restart()
        

    def get_points(self):
        """Returns the points value attached to any given instance.
        
        Args: 
            None
            
        Returns:
            _points (int)
        """
        return self._points


    def restart(self, at_top = False):
        """Resets all of the attributes in order to continue the sequence of play. 
        This particular instance may change types (rock -> gem or vice versa) or
        maybe not. In any case, it will have a new location and velocity on screen.

        Args: 
            None
        """
        point_values = [-1,1]
        self._points = point_values[random.randint(0,1)]
        random_value = random.randint(64,127)
        random_gem_color = random.randint(1,4)
        artifact_colors = [
            # Grey
            Color(random_value, random_value, random_value),
            # Red
            Color(random_value+128, 0, 0),
            # Yellow
            Color(random_value+128, random_value+128, 0),
            # Green
            Color(0, random_value+128, 0),
            # Cyan
            Color(0, random_value+128, random_value+128)
        ]

        x = random.randint(1, 60 - 1)
        if not at_top:
            y = random.randint(1, 40 - 1)
        else:
            y = 1
        
        self._position = Point(x, y).scale(self._font_size)
        self._velocity = Point(0, random.randint(2, 10))

        if self._points == -1:
            self.set_text('@')
            self.set_color(artifact_colors[0])
            # print("I am now a ROCK.")
        else: 
            self.set_text('*')
            self.set_color(artifact_colors[random_gem_color])
            # print("I am now a GEM.")