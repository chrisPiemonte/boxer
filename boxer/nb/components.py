from typing import *
from PIL import Image, ImageDraw
import ipywidgets as widgets
from IPython.display import display # as ipy_display
from ipywidgets import interact, interactive, SelectionRangeSlider, Output, HBox

from boxer.service.boundingbox import BoundingBox, from_yolo_format

vertical_desc   = 'Top - Down'
horizontal_desc = 'Left - Right'
Callback = Callable[[Tuple[int, int], Tuple[int, int]], None]

def get_range_slider(img: Image, orientation: str = 'horizontal') -> SelectionRangeSlider:
    width: int    = img.size[0]
    height: int   = img.size[1]
    max_size: int = width if orientation == 'horizontal' else height
    slider_range: range = range(0, width) if orientation == 'horizontal' else range(height, -1, -1)
    description: str = horizontal_desc if orientation == 'horizontal' else vertical_desc
    return widgets.SelectionRangeSlider(
        orientation=orientation,
        options=slider_range,
        index=(0, max_size - 1),
        description=description,
        disabled=False
    )

def get_callback_range_slider(img: Image, horizontal: Tuple[int, int], vertical: Tuple[int, int]) -> Callback:
    def callback(horizontal: Tuple[int, int], vertical: Tuple[int, int]) -> None:
        # TODO tuple cannot be annotated
        bottom, top = vertical
        left, right = horizontal
        box: BoundingBox = from_yolo_format(f'{top},{left},{right},{bottom},{None}')
        display(draw_box(img, box))
    return callback


def get_range_controller(callable: Callable[[SelectionRangeSlider, SelectionRangeSlider], None],
                         h_slider: SelectionRangeSlider, v_slider: SelectionRangeSlider) -> Output:
    return widgets.interactive_output(
        callable,
        {'vertical': v_slider, 'horizontal': h_slider}
    )

def draw_box(img: Image, box: BoundingBox, color: str = 'red') -> Image:
    new_img: Image  = img.copy()
    draw: ImageDraw = ImageDraw.Draw(new_img)
    draw.rectangle( ((box.left, box.top), (box.right, box.bottom)), outline=color)
    return new_img

def get_layout_row(components: Sequence[Any]) -> HBox:
    return widgets.HBox(components)
