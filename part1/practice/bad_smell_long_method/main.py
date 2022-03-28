
from typing import Callable

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def read_from_str(input: str) -> list:
    return [
        {'name': name, 'age': int(age)}
        for name, age in [item.split(';') for item in input.split('\n')]
    ]


def sort_by(list_to_sort: list, key: str) -> list:
    return sorted(list_to_sort, key=lambda item: item[key])


def filter_by_predicate(list_to_filter: list, predicate: Callable) -> list:
    return list(filter(predicate, list_to_filter))


def get_users_list():
    # Чтение данных из строки
    csv_as_list = read_from_str(csv)
    csv_list_sorted = sort_by(csv_as_list, 'age')
    return filter_by_predicate(csv_list_sorted, lambda item: item['age'] > 10)


if __name__ == '__main__':
    print(get_users_list())