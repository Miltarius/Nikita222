from app.fraction import Fraction, IrreduceadFraction


def test_input(mocker):
    mocker.patch('builtins.input', side_effect=['2', '4'])
    e = IrreduceadFraction()
    e.input()
    assert e.num == 1
    assert e.den == 2


def test__init__():
    q = IrreduceadFraction(4, 8)
    assert q.num == 1
    assert q.den == 2
