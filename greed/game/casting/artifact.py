from game.casting.actor import Actor
import random

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """The Artifact class. First I need to figure out what methods are needed...
    The only unique thing an Artifact does aside from an Actor is that it holds a message.
    So we will establish a message attribute, as well as the associated getter and setter."""


    def __init__(self):
        """Constructor. Initializes an instnance of Artifact, random either rock or gem.
        """
        super().__init__()
        self._value = 0
       

    
    def get_value(self):
        """Gets this artifact's message and returns it."""
        return self._value

    
    def set_value(self, value):
        """Sets this artifact's message to that specified by the message parameter."""
        self._value = value











    # artifact.set_text(text) # Actor method
    # artifact.set_font_size(FONT_SIZE) # Actor method
    # artifact.set_color(color) # Actor method
    # artifact.set_position(position) # Actor Method
    # artifact.set_message(message) # Artifact Method
