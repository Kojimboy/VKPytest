import pytest


def test_set_has_element():
    a = {1, 2, 2, 3, 0}
    assert 3 in a


@pytest.mark.parametrize("test_data1, test_data2, expected_result", [({1, 2, 2, 4}, {5, 6, 1, 0}, {1}),  #входит один элемент
                                                                     ({1, 2, 2, 4}, {5, 6, 6, 0}, set()), #ни один не входит
                                                                     ({1, 2, 2, 3, 4}, {1, 2, 6, 7, 3}, {1, 2, 3}), #входят несколько элементов
                                                                     ])
def test_set_intersection(test_data1, test_data2, expected_result):
    a = test_data1
    b = test_data2
    assert a.intersection(b) == expected_result


def test_set_from_list():
    try:
        assert set([[1, 2], [2, 3], [1, 2], [2, 5]])
    except TypeError:
        pass
