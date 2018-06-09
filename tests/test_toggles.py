import pytest

import donut

def test_create_toggle():
    with pytest.raises(donut.exceptions.DonutError):
        donut.is_toggle_active('test_toggle')

    donut.create_toggle('test_toggle', active=False)

    assert donut.is_toggle_active('test_toggle') is False

