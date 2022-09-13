import pytest


def test_list_len():
    list = [1, 2, 3, 4]
    assert len(list) == 4


@pytest.mark.parametrize("test_data, expected_result", [([0, 1, 2, 3, 4], [0, 1, 2, 3, 4]), # отсортированные положит числа
                                                        ([4, 3, 2, 1, 0], [0, 1, 2, 3, 4]), # неотсортированные положит числа
                                                        ([-4, -3, -2, -1, 0], [-4, -3, -2, -1, 0]), # отсортированные негатив числа
                                                        ([-3, -4, -1, -2, 0], [-4, -3, -2, -1, 0]), # неотсортированные негатив числа
                                                        ([-4, 5, 1, 1, 0], [-4, 0, 1, 1, 5])])      # неотсортированные негатив и позитив числа
def test_list_sort(test_data, expected_result):
    list = test_data
    list.sort()
    assert list == expected_result

def test_list_remove():
        list = [1,2,3]
        try:
            assert list.remove(4)
        except ValueError:
            pass
