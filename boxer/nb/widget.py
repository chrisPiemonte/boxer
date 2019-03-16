from typing import *
from PIL import Image
import ipywidgets as widgets
from IPython.display import display # as disp
from ipywidgets import interact, interactive, SelectionRangeSlider

from boxer.service.imgcollection import ImgCollection
from .components import *

Callback = Callable[[Tuple[int, int], Tuple[int, int]], None]

class CollectionWidget:
    def __init__(self, image_collection: ImgCollection) -> None:
        pass


class SingleImageWidget:
    def __init__(self, path: str) -> None:
        self.path: str    = path
        self.image: Image = Image.open(path)

    def show(self) -> None:
        self.h_slider: SelectionRangeSlider = get_range_slider(self.image, 'horizontal')
        self.v_slider: SelectionRangeSlider = get_range_slider(self.image, 'vertical')
        callback: Callback = get_callback_range_slider(self.image, self.h_slider, self.v_slider)
        controller = get_range_controller(callback, self.h_slider, self.v_slider)
        layout_top_row: HBox    = get_layout_row([self.h_slider])
        layout_bottom_row: HBox = get_layout_row([self.v_slider, controller])
        display(layout_top_row, layout_bottom_row)

    def get_string_box(self) -> str:
        top: int    = self.v_slider.value[1]
        left: int   = self.h_slider.value[0]
        right: int  = self.h_slider.value[1]
        bottom: int = self.v_slider.value[0]
        return f'{top},{left},{right},{bottom},{None}'

    def get_box(self) -> BoundingBox:
        top: int    = self.v_slider.value[1]
        left: int   = self.h_slider.value[0]
        right: int  = self.h_slider.value[1]
        bottom: int = self.v_slider.value[0]
        return BoundingBox(top, left, right, bottom)
