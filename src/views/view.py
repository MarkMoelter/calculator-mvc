import logging
import tkinter as tk
from tkinter import ttk

from calc_caption_enum import CalcCaption

logger = logging.getLogger(__name__)


class View(tk.Tk):
    PAD = 10

    MAX_BUTTONS_PER_ROW = 4

    button_captions = [
        CalcCaption.CLEAR,
        CalcCaption.INVERT_SIGN,
        CalcCaption.PERCENT,
        CalcCaption.DIVIDE,
        '7', '8', '9', CalcCaption.MULTIPLY,
        '4', '5', '6', CalcCaption.SUBTRACT,
        '1', '2', '3', CalcCaption.ADD,
        '0', CalcCaption.DECIMAL, CalcCaption.EQUALS,
    ]

    def __init__(self) -> None:
        super().__init__()

        self.title('PyCalculator')

        self.main_frame = self._make_main_frame()
        self.value_var = tk.StringVar()
        self._make_entry()
        self.buttons = self._make_buttons()

    def _make_main_frame(self):
        frame = ttk.Frame(self)
        frame.pack(padx=self.PAD, pady=self.PAD)
        return frame

    def _make_entry(self) -> None:
        """Make the entry widget."""
        ent = ttk.Entry(self.main_frame,
                        justify='right',
                        textvariable=self.value_var)
        ent.state(statespec=['readonly'])  # Make entry read-only
        ent.pack(fill='x')

    def _make_buttons(self) -> list[ttk.Button]:
        """Make the calculator buttons."""
        outer_frame = ttk.Frame(self.main_frame)
        outer_frame.pack()

        inner_frame = ttk.Frame(outer_frame)

        buttons = []
        for idx, caption in enumerate(self.button_captions):
            if idx % self.MAX_BUTTONS_PER_ROW == 0:
                inner_frame = ttk.Frame(outer_frame)
                inner_frame.pack()

            btn = ttk.Button(
                inner_frame,
                text=caption
            )
            btn.pack(side='left')

            buttons.append(btn)

        return buttons
