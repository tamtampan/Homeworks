from img_class import ImgFile


class Video(ImgFile):
    def __init__(self, name: str, file_type: str, size: str, description: str,
                 content: str, pic_dimension: str, duration: str) -> None:
        super().__init__(name, file_type, size, description, content, pic_dimension)
        self.duration = duration
