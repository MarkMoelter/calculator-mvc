import logging

import src.calc_captions as cc

logger = logging.getLogger(__name__)


class Model:
    def __init__(self) -> None:
        self.prev_value = ""
        self.value = ""
        self.operator = ""

    def calculate(self, caption: str) -> str:
        if caption == cc.CLEAR:
            self.value = ""
            self.operator = ""
            self.prev_value = ""

        elif caption == cc.INVERT and self.value and self.value != cc.DECIMAL:
            # Determine if int or float
            is_float = cc.DECIMAL in self.value
            if is_float:
                numeric_val = float(self.value)
            else:
                numeric_val = int(self.value)

            self.value = str(numeric_val * -1)

        elif caption == cc.EQUALS:
            if self.value and self.operator and self.prev_value:
                equation = f"{self.prev_value} {self.operator} {self.value}"
                try:
                    self.value = str(eval(equation))
                except ZeroDivisionError:
                    logger.warning("Cannot divide by zero")

        elif caption == cc.DECIMAL:
            if caption not in self.value:
                self.value += caption

        elif caption == cc.DELETE:
            self.value = self.value[:-1]

        elif caption.isdigit():
            self.value += caption

        elif self.value:
            self.operator = caption
            self.prev_value = self.value
            self.value = ""

        return self.value
