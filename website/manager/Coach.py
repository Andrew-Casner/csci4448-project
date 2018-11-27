from manager.Player import Player

class Coach(Player):

    def __init__(self):
        self.wins = 0
        self.losses = 0

    def getWins(self):
        return self.wins

    def addWin(self):
        self.wins = self.wins + 1

    def getLosses(self):
        return self.losses

    def addLoss(self):
        self.losses = self.losses + 1

    def getRecord(self):
        return self.wins/self.losses

    def setRecord(self, w, l):
        self.wins = w
        self.losses = l
