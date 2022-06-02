from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """The Artifact class. First I need to figure out what methods are needed...
    The only unique thing an Artifact does aside from an Actor is that it holds a message.
    So we will establish a message attribute, as well as the associated getter and setter."""


    def __init__(self, message=""):
        """Constructor. Initializes an instnance of Artifact, optionally with a message.
        """
        super().__init__()
        self._message = message

    
    def get_message(self):
        """Gets this artifact's message and returns it."""
        return self._message

    
    def set_message(self, message):
        """Sets this artifact's message to that specified by the message parameter."""
        self._message = message











    # artifact.set_text(text) # Actor method
    # artifact.set_font_size(FONT_SIZE) # Actor method
    # artifact.set_color(color) # Actor method
    # artifact.set_position(position) # Actor Method
    # artifact.set_message(message) # Artifact Method
