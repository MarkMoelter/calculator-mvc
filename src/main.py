import logging

from src.controllers import Controller
from src.models import Model
from src.views import View


def main() -> None:
    logging.info('Starting PyCalc')

    model = Model()
    view = View()
    controller = Controller(model, view)
    controller.start_calculator()
    
    logging.info('Closing PyCalc')


def logger_setup(file_name: str = 'App.log') -> None:
    """
    Create a root logger with a Stream and File Handler
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(file_name)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    FORMAT = '%(levelname)s - %(asctime)s - %(name)s - %(message)s'
    formatter = logging.Formatter(FORMAT)
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


if __name__ == '__main__':
    logger_setup('calc.log')
    main()
