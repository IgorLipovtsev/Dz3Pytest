import pytest


@pytest.fixture()
def all_fruits():
    """
    фикстура для списков
    """
    fruits = ["banana", "apple", "orange", "apple"]
    return fruits


@pytest.fixture()
def year2020():
    """
    фикстура для сэтов
    """
    months = set(["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
    return months


@pytest.fixture()
def week():
    """
     фикстура для словарей
    """
    not_a_full_week = {'day1': 'Monday', 'day2': 'Tuesday', 'day3': 'Wednesday', 'day4': 'Thursday', 'day5': 'Friday'}
    return not_a_full_week


@pytest.fixture()
def homework():
    """
     фикстура для стринг
    """
    dz = "domashka"
    return dz