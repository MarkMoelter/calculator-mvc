from .controllers import Controller
from .models import Model
from .views import View


def main() -> None:
    model = Model()
    view = View()
    controller = Controller(model, view)

    controller.start()


if __name__ == '__main__':
    main()
