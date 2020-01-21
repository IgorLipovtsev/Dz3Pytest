import pytest


@pytest.mark.parametrize("more_fruits", ["pear", "peach", "pineapple", "tomato", "coconut"])
def test_find_tomato(all_fruits, more_fruits):
    """
    добавляем новые фрукты и ищем помидор
    """
    all_fruits.append(more_fruits)
    if "tomato" in all_fruits:
        print("\n tomato is not a fruit!!!")
        assert False  # экспиримент с False ассертом


def test_remove_banana(all_fruits):
    """
    удаляем банан из списка
    """
    banana = all_fruits.remove("banana")
    assert "banana" not in all_fruits


def test_count_apple(all_fruits):
    """
    проверяем сколько яблок в списке
    """
    apple = all_fruits.count("apple")
    print(f"\n добавили еще яблоко, их теперь {apple}")
    assert apple == 2


def test_count_orange(all_fruits):
    """
    смотрим где лежит апельсин
    """
    orange_index = all_fruits.index("orange")
    print(f"\n апельсин лежит тут: Индекс {orange_index}")
    assert orange_index == 2


def test_clear_fruits(all_fruits):
    """
    убираем все фрукты
    """
    no_fruits = all_fruits.clear()
    print(f"\n фруктов больше нет")
    assert no_fruits == None
