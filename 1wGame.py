import random


class GameRun():
    def __init__(self,GameRound = 10,cout = 0):
        self.gameround=GameRound
        self.cout = cout

    def whowin(self,PlayA,PlayB):
        if PlayA < PlayB:
            win = 1
        elif PlayA == PlayB:
            win = 0
        else:
            win = 2
        self.cout += 1
        return  win

class Player():
    def __init__(self,Totalmoney = 100,outmoneylist = [],takemoneylist = [],duemoneylist = []):
        self.totalmoney = Totalmoney
        self.outmoneylist = outmoneylist
        self.takemoneylist = takemoneylist
        self.duemoneylist = duemoneylist

    def outmoney(self,money):
        self.outmoneylist.append(money)

    def takemoney(self,money):
        self.takemoneylist.append(money)

    def duemoney(self,money):
        self.duemoneylist.append(money)
        self.totalmoney -= money

class Play_PlanA(Player):
    def due(self):
        self.duemoney(10)
        return 10

class Play_PlanB(Player):
    def __init__(self,Totalmoney = 100,outmoneylist = [],takemoneylist = [],duemoneylist = []):
        self.totalmoney = Totalmoney
        self.outmoneylist = outmoneylist
        self.takemoneylist = takemoneylist
        self.duemoneylist = duemoneylist

    def due(self):
        if len(self.duemoneylist) < 9:
            money = random.randint(0,self.totalmoney)
        else:
            money = self.totalmoney
        self.duemoney(money)
        return money

class Play_PlanC(Player):
    def due(self):
        return 1


if __name__ == '__main__':
    Game = GameRun()
    PlayerA = Play_PlanA()
    PlayerB = Play_PlanB()
    print  "GameRound :", Game.gameround
    print  "Player A : ", PlayerA.totalmoney
    print  "Player B : ", PlayerB.totalmoney

    for i in range(0, Game.gameround):
        winer = "none"
        gameround = i+1
        moneyA = PlayerA.due()
        moneyB = PlayerB.due()
        moneysum = moneyA+moneyB
        result = Game.whowin(moneyA, moneyB)
        if result == 0:
            winer = "equal"
        elif result == 1:
            PlayerA.takemoney(moneysum)
            PlayerB.outmoney(moneyB)
            winer = "PlayerA WIN !"
        else:
            PlayerB.takemoney(moneysum)
            PlayerA.outmoney(moneyA)
            winer = "PlayerB WIN !"
        print "GameRound %d : %d vs %d ,%s " % (gameround, moneyA, moneyB, winer)
    totaltakemoneyA = 0
    totaltakemoneyB = 0
    for j in range(0,len(PlayerA.takemoneylist)):
        totaltakemoneyA += PlayerA.takemoneylist[j]
    for j in range(0, len(PlayerB.takemoneylist)):
        totaltakemoneyB += PlayerB.takemoneylist[j]
    if totaltakemoneyA > totaltakemoneyB:
        print "Game Winer is PlayerA ! %d : %d" % (totaltakemoneyA , totaltakemoneyB)
    elif totaltakemoneyA < totaltakemoneyB:
        print "Game Winer is PlayerB ! %d : %d" % (totaltakemoneyA , totaltakemoneyB)
    else:
        print "No One win the Game ! %d : %d" % (totaltakemoneyA , totaltakemoneyB)
