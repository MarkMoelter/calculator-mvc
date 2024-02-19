from src.models import Model
from src.views import View


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
