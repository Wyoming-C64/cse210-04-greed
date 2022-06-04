from pyray import pointer
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
import random

class Artifact(Actor):
    """
    A rock or gem with value.

    The responsability of the Artifact is to restart himself.

    Attributes
    """
    def __init__(self, message=""):
        """Constructor. Initializes an instnance of Artifact.
        """
        super().__init__()

    def restart(self):
        """Resets all of his attributes in order to continue the sequence of play.
        """
        x = random.randint(1, 60 - 1)
        y = random.randint(1, round(40 / 2) - 1)
        self._position = Point(x, y).scale(self._font_size)
        self.color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.velocity = Point(0, 5)