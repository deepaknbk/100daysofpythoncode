class Roll:
    def __init__(self, name):
        self.name = name

    def can_defeat(self, p2_roll):
        wins = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock',
        }


        if p2_roll.name == wins[self.name]:
            return True

        else:
            return False


class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score