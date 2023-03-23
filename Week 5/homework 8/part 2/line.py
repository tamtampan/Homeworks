from point import Point


class Line:
    """Model for line."""

    def __init__(self, first_point: Point, second_point: Point, length: int):
        """Initialize the line object."""
        self.first_point = first_point
        self.second_point = second_point
        self.length = length

    def change_point_a(self, new_first_point: Point):
        """Change first point."""
        self.first_point = new_first_point

    def change_point_b(self, new_second_point: Point):
        """Change second point."""
        self.second_point = new_second_point

    def change_length(self, new_length):
        """Change length of line."""
        self.length = new_length
