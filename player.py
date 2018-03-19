from strategy import *
import random
from hand import JunkenHand

class Player:

    def __init__(self,name):
        self._name = name
        #デフォルトではJankenStrategyをつかう
        self.strategy = JankenStrategy()

    @property
    def name(self):
        return str("player:"+self._name)

    def next_hand(self):
        #random.seed()
        #n = random.randint(0,2)
        #return(JunkenHand(n))
        return self.strategy.next_hand()

if __name__ == '__main__':
    player1 = Player("taro")
    player2 = Player("hanako")
    player1.strategy = RandomStrategy()
    hand1 = player1.next_hand();
    hand2 = player2.next_hand();

    result = "あいこ" #常に結果を反映させるために最初にあいこを代入している。
    if hand1.win_to(hand2):
        result = player1.name+"の勝利"
    elif hand1.lose_to(hand2):
        result = player2.name+"の勝利"
    print("{}:{} - {}:{}({})".format(player1.name,hand1,hand2,player2.name,result))
