import pandas as pd
from typing import *
from pathlib import Path
from PIL import Image, ImageDraw


class ImgCollection:

    def __init__(self, images: Iterable, classes: Iterable = None):
        assert len(images) > 0
        self.images: List[str] = list(images)
        self.classes: set      = set(classes)
        self.__current: str    = self.images[0]
        self.__img2bbs: Dict[str, List[BoundingBox]] = {path: [] for path in images}


def from_folder(folder_path: str, classes=None) -> ImgCollection:
    path: Path   = Path(str(folder_path))
    images: List[str]  = path.glob('*')
    return ImgCollection(images)

def from_collection(images: Iterable, classes: Iterable = None) -> ImgCollection:
    return ImgCollection(images)
