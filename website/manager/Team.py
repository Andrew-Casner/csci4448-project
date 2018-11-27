from manager.Coach import Coach


class Team:

    def __init__(self, id, name=None, city=None, state=None):
        self.id = id
        self.name = name
        self.players = []
        self.coach = None
        self.city = city
        self.state = state
        self.seed = 0


    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getCoach(self):
        return self.coach

    def setCoach(self):
        self.coach = coach

    def getPlayers(self):
        return self.players

    def addPlayer(self, player):
        self.players.append(player)

    def removePlayer(self, playerIn):
        itr = 0
        popIdx = -1
        for player in self.players:
            if player == playerIn:
                popIdx = itr
            itr = itr + 1

        if popIdx != -1:
            self.players.pop(popIdx)

    def getCity(self):
        return self.city

    def setCity(self, city):
        self.city = city

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def setSeed(self, seed):
        self.seed = seed

    def getSeed(self):
        return self.seed

    def __str__(self):
        players = ''
        for player in self.players:
            players = players + str(player) + ' '
        return '#{} {}, {}, {}, {}'.format(self.seed, self.name, self.city, self.state, players)

