from src.ui.ui_utils import UIUtils
from src.utils.config import Config


def employers_list(utils: UIUtils, config: Config):
    while True:
        utils.clear_screen()
        menu_list = ['Список']
        [print(f"{i + 1}. {menu_list[i]}") for i in range(len(menu_list))]
        match input('>> ').strip():
            case '1':
                pass
            case '':
                return
