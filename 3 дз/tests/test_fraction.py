from app.fraction import Fraction


def test_reduce():
    q = Fraction(4, 8)
    q.reduce()
    assert q.num == 1
    assert q.den == 2


def test__str__():
    a = Fraction(1, 20)
    assert str(a) == "1/20"


def test_input(mocker):
    mocker.patch('builtins.input', side_effect=['1', '4'])
    e = Fraction()
    e.input()
    assert e.num == 1
    assert e.den == 4



    





    
    
