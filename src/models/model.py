import logging

from calc_caption_enum import CalcCaption

logger = logging.getLogger(__name__)


class Model:

    def __init__(self) -> None:
        self.value = ''

    def calculate(self, caption: str) -> str:

        if caption == 'C':
            self.value = ''

        elif caption == CalcCaption.INVERT_SIGN:
            pass

        elif caption.isdigit():
            self.value += caption

        return self.value
