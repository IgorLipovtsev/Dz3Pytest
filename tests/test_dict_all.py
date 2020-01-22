import pytest


def test_values_in_dict(week):
    """смотрим значения словаря"""

    w = week.values()
    print(f'\nзначения словаря: {w}')
    assert True


@pytest.mark.parametrize("weekend_day", [{'day6': 'Saturday'}, {'day7': 'Sunday'}])
def test_full_week(week, weekend_day):
    """добавляем субботу, воскресенье"""

    w = week.update(weekend_day)
    print(week)
    assert len(week) == 6


def test_get_keys_of_dict(week):
    """смотрим ключи словаря"""

    w = week.keys()
    print(f'\nключи словаря: {w}')
    assert 'day4' in w


def test_pop_dict(week):
    """удаляем четверг"""

    w = week.pop('day4')
    print(f'\nключи словаря: {week}')
    assert 'day4' not in w


def test_get_6day(week):
    """проверяем что нет субботы"""

    w = week.get('day6')
    print(f'\nналичие субботы в словаре: {w}')
    assert w == None
