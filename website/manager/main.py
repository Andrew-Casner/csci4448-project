import uuid
from manager.Game import Game
from manager.Player import Player
from manager.Coach import Coach
from manager.Team import Team
from manager.Tournament import Tournament

class Runner:
    def __init__(self):

        self.players = []
        self.teams = []
        # Create Players
        self.p1 = Player(uuid.uuid4(), 'Drew', 'Casner')
        self.p2 = Player(uuid.uuid4(), 'RJ', 'Morley')
        self.p3 = Player(uuid.uuid4(), 'Jesper', 'Stryen')
        self.p4 = Player(uuid.uuid4(), 'Austin', 'Smith')
        self.p5 = Player(uuid.uuid4(), 'Lucas', 'Sward')
        self.p6 = Player(uuid.uuid4(), 'Ben', 'Settlerquist')
        self.p7 = Player(uuid.uuid4(), 'Powell', 'Hinson')
        self.p8 = Player(uuid.uuid4(), 'Quinn', 'Mahone')
        self.p9 = Player(uuid.uuid4(), 'Colt', 'Wise')
        self.p10 = Player(uuid.uuid4(), 'Ryan', 'Becker')
        self.p11 = Player(uuid.uuid4(), 'Matt', 'Skogen')
        self.p12 = Player(uuid.uuid4(), 'Isaiah', 'Jones')
        self.p13 = Player(uuid.uuid4(), 'John', 'Gadbois')
        self.p14 = Player(uuid.uuid4(), 'Kian', 'Tanner')
        self.p15 = Player(uuid.uuid4(), 'Pete', 'Snowden')
        self.p16 = Player(uuid.uuid4(), 'Nick', 'Hearon')

        self.players.append(self.p1)
        self.players.append(self.p2)
        self.players.append(self.p3)
        self.players.append(self.p4)
        self.players.append(self.p5)
        self.players.append(self.p6)
        self.players.append(self.p7)
        self.players.append(self.p8)
        self.players.append(self.p9)
        self.players.append(self.p10)
        self.players.append(self.p11)
        self.players.append(self.p12)
        self.players.append(self.p13)
        self.players.append(self.p14)
        self.players.append(self.p15)
        self.players.append(self.p16)


        # Create Teams
        self.t1 = Team(uuid.uuid4(), 'The Killerz', 'Boulder', 'Colorado')
        self.t1.addPlayer(self.p1)
        self.t1.addPlayer(self.p2)
        self.t2 = Team(uuid.uuid4(), 'The Vikings', 'New York', 'New York')
        self.t2.addPlayer(self.p3)
        self.t2.addPlayer(self.p4)
        self.t3 = Team(uuid.uuid4(), 'The High Flyers', 'Austin', 'Texas')
        self.t3.addPlayer(self.p6)
        self.t3.addPlayer(self.p7)
        self.t4 = Team(uuid.uuid4(), 'The Ballers', 'Aurora', 'Colorado')
        self.t4.addPlayer(self.p5)
        self.t4.addPlayer(self.p8)
        self.t5 = Team(uuid.uuid4(), 'The Wurst', 'Boulder', 'Colorado')
        self.t5.addPlayer(self.p9)
        self.t5.addPlayer(self.p10)
        self.t6 = Team(uuid.uuid4(), 'Da N3rds', 'Seattle', 'Washington')
        self.t6.addPlayer(self.p11)
        self.t6.addPlayer(self.p12)
        self.t7 = Team(uuid.uuid4(), 'The Climbers', 'LA', 'Cali')
        self.t7.addPlayer(self.p13)
        self.t7.addPlayer(self.p14)
        self.t8 = Team(uuid.uuid4(), 'Rockstars', 'Summit County', 'Colorado')
        self.t8.addPlayer(self.p15)
        self.t8.addPlayer(self.p16)

        self.teams.append(self.t1)
        self.teams.append(self.t2)
        self.teams.append(self.t3)
        self.teams.append(self.t4)
        self.teams.append(self.t5)
        self.teams.append(self.t6)
        self.teams.append(self.t7)
        self.teams.append(self.t8)

        # Test Game
        #g1 = Game(uuid.uuid4(), self.t1, self.t2)

        # Create Tournament
        self.turny1 = Tournament(uuid.uuid4(), 'Champions Club', 1, 8*60, 60)
        self.turny1.addTeam(self.t1, 0)
        self.turny1.addTeam(self.t2, 0)
        self.turny1.addTeam(self.t3, 0)
        self.turny1.addTeam(self.t4, 0)
        self.turny1.addTeam(self.t5, 0)
        self.turny1.addTeam(self.t6, 0)
        self.turny1.addTeam(self.t7, 0)
        self.turny1.addTeam(self.t8, 0)
        self.turny1.start()

        # Update results
        '''
        self.turny1.getGames()[2][0].setScoreHome(90)
        self.turny1.getGames()[2][0].setScoreAway(80)
        self.turny1.getGames()[2][0].gameComplete()
        print('')
        print(self.turny1.getGames()[2][0].getWinningTeam())
        print('')
        self.turny1.update()
        #'''


    def getPlayers(self):
        return self.players

    def getTeams(self):
        return self.teams

    def getTourny(self):
        return self.turny1
