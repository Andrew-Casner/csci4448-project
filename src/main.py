import uuid
from Game import Game
from Player import Player
from Coach import Coach
from Team import Team
from Tournament import Tournament

def main():
    # Create Players
    p1 = Player(uuid.uuid4(), 'Drew', 'Casner')
    p2 = Player(uuid.uuid4(), 'RJ', 'Morley')
    p3 = Player(uuid.uuid4(), 'Jesper', 'Stryen')
    p4 = Player(uuid.uuid4(), 'Austin', 'Smith')
    p5 = Player(uuid.uuid4(), 'Lucas', 'Sward')
    p6 = Player(uuid.uuid4(), 'Ben', 'Settlerquist')
    p7 = Player(uuid.uuid4(), 'Powell', 'Hinson')
    p8 = Player(uuid.uuid4(), 'Quinn', 'Mahone')
    p9 = Player(uuid.uuid4(), 'Colt', 'Wise')
    p10 = Player(uuid.uuid4(), 'Ryan', 'Becker')
    p11 = Player(uuid.uuid4(), 'Matt', 'Skogen')
    p12 = Player(uuid.uuid4(), 'Isaiah', 'Jones')
    p13 = Player(uuid.uuid4(), 'John', 'Gadbois')
    p14 = Player(uuid.uuid4(), 'Kian', 'Tanner')
    p15 = Player(uuid.uuid4(), 'Pete', 'Snowden')
    p16 = Player(uuid.uuid4(), 'Nick', 'Hearon')

    # Create Teams
    t1 = Team(uuid.uuid4(), 'The Killerz', 'Boulder', 'Colorado')
    t1.addPlayer(p1)
    t1.addPlayer(p2)
    t2 = Team(uuid.uuid4(), 'The Vikings', 'New York', 'New York')
    t2.addPlayer(p3)
    t2.addPlayer(p4)
    t3 = Team(uuid.uuid4(), 'The High Flyers', 'Austin', 'Texas')
    t3.addPlayer(p6)
    t3.addPlayer(p7)
    t4 = Team(uuid.uuid4(), 'The Ballers', 'Aurora', 'Colorado')
    t4.addPlayer(p5)
    t4.addPlayer(p8)
    t5 = Team(uuid.uuid4(), 'The Wurst', 'Boulder', 'Colorado')
    t5.addPlayer(p9)
    t5.addPlayer(p10)
    t6 = Team(uuid.uuid4(), 'Da N3rds', 'Seattle', 'Washington')
    t6.addPlayer(p11)
    t6.addPlayer(p12)
    t7 = Team(uuid.uuid4(), 'The Climbers', 'LA', 'Cali')
    t7.addPlayer(p13)
    t7.addPlayer(p14)
    t8 = Team(uuid.uuid4(), 'Rockstars', 'Summit County', 'Colorado')
    t8.addPlayer(p15)
    t8.addPlayer(p16)

    # Test Game
    g1 = Game(uuid.uuid4(), t1, t2)

    # Create Tournament
    turny1 = Tournament(uuid.uuid4(), 'Champions Club', 1, 8*60, 60)
    turny1.addTeam(t1, 0)
    turny1.addTeam(t2, 0)
    turny1.addTeam(t3, 0)
    turny1.addTeam(t4, 0)
    turny1.addTeam(t5, 0)
    #turny1.addTeam(t6, 0)
    #turny1.addTeam(t7, 0)
    #turny1.addTeam(t8, 0)
    turny1.start()

    # Update results
    turny1.getGames()[2][0].setScoreHome(90)
    turny1.getGames()[2][0].setScoreAway(80)
    turny1.getGames()[2][0].setScoreAway(80)
    turny1.getGames()[2][0].gameComplete()
    print(turny1.getGames()[2][0].getWinningTeam())
    turny1.update()


if __name__=='__main__':
    main()
