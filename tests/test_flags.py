import pytest

import donut


def test_flags():
    with pytest.raises(donut.exceptions.DonutError):
        donut.is_flag_active('test_flag')

    donut.create_flag('test_flag')

    assert donut.is_flag_active('test_flag') is False

