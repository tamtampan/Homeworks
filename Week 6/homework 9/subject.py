"""Model for describing departments."""


class Subject:
    """Model for exams."""

    def __init__(self, name: str, exam_code: str) -> None:
        """Initialize the Exam object."""
        self.name = name
        self.exam_code = exam_code

    def __str__(self) -> str:
        """Get information about Exam object."""
        return f"Predmet: {self.name}, Sifra predmeta: {self.exam_code}"
