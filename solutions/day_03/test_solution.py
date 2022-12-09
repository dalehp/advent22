import pytest

from .solution import priority


def test_priority():
    assert priority("p") == 16
    assert priority("L") == 38
    assert priority("v") == 22
    assert priority("t") == 20
    assert priority("s") == 19


def test_priority_non_char():
    with pytest.raises(ValueError):
        priority("nope")


def test_priority_non_alpha():
    with pytest.raises(ValueError):
        priority("!")
