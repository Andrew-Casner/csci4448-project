class Game:

    def __init__(self, id):
        self.id = id
        self.homeTeam = None
        self.awayTeam = None
        self.scoreHome = 0
        self.scoreAway = 0
        self.forefit = False
        self.complete = False
        self.day = 0
        self.month = 0
        self.year = 0
        self.time = None
        self.location = ""

    def getId(self):
        return self.id

    def getDay(self):
        return self.day

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year

    def getTime(self):
        return self.time

    def getDatestring(self):
        return self.month + "/" + self.day + "/" + self.year

    def setDay(self, day):
        self.day = day

    def setMonth(self, month):
        self.month = month

    def setYear(self, year):
        self.year = year

    def setTime(self, time):
        self.time = time

    def getHomeTeam(self):
        return self.homeTeam

    def setHomeTeam(self, home):
        self.homeTeam = home

    def getAwayTeam(self):
        return self.awayTeam

    def setAwayTeam(self, away):
        self.awayTeam = away

    def getLocation(self):
        return self.location

    def setLocation(self, loc):
        self.location = loc

    def getScoreHome(self):
        return self.scoreHome

    def setScoreHome(self, score):
        self.scoreHome = score

    def getScoreAway(self):
        return self.scoreAway

    def setScoreAway(self, score):
        self.scoreAway = score

    def isForefit(self):
        return self.forefit

    def gameForefit(self):
        self.forefit = True

    def isComplete(self):
        return self.complete

    def gameComplete(self):
        self.complete = True

