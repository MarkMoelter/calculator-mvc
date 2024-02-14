from src.controllers import Controller
from src.models import Model
from src.views import View

def main() -> None:
    model = Model()
    view = View()
    controller = Controller(model, view)

    controller.start()


if __name__ == '__main__':
    main()
