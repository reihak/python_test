import random
from hand import JunkenHand

class JankenStrategy:
    #とりあえず固定の手を出す
    def next_hand(self):
        return JunkenHand.SCISSORS

class RandomStrategy(JankenStrategy):
    def next_hand(self):
        random.seed()
        n = random.randint(0,2)
        return JunkenHand(n)
