from line import Line


class Quadrilateral:
    """Model for quadrilateral."""

    def __init__(self, a: Line, b: Line):
        """Initialize the quadrilateral object."""
        self.a = a
        self.b = b

    def scope_of_quadrilateral(self):
        """Calculate the scope of quadrilateral."""
        return (2 * self.a.length) + (2 * self.b.length)

    def surface(self):
        """Calculate the surface of quadrilateral."""
        return self.a.length * self.b.length
