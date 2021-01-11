class Bowling:
    def __init__(self, score):
        self.score = list(score)
    
    def it_is_strike(self):
        # strikev2 = []
        # sparev2 = []
        # nullv2 = []
        strike = ["X"]
        spare = ["/"]
        null = ["-"]
        contador = 0
        for number in self.score:
            if number in strike:
                contador = contador + 10 + [self.score + 1] + [self.score + 2]
            else:
                pass
            if number in spare:
                contador = contador + 10 + [self.score + 1]
            else:
                pass
            if number in null:
                contador = contador + 0
            else:
                pass
            if int(number) < 10:
                contador = contador + number.isdigit()
        return contador

    

    