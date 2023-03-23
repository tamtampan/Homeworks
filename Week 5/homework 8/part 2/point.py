
class Point:
    """Model for point."""

    def __init__(self, x: int, y: int):
        """Initialize the point object."""
        self.x = x
        self.y = y

    def change_coordinates(self, new_x, new_y):
        """Change point coordinates."""
        self.x = new_x
        self.y = new_y
