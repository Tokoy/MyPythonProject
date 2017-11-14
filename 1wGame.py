import random


class GameRun():
    def __init__(self,GameRound = 10):
        self.gameround=GameRound

    def whowin(self,PlayA,PlayB):
        if PlayA < PlayB:
            win = 1
        elif PlayA == PlayB:
            win = 0
        else:
            win = 2
        return  win

class Player():
    def __init__(self,Totalmoney = 100):
        self.totalmoney = Totalmoney

    def outmoney(self,money):
        restmoney = self.totalmoney - money
        self.totalmoney = restmoney

    def takemoney(self,money):
        restmoney = self.totalmoney + money
        self.totalmoney = restmoney

    def due(self):
        money = random.randint(0, self.totalmoney)
        return money


Game = GameRun()
PlayerA = Player()
PlayerB = Player()
print  "GameRound :",Game.gameround
print  "Player A : ",PlayerA.totalmoney
print  "Player B : ",PlayerB.totalmoney

for i in range(0,Game.gameround):
    winer = "none"
    moneyA = PlayerA.due()
    moneyB = PlayerB.due()
    result = Game.whowin(moneyA,moneyB)
    if result == 0:
        print PlayerA.totalmoney
        print PlayerB.totalmoney
        winer = "equal"
    elif result == 1:
        PlayerA.takemoney(moneyB)
        PlayerB.outmoney(moneyB)
        winer = "PlayerA WIN !"
    else:
        PlayerA.outmoney(moneyA)
        PlayerB.takemoney(moneyA)
        winer = "PlayerB WIN !"
    print "GameRound %d : %d vs %d ,%s || PlayA : %d , PlayB : %d " % (i+1,moneyA,moneyB,winer,PlayerA.totalmoney,PlayerB.totalmoney)

if PlayerA.totalmoney > PlayerB.totalmoney:
    print "Game Winer is PlayerA !"
elif PlayerA.totalmoney < PlayerB.totalmoney:
    print "Game Winer is PlayerB !"
else:
    print "No One win the Game !"



