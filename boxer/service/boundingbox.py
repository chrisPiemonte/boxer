from typing import *

class BoundingBox:

    def __init__(self, top: int, left: int, right: int, bottom: int, label=None) -> None:
        self.top: int    = top
        self.left: int   = left
        self.right: int  = right
        self.bottom: int = bottom
        self.label: int  = label

    def __repr__(self) -> str:
        return f'{self.top},{self.left},{self.right},{self.bottom},{self.label}'

    def __str__(self) -> str:
        return f'{self.top},{self.left},{self.right},{self.bottom},{self.label}'

# yolo format = <top,left,right,bottom,label>
def from_yolo_format(bounding_box_string: str) -> BoundingBox:
    elems: List[str] = bounding_box_string.split(',')
    assert len(elems) == 5
    top : int   = int(elems[0])
    left: int   = int(elems[1])
    right: int  = int(elems[2])
    bottom: int = int(elems[3])
    label: str  = elems[4]
    return BoundingBox(top, left, right, bottom, label)
