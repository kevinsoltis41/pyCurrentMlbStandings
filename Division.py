class Division:
	def __init__(self, league, div):
		self.league = league
		self.division = div
		self.teamList = []

	def addTeam(self, team):
		self.teamList.append(team)

	def printDivision(self):
		returnString = '##############################\n'
		returnString += '#\t' + self.league.upper() + ' ' + self.division.upper() + '\n'
		for t in self.teamList:
			returnString += '#\t  (' + str(t.gamesBack) + ') ' + t.toString() + ' -- (' + str(t.won) + ')/(' + str(t.lost) + ')\n'
		returnString += '##############################'

		return returnString
