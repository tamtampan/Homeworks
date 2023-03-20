from file_class import File


class ImgFile(File):
    def __init__(self, name: str, file_type: str, size: str, description: str, content: str, pic_dimension: str) -> None:
        super().__init__(name, file_type, size, description, content)
        self.pic_dimension = pic_dimension
