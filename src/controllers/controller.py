import logging

from src.models import Model
from src.views import View

logger = logging.getLogger(__name__)


class Controller:

    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self._bind()

    def _bind(self) -> None:
        for btn in self.view.buttons:
            btn.config(
                command=lambda caption=btn["text"]: self.on_button_click(caption)
            )

    def start_calculator(self) -> None:
        """
        Start the application.
        """
        self.view.mainloop()

    def on_button_click(self, button_caption: str) -> None:
        result = self.model.calculate(button_caption)

        self.view.value_var.set(result)
