import pytest
import random


def test_months_in_year(year2020):
    """проверяем что в году 12 месяцев"""

    assert len(year2020) == 12


def test_13_months(year2020):
    """проверяем что к 12 добавился еще 1 месяц"""

    year2020.add("13month")
    assert len(year2020) == 13


def test_remove_month(year2020):
    """проверяем удаление 1ого месяца"""

    year2020.remove('Jan')
    print(year2020)
    assert len(year2020) == 11


@pytest.mark.parametrize("hour", ["5", "10", "15", "20", "очень много"])
def test_wasted_time(year2020, hour):
    """проверяем сколько часов я потрачу на домашку"""

    random_month = random.sample(year2020, 1)
    print("Сегодня {random_month}, и я потратил {hour} часов на изучение уроков".format(random_month=random_month,
                                                                                        hour=hour))
    assert random_month != int

def test_union_year():
    """обьединяем все месяцы"""

    first = {"Jan", "Feb", "March", "Apr"}
    second = {"May", "June", "July", "Aug"}
    third = {"Sep", "Oct", "Nov", "Dec"}

    year = first.union(second, third)
    print(year)
    assert len(year) == 12
