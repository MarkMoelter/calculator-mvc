import logging

from src.models import Model
from src.views import View

logger = logging.getLogger(__name__)


class Controller:

    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

    def start_calculator(self) -> None:
        """
        Start the application.
        :return: None
        """
        self.view.mainloop()

    def on_button_click(self, button_caption: str) -> None:
        logger.info(f"Clicked button: {button_caption}")
