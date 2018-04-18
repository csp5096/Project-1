import pytest

@pytest.mark.smoke
def test_bad_maths():
    assert (1 + 1) == 3
