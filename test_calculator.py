import calculator
import pytest

def test_average():
    assert calculator.average([1, 2, 3, 4, 5]) == 3
    assert calculator.average([0, 0, 0, 0, 0]) == 0
    assert calculator.average([10, 20, 30, 40, 50]) == 30
    assert calculator.average([-1, 0, 1]) == 0
    assert calculator.average([]) == 0

def test_get_minimum():
    assert calculator.get_minimum([1, 2, 3, 4, 5]) == 1
    assert calculator.get_minimum([0, 0, 0, 0, 0]) == 0
    assert calculator.get_minimum([10, 20, 30, 40, 50]) == 10
    assert calculator.get_minimum([-1, 0, 1]) == -1
    assert calculator.get_minimum([]) is None

if __name__ == "__main__":
    pytest.main()
