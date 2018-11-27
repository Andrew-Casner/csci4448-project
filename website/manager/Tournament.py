import random
import math
import uuid
from manager.Game import Game

class Tournament:

    def __init__(self, id, name, elims, st, gt):

        self.id = id
        self.name = name
        self.games = []
        self.teams = []
        self.winner = None
        self.elims = elims
        self.started = False
        self.startTime = st
        self.gameLength = gt

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getTeams(self):
        return self.teams

    def getGames(self):
        return self.games

    def addTeam(self, team, seed):
        # Generate Random Seed if non seeeded tourny
        if seed == 0:
            seed = random.randint(1, 101)
        if not self.started:
            self.teams.append(team)
            team.setSeed(seed)
        else:
            print('Tournament has started, cannot add team')

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

    def start(self):
        if not self.started:
            self.started = True
            if self.elims == 1: #Single Elimination
                numTeams = len(self.teams)
                depth = math.ceil(math.log(numTeams, 2))
                totGames = numTeams - 1

                # Sort teams by seed
                self.teams.sort(key=lambda x: x.seed, reverse=False)
                for idx in range(0, numTeams):
                    self.teams[idx].setSeed(idx + 1)

                gAdded = 0
                botGames = 0
                for i in range(0, depth):
                    botGames = 0
                    games = []
                    for j in range(0, (2**i)):
                        if gAdded < totGames: #Add Game
                            gAdded+=1
                            botGames+=1
                            newGame = Game(uuid.uuid4())
                            games.append(newGame)
                    self.games.append(games)


                teamSet = 0
                curDepth = depth
                teamAdded = []
                teamAdded.append(0)
                for round in reversed(self.games):
                    seed = 2**curDepth + 1
                    for game in reversed(round):
                        teamIdx = len(self.teams) - len(teamAdded) + 1
                        if teamIdx not in teamAdded:
                            game.setAwayTeam(self.teams[teamIdx-1])
                            teamAdded.append(teamIdx)
                        teamIdx = seed - teamIdx
                        if teamIdx not in teamAdded:
                            game.setHomeTeam(self.teams[teamIdx-1])
                            teamAdded.append(teamIdx)
                        else:
                            if game.getAwayTeam():
                                game.setHomeTeam(game.getAwayTeam())
                                game.setAwayTeam(None)
                        # Make sure home and away is correct
                        if game.getAwayTeam() and game.getHomeTeam():
                            if game.getAwayTeam().seed < game.getHomeTeam().seed:
                                tempTeam = game.getAwayTeam()
                                game.setAwayTeam(game.getHomeTeam())
                                game.setHomeTeam(tempTeam)


                    curDepth-=1

                self.teams.sort(key=lambda x: x.seed, reverse=False)
                roundIdx = 1
                for round in self.games:
                    print('====Round {}===='.format(roundIdx))
                    for game in round:
                        print(game)
                    roundIdx+=1

            else: # Double Elimination
                pass
        else:
            print('Tournament Already Started')


    def update(self):
        for idx in range(len(self.games)-2, -1, -1):
            count = 0
            for game in self.games[idx]:
                if not game.getAwayTeam():
                    game.setAwayTeam(self.games[idx+1][count].getWinningTeam())
                    count+=1
                if not game.getHomeTeam():
                    game.setHomeTeam(self.games[idx+1][count].getWinningTeam())
                    count+=1

        print('')
        roundIdx = 1
        for round in self.games:
            print('====Round {}===='.format(roundIdx))
            for game in round:
                print(game)
            roundIdx+=1



