import logging
import tkinter as tk
from tkinter import ttk

logger = logging.getLogger(__name__)


class View(tk.Tk):
    PAD = 10

    MAX_BUTTONS_PER_ROW = 4

    button_captions = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '='
    ]

    def __init__(self) -> None:
        super().__init__()

        self.title('PyCalculator')
        self.main_frame = self._make_main_frame()
        self.value_var = tk.StringVar()
        self._make_entry()
        self._make_buttons()

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

    def _make_buttons(self) -> None:
        """Make the calculator buttons."""
        outer_frame = ttk.Frame(self.main_frame)
        outer_frame.pack()

        inner_frame = ttk.Frame(outer_frame)

        for idx, caption in enumerate(self.button_captions):
            if idx % self.MAX_BUTTONS_PER_ROW == 0:
                inner_frame = ttk.Frame(outer_frame)
                inner_frame.pack()

            button = ttk.Button(inner_frame, text=caption)
            button.pack(side='left')
