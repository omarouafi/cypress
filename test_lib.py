def average(arr):
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)

def get_minimum(values):
    if len(values) == 0:
        return None
    return min(values)

import pytest
def test_average():
    assert average([1, 2, 3, 4, 5]) == 3
    assert average([0, 0, 0, 0, 0]) == 0
    assert average([10, 20, 30, 40, 50]) == 30
    assert average([-1, 0, 1]) == 0
    assert average([]) == 0


def test_get_minimum():
    assert get_minimum([1, 2, 3, 4, 5]) == 1
    assert get_minimum([0, 0, 0, 0, 0]) == 0
    assert get_minimum([10, 20, 30, 40, 50]) == 10
    assert get_minimum([-1, 0, 1]) == -1
    assert get_minimum([]) is None

if __name__ == "__main__":
    pytest.main()