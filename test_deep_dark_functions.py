import deep_dark_functions
import pytest


def test_millimeters_to_inches():
    assert type(deep_dark_functions.millimeters_to_inches()) == str


check_list = [
    (5, 0.1968503937007874),
    (0, 0.0),
    (25.4, 1),
    (99, 3.8976377952755907),
]


@pytest.mark.parametrize('test_input, expected', check_list)
def test_millimeters_to_inches(test_input, expected):
    assert deep_dark_functions.millimeters_to_inches(test_input) == expected


def test_area_of_the_paper():
    assert type(deep_dark_functions.area_of_the_paper()) == str


check_list = [
    (('A0', 841, 1189), 'Paper A0 has area 1549.9240498481 square inches'),
    (('A3', 297, 420), 'Paper A3 has area 193.34738669477343 square inches'),
    (('A7', 74, 105), 'Paper A7 has area 12.043524087048176 square inches'),
]


@pytest.mark.parametrize('test_input, expected', check_list)
def test_area_of_the_paper(test_input, expected):
    assert deep_dark_functions.area_of_the_paper(test_input) == expected


def test_filter_temp():
    assert type(deep_dark_functions.filter_temp()) == str


check_list = [
    ('SGHF JKhg sjhgkj dfshdfhsgkA', True),
    ('sgkljlkj gjsdlkjg lskd jglklks sdjkglk', False),
    ('Asala msdgjk sg;s gldk', True),
]


@pytest.mark.parametrize('test_input, expected', check_list)
def test_filter_temp(test_input, expected):
    assert deep_dark_functions.filter_temp(test_input) == expected
