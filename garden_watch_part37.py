# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: GardenWatch
import unittest


def test_basic():
    assert 1 + 1 == 2, "1+1 should be 2"


def test_string_case():
    assert "hello".upper() == "HELLO", "String case conversion failed"


def test_list_operations():
    lst = [1, 2, 3]
    lst.append(4)
    assert len(lst) == 4
    assert lst[3] == 4


def test_dict_access():
    d = {"name": "GardenWatch", "version": 37}
    assert d["name"] == "GardenWatch"
    assert d["version"] == 37


def test_math_operations():
    result = (10 + 5) * 2 - 8 / 4
    assert result == 17.25


if __name__ == "__main__":
    test_basic()
    test_string_case()
    test_list_operations()
    test_dict_access()
    test_math_operations()
    print("All basic tests passed!")
