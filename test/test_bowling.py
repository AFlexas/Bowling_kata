from src.bowling import Bowling
def test_it_is_strike():
    # assert 60 == Bowling.it_is_strike(1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5)
    # assert 80 == Bowling.it_is_strike(2,3,4,5,6,2,3,4,5,6,2,3,4,5,6,2,3,4,5,6)

# def test_it_is_strike():
#     assert 300 == Bowling.it_is_strike('X, X, X, X, X, X, X, X, X, X, X')

    assert 60 == Bowling("12345123451234512345").it_is_strike()
    assert 90 == Bowling("9-9-9-9-9-9-9-9-9-9-").it_is_strike()
    assert 150 == Bowling('5/5/5/5/5/5/5/5/5/5/5').it_is_strike()
    assert 149 == Bowling('8/549-XX5/53639/9/X').it_is_strike()
    assert 111 == Bowling('9-9-9-9-9-9-9-9-9-XXX').it_is_strike()
    assert 141 == Bowling('XXX9-9-9-9-9-9-9-').it_is_strike
    assert 175 == Bowling('X5/X5/XX5/--5/X5/').it_is_strike()
    assert 120 == Bowling('XX9-9-9-9-9-9-9-9-').it_is_strike()