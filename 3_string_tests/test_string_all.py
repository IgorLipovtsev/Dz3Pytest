import pytest


@pytest.mark.parametrize("slovo", ["nravitsa", "slojnaya", "legkaya"])
def test_concatenate(homework, slovo):
    """
    складываем слова
    """
    phrase = (f'\n{homework} очень {slovo}')
    print(phrase)
    assert slovo in phrase


def test_capitalize(homework):
    """
    переводим первый символ слова в верхний регистр
    """
    w = homework.capitalize()
    print(w)
    assert w[0].isupper() == True


def test_aplpha(homework):
    """
    проверяем что в слове только буквы
    """
    w = homework.isalpha()
    print(w)
    assert homework.isdigit() == False


def test_Upper(homework):
    """
    преобразуем слово к верхнему регистру
    """
    w = homework.upper()
    print(w)
    assert w[-1].isupper() == True


def test_count_symbol(homework):
    """
    ищем сколько символов А в слове
    """
    w = homework.count("a")
    print(w)
    assert w == 2
