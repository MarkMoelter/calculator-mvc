import logging

import calc_captions as cc

logger = logging.getLogger(__name__)


class Model:

    def __init__(self) -> None:
        self.value = ""

    def calculate(self, caption: str) -> str:

        if caption == "C":
            self.value = ""

        elif caption == cc.INVERT_SIGN and self.value and self.value != cc.DECIMAL:
            # Determine if int or float
            if cc.DECIMAL in self.value:
                numeric_val = float(self.value)
            else:
                numeric_val = int(self.value)

            self.value = str(numeric_val * -1)

        elif caption == cc.DECIMAL:
            if caption not in self.value:
                self.value += caption

        elif caption == cc.DELETE:
            self.value = self.value[:-1]

        elif caption.isdigit():
            self.value += caption

        return self.value
