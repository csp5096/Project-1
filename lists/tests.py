import pytest

@pytest.mark.smoke
def test_bad_maths():
    with pytest.raises(AssertionError):
        assert (1 + 1) == 3
