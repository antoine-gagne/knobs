import donut

from donut.exceptions import DonutError


def test_toggle():
    try:
        donut.is_toggle_active('test_knob')
    except DonutError:
        print('is_toggle_active raised before test_knob created')

    donut.create_flag('test_knob', active=False)
    print('created test_toggle')

    print(donut.is_toggle_active('test_knob'))


if __name__ == '__main__':
    test_toggle()