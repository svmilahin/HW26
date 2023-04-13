from json import JSONDecodeError
import json


class Data:

    def __init__(self, path):
        """
        При создании экземпляра нужно указать путь к файлу с данными
        """
        self.path = path

    def load_data(self):
        """
        Загружает данные из файла и возвращает обычный list
        """
        try:
            with open(self.path, 'r', encoding='UTF-8') as fl:
                data = json.load(fl)
            return data
        except FileNotFoundError as err:
            return f'Файл не найден: {err}'
        except JSONDecodeError as err:
            return f'Файл не удалось преобразовать: {err}'
