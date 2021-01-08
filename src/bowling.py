class Bowling:
    strike = 'X'
    
    spare = '/'

    # def __init__(self, score):
    #     if score != int:
    #         raise ValueError ("Score not valid")
    #     else:
    #         True

    @staticmethod
    def open_frame(*score):
        for numbers in score:
            if numbers < 10:
                return sum(score)
    @staticmethod
    def score_strike(*score):
        contador = 0
        for numbers in score:
            if numbers == 'X':
                contador == contador + 10 + [score+1] + [score + 2]
                return contador 




