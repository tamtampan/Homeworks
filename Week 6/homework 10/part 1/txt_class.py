from file_class import File
import datetime


class TextFile(File):

    def __init__(self, name: str, file_type: str, size: str, description: str, content: str):
        super().__init__(name, file_type, size, description, content)
        self.num_of_characters = len(self.content)

    def write(self, new_content):
        self.content = new_content
        self.num_of_characters = len(new_content)
        self.date = datetime.datetime.now().date()
        self.time = datetime.datetime.now().time()
