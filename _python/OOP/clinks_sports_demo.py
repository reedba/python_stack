scorecard = {
    'points':38,
    'rebounds':45,
    'turnovers':90
}

scorecard = {
    'points':38,
    'rebounds':45,
    'turnovers':90
}

class ScoreCard:
    def __init__(self, points, rebounds, turnovers):
        self.points = points
        self.rebounds = rebounds
        self.turnovers = turnovers
    
    def printPoints(self):
        print("I scored", self.points,"points")


Game1 = ScoreCard(32, 8, 4)

Game1.printPoints()



class Player():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.points = 0
        self.rebounds = 0
        self.turnovers = 0

    def printPoints(self):
        print(self.first_name, self.last_name,"has scored: ", self.points, " points this season")

    def addScore(self, points= 0, rebounds = 0, turnovers = 0):
        self.points += points
        self.rebounds += rebounds
        self.turnovers += turnovers
        return self
    def __repr__(self):
        return self.first_name + self.last_name


class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.rebounds = 0
        self.turnovers = 0
        self.players = []
    
    def addPlayer(self, player = Player("default","default")):
        self.points += player.points
        self.rebounds += player.rebounds
        self.turnovers += player.turnovers
        self.players.append(player)
        return self

    def printPoints(self):
        print("The", self.name, "have scored", self.points, " points this season")
        return self

Nuggets = Team("Nuggets")
player1 = Player("Nikola", "Jokic")
player2 = Player("Jamal", "Murray")

player1.addScore(20,30,1)
player2.addScore(17,8, 6)

print(Nuggets.addPlayer(player1).addPlayer(player2).printPoints().players)







#player1 = Player("Brandon", "Reed")
#
#player1.addScore()
#player1.addScore()
#player1.printPoints()
#print(player1.last_name)

