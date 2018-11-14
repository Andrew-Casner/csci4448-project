class Tournament:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.games = []
        self.teams = []
        self.winner = None

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getTeams(self):
        return self.teams

    def addTeam(self, team):
        self.teams.push(team)

    def removeTeam(self, teamIn):
        itr = 0
        popIdx = -1
        for team in self.teams:
            if team == teamIn:
                popIdx = itr
            itr = itr + 1

        if popIdx != -1:
            self.teams.pop(popIdx)


    def getWinner(self):
        return self.winner

    def setWinner(self, winner):
        self.winner = winner

