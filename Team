class Team:
	def __init__(self, rank, won, lost, streak, fn, ln, tid, gb, pf, pa, hw, hl, aw, al, cw, cl, lv, lt, conf, div, gp):		
		self.rank = rank
		self.won = won
		self.lost = lost
		self.streak = streak
		self.firstName = fn
		self.lastName = ln
		self.team_id = tid
		self.gamesBack = gb
		self.pointsFor = pf
		self.pointsAgainst = pa
		self.homeWon = hw
		self.homeLost = hl
		self.awayWon = aw
		self.awayLost = al
		self.conferenceWon = cw
		self.conferenceLost = cl
		self.lastFive = lv
		self.lastTen = lt
		self.conference = conf
		self.division = div
		self.gamesPlayed = gp
		self.pointsScoredPerGame = self.pointsFor / self.gamesPlayed
		self.pointsAllowedPerGame = self.pointsAgainst / self.gamesPlayed
		self.winPercentage = self.won / self.gamesPlayed
		self.pointDifferential = self.pointsFor - self.pointsAgainst
		self.pointDifferentialPerGame = self.pointDifferential / self.gamesPlayed

	def toString(self):
		return self.firstName + ' ' + self.lastName
