import pytest

from cellularautomata.gui.setupmap.clickabletile import ClickableTile


@pytest.mark.parametrize("op1_kwargs, op2_kwargs, expected", [
    ({'row':1, 'column':1}, {'row':0, 'column':1}, False),
    ({'row':1, 'column':1}, {'row':1, 'column':1}, False),
    ({'row':1, 'column':1}, {'row':2, 'column':1}, True),
    ({'row':1, 'column':1}, {'row':1, 'column':2}, True),
])
def test_less_than_function(op1_kwargs, op2_kwargs, expected):
    # given:
    op1:ClickableTile = ClickableTile(**op1_kwargs)
    op2:ClickableTile = ClickableTile(**op2_kwargs)

    # expect:
    assert (op1 < op2) is expected
