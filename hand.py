from enum import Enum #enumからクラスEnumを呼び出す

class JunkenHand(Enum):
    ROCK = 0
    SCISSORS = 1
    paper = 2

    def __str__(self): #クラスの中にインデントさせる
        if self == JunkenHand.ROCK:
            return "👊"
        elif self == JunkenHand.SCISSORS:
            return "✌"
        else:
            return "✋"



    def win_to(self, hand):
        n = (self.value+1)%3
        return hand.value == n

    def lose_to(self,hand):
        return (self.value != hand.value) and not self.win_to(hand)
if __name__ == '__main__':
    print(JunkenHand.SCISSORS)
