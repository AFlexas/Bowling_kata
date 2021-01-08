from src.bowling import Bowling
def test_open_frame():
    assert 51 == Bowling.open_frame(4, 5, 9, 8, 7, 3, 1, 0, 5, 9)
    # numero de bolos tirados en los dos intentos de los 10 turnos
def test_spares():
    assert 300 == Bowling.score_strike('X, X, X, X, X, X, X, X, X, X, X, X')